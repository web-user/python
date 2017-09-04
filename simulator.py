#!/usr/bin/env python3

# Import random numbers.
try:
  # this should be the normal path if Python has access to the standard library. 
  import random
except:
  # This is a fallback for IronPython when running wihtout access to the standard library
  import _random as random

g_rand = random.Random()


#---------------------------------
# Different attack policies

# Policy: attack the weakest guy on the other side
def PickWeakest(army):
    h = [(a.health if a.IsAlive() else 1000) for a in army]
    sickest = min(h)
    idx = h.index(sickest)
    return army[idx]

# Policy: Pick a random opponent in the enemy army
def PickRandom(army): 
    alive=[a for a in army if a.IsAlive()]
    assert(len(alive) > 0)
    idx = int(g_rand.random() * len(alive))
    return alive[idx]

#---------------------------------
# Inidividual unit.
class Unit:
  def __init__(self, fpAttackPolicy=PickWeakest):
    self.healthStart = self.health=50
    self.fpAttackPolicy = fpAttackPolicy
  def __str__(self):
    return "health: %d/%d" % (self.health, self.healthStart)
  def ApplyDamage(self, d):
    self.health -= d
    if (self.health < 0): self.health = 0
  # Return true iff is alive.
  def IsAlive(self): 
    return (self.health > 0)
  # Pick a target in the opposing army.
  def PickTarget(self, army):
    guy = self.fpAttackPolicy(army)
    assert(guy.IsAlive())
    return guy

#---------------------------------
# Given 2 arrays of armies, do a single round of attacks. 
# Return True if both armies are still alive. 
def Attack1(a1, a2):
  # 1) calculate targets
  # each alive unit can attack another unit.
  t1 = [x.PickTarget(a2) for x in a1 if x.IsAlive()]
  t2 = [x.PickTarget(a1) for x in a2 if x.IsAlive()]
  assert(len(t1) > 0)
  assert(len(t2) > 0)  
  # 2) apply targets.  
  # Apply all attacks at once, to avoid giving bias to order of attack. 
  # This allows 2 units to kill each other. 
  for x in (t1 + t2):
    x.ApplyDamage(1)
  # 3) check if armies are still alive
  if (NumAlive(a1) == 0): return False
  if (NumAlive(a2) == 0): return False  
  return True

# count how many in army are still alive.
def NumAlive(army):
  c = 0
  for x in army:
    if x.IsAlive(): c+= 1
  return c

#---------------------------------
# Helper functions. 

# Make an army
def Make(size, fpAttackPolicy=PickWeakest):
  return [Unit(fpAttackPolicy) for i in range(size)]

# shorthand for Making army with 'random attack' policy
def MakeR(size):
  return Make(size, PickRandom)

# Returns an anonymous type with fields as stats on an army
#   health = sum current health of army
#   healthStart = sum initial health of army
#   alive = true iff at least one member in army is alive (health > 0)
def Stat(army):
    class S:
      def __init__(self):
        self.health = 0
        self.healthStart = 0
        self.alive = False
      def Apply(self, x):
        self.health += x.health
        self.healthStart += x.healthStart
        if (x.IsAlive()): self.alive = True
    s = S()
    for x in army:
      s.Apply(x)
    return s
    
# return victory margin between 2 armies.
#  = (winner current health / winner starting health) * 100
#   negative for a1, positive for a2
#   0 if both are dead
def VictoryMargin(a1, a2):
    s1 = Stat(a1)
    s2 = Stat(a2)
    if s1.alive:
        assert(not s2.alive)
        return - s1.health * 100 / s1.healthStart
    elif s2.alive:
        assert(not s1.alive)
        return s2.health * 100 / s2.healthStart
    else:
        return 0 # both dead

# Fight the 2 armies until 1 is defeated, printing status at each turn.
# Return a rich summary object.
def Battle(a1, a2):
  turn = 0
  done = False
  print('-----------')
  while(True): 
    # print status
    print('%2d)' % (turn)),
    for x in a1:
      print('%2d' % (x.health)),
    print('|'),
    for x in a2:
      print('%2d' % (x.health)),
     # end of line
    if (done): break
    turn+= 1
    done = not Attack1(a1, a2)
  print('-----------')
  v = VictoryMargin(a1, a2)
  print("done. Margin=%d%% (of victor's original health)" % (v))
  # Create a summary container for results.
  class Res:
    def __init__(self):
      self.turns = turn
      self.victory = v
      self.size1=len(a1) # starting size of each army
      self.size2=len(a2)  
      self.end1 = NumAlive(a1) # ending size of each army
      self.end2 = NumAlive(a2) 
  return Res()

# Simulate
print( '1')
Battle(Make(1), Make(1))

#------------------
# General helper functions for stat stuff 

# return an average from a list of integers
def avg(l): 
    return float(sum(l)) / len(l)

# Run a function n times and return the results in a sequence
def frun(n, func):
    return [func() for i in range(n)]

# Execute a function n times and return the average.
def favg(n, func):
    return avg(frun(n, func))


# ***
# Graph: num turns vs. army size.  (using Pick Weakest)
# For PickWeakest, since both armies are the same size, they always kill each other
# off and the battle is a draw, so VictoryMargin==0.
def NTurns_Weakest(nMax):
    return [Battle(Make(i),Make(i)).turns for i in range(1,nMax+1)]


# Graph: Random vs. Random, same size army.
# Show it averages out to a tie. Look at average victory margin 
# return vector of victory margins for nTimes battles. 
def NVictory_Random(size=5, nTimes=10):
    return frun(nTimes, lambda: Battle(MakeR(size), MakeR(size)).victory)


# ***
# Graph: turns vs. size (using pick random), for 1 <= size  < nMax
# Since we already showed victory margin averages over 0, we ignore that and just focus on turns.
# Since this is a non-determistic algorithm, run nTimes to get an average
# Expect: constant answer
def NTurns_Random(nMax, nTimes=5):
    return [  favg(nTimes, lambda : Battle(MakeR(i),MakeR(i)).turns) for i in range(1,nMax+1)]

# observed: avg(NTurns_Random(10, 5)) = 53.22

# Random vs. Weakest. (Expect attack-weakest to always win)
# Victory margins
# The random activity here averages out so that this is actually almost always deterministic.
# Attack-Weakest kills off the other army determinstically, before it loses any guys (since attack-random
# is spreading out the fire too much to actually kill anybody first) 
def RvsW(nMax, nTimes=1):
  return [  favg(nTimes, lambda : Battle(MakeR(i),Make(i)).victory) for i in range(1,nMax+1)]

# collect more stats: Turns, Victory, End-size
def RvsW2(nMax = 4):
  # get raw data
  b = [Battle(MakeR(i),Make(i)) for i in range(1,nMax+1)]
  # run projection to get interesting fields:
  w=map(lambda i: (i.size2, i.end2, i.turns, i.victory), b)
  return w

# FYI, we could even chain the above statements together like:
#   [(lambda x=i:(x,x*x))() for i in range(1,10)]
# using default parameters, function application


# Margin of victory:
def NMargin_Extra(nMaxDelta = 5, size=10):
  return [Battle(Make(size), Make(size+i)).victory for i in range(nMaxDelta)]

# Produce a vector of 20 cases of the victory margin of a 5 random -on-5 weakest battle.
# frun(20, lambda: Battle(MakeR(5),Make(5)).victory)

# Trials: (Turns, Victory) for nTimes. (armySize = constant)
# Test theory that k1*Turns + k2*Victory = k3.
# frun(Battle(size).[turns, victory])
#
#   l= frun(nTimes, lambda: Battle(size))
#   l2 = select(l, "turns", "victory").