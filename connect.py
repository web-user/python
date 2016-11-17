import MySQLdb
import time
conn = MySQLdb.connect("localhost","root","qwerty","python")
c  = conn.cursor()

user = "Python"
tweet = 'Hi, thaks! der as breb'

# c.execute("INSERT IGNORE INTO taula (time, user, tweet) VALUES (%s,%s,%s) ON DUPLICATE KEY UPDATE tweet = tweet", (time.time(), user, tweet) )

# conn.commit()

c.execute("SELECT * FROM link WHERE tweet = %s", [tweet])

rows = c.fetchall()

if len(rows) > 0:
	print "Yes"
else:
	print "No"
	c.execute("INSERT INTO taula (time, user, tweet) VALUES (%s,%s,%s)", (time.time(), user, tweet) )
	conn.commit()
	c.execute("SELECT * FROM taula WHERE tweet = %s", [tweet])
	rows = c.fetchall()

for eachRow in rows:
	d = dict(time=time.asctime( time.localtime(eachRow[0]) ), name=eachRow[1], tweet=eachRow[2])
	print eachRow[2]




# import requests
# from bs4 import BeautifulSoup
# import MySQLdb
# import time
# conn = MySQLdb.connect("localhost","root","qwerty","python")
# c  = conn.cursor()



# def trade_spider(max_pages):

#     page = 1
#     page_attr_my = ''
#     while page <= max_pages:
# 		url = "https://auto.ria.com/legkovie/?page=" + str(page)
# 		source_code = requests.get(url)
# 		plain_text = source_code.text
# 		soup = BeautifulSoup(plain_text)

# 		for link in soup.findAll("a", {"class": "address"}):
# 			href = link.get("href")
# 			title = link.get("title")
# 			print title
# 			# print href
# 			c.execute("SELECT * FROM link WHERE linn_txt = %s", [href])
# 			rows = c.fetchall()
# 			if len(rows) > 0:
# 				print "Yes"
# 				c.execute("SELECT * FROM link",)
# 				rows = c.fetchall()
# 				for eachRow in rows:
# 					# d = dict(time=time.asctime( time.localtime(eachRow[0]) ), name=eachRow[1], tweet=eachRow[2])
# 					print eachRow[1]
# 			else:
# 				print "No"
# 				c.execute("INSERT INTO link (time, linn_txt) VALUES (%s,%s)", (time.time(), href) )
# 				conn.commit()
# 				c.execute("SELECT * FROM link",)
# 				rows = c.fetchall()
# 				for eachRow in rows:
# 					# d = dict(time=time.asctime( time.localtime(eachRow[0]) ), name=eachRow[1], tweet=eachRow[2])
# 					print eachRow[1]
# 		page += 1

# trade_spider(1)




