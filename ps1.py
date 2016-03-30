# def reverse_name(first_name,last_name):
#     if first_name and last_name:
#         reversed_name = ' '.join([last_name, first_name])
#     else:
#         reversed_name = 'Error'
#     return reversed_name

# first_name = raw_input('What is first name? ')
# last_name = raw_input('What is last namee? ')
# print(reverse_name(first_name, last_name))
# python stop 
# import sys
# sys.exit("Error message")

# a = [1, 4, 5, 7, 8, 0, 23]

# currenr = None

# while currenr != 0:
#     currenr = a.pop(0)
#     print(currenr)
# print('End')

def find(string, substring):
    counter = 0
    for start in range(len(string) - len(substring)):
        if string[start: start + len(substring)] == substring:
            counter += 1
    return counter

print(find('azc bob obegghakl bob', 'bob'))



def search(sub, st):
    count = 0
    for i in range(len(st) - len(sub)):
        if  st[i: i + len(sub)] == sub:
            count += 1
    return count

res = search('12','hello 12 2 e worl 12 de')

if res > 0:
    print(res)
else:
    print('No search')