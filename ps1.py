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

# def find(string, substring):
#     counter = 0
#     for start in range(len(string) - len(substring)):
#         if string[start: start + len(substring)] == substring:
#             counter += 1
#     return counter

# print(find('azc bob obegghakl bob', 'bob'))



# def search(sub, st):
#     count = 0
#     for i in range(len(st) - len(sub)):
#         if  st[i: i + len(sub)] == sub:
#             count += 1
#     return count

# res = search('12','hello 12 2 e worl 12 de')

# if res > 0:
#     print(res)
# else:
#     print('No search')

# text_new = ''
# word_letter = "word"
# # Write your code below!
# while len(text_new) < len(word_letter):
#     guess_row = raw_input("Enter letter:")
#     if guess_row not in word_letter:
#         print "No letter"
#         break
#     else:
#         if guess_row not in text_new:
#             text_new += guess_row
#             print text_new
#         else:
#             print("Yes this letter in word!")
#             print text_new
# print "You big game !" + word_letter

import requests
from bs4 import BeautifulSoup


def trade_spider(max_pages):
	page = 1
	page_attr_my = ''
	while page <= max_pages:
		url = "https://auto.ria.com/moto/mopedy/?page=" + str(page)
		source_code = requests.get(url)
		plain_text = source_code.text
		soup = BeautifulSoup(plain_text)
		for link in soup.findAll("a", {"class": "address"}):
			href = link.get("href")
			title = link.get("title")
			print(title)
			print(href)
			get_single_item_data(href)
		page += 1

def get_single_item_data(item_url):
	source_code = requests.get(item_url)
	plain_text = source_code.text
	soup = BeautifulSoup(plain_text)
	for item_name in soup.findAll("span", {"class": "price"}):
		print(item_name.string)
	for item_name in soup.findAll("div", {"id": "description"}):
		print(item_name)


trade_spider(1)













