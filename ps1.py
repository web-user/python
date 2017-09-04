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

# import requests
# from bs4 import BeautifulSoup


# def trade_spider(max_pages):
# 	page = 1
# 	page_attr_my = ''
# 	while page <= max_pages:
# 		url = "https://auto.ria.com/moto/mopedy/?page=" + str(page)
# 		source_code = requests.get(url)
# 		plain_text = source_code.text
# 		soup = BeautifulSoup(plain_text)
# 		for link in soup.findAll("a", {"class": "address"}):
# 			href = link.get("href")
# 			title = link.get("title")
# 			print(title)
# 			print(href)
# 			get_single_item_data(href)
# 		page += 1

# def get_single_item_data(item_url):
# 	source_code = requests.get(item_url)
# 	plain_text = source_code.text
# 	soup = BeautifulSoup(plain_text)
# 	for item_name in soup.findAll("span", {"class": "price"}):
# 		print(item_name.string)
# 	for item_name in soup.findAll("div", {"id": "description"}):
# 		print(item_name)


# trade_spider(1)









from random import randint
# def reverse_name(first_name,last_name):
#     if first_name and last_name:
#         reversed_name = ' '.join([last_name, first_name])
#     else:
#         reversed_name = 'Error'
#     return reversed_name

# first_name = raw_input('What is first name? ')
# last_name = raw_input('What is last namee? ')
# print(reverse_name(first_name, last_name))

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

# print(find('azc bob bob egghakl ber bob', 'b'))



# string = 'bala la yka la'
# substring = 'la'
# messege = 'No'

# print(string.count(substring) or messege)


balance = 4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
month = 1
totalPay = 0

while month < 13:
    minimum_monthly_payment = balance * monthlyPaymentRate
    print "Month: " + str(month)
    print "Minimum monthly payment: " + str(round(minimum_monthly_payment, 2))
    balance = (balance - (balance*monthlyPaymentRate))*(1+(annualInterestRate/12))
    print "Remaining balance: " + str(round(balance, 2))
    totalPay += minimum_monthly_payment
    if month == 12:
        print "Total paid:" + str(totalPay)
    month += 1

# def count_small(numbers):
#     total = 0
#     for n in numbers:
#         if n < 10:
#             total = total + 1
#     return total

# lost = [4, 8, 15, 16, 23, 42]
# small = count_small(lost)
# print "Total: " + str(small)

# shopping_list = ["banana", "orange", "apple", "pear"]

# stock = {
#     "banana": 6,
#     "apple": 0,
#     "orange": 32,
#     "pear": 15
# }
    
# prices = {
#     "banana": 4,
#     "apple": 2,
#     "orange": 1.5,
#     "pear": 2
# }

# # Write your code below!
# def compute_bill(food):
#     total = 0
#     for item in food:
#         if stock[item] > 0:
#             total += prices[item]
#     return total

# print compute_bill(shopping_list)

# # Generates a number from 1 through 10 inclusive
# random_number = randint(1, 10)

# guesses_left = 3
# # Start your game!

# while guesses_left > 0:
#     guess = int(raw_input("Your guess: "))
#     guesses_left -= 1
#     print "Our number is: ", random_number
#     print "Your number is: ", guess
    
#     if guess == random_number:
#         print "you win!"
#         break
# else:
#     print "You louse!"

# def is_int(x):
#     if x - int(x) == 0:
#         return True
#     else:
#         return False

# print is_int(1.0)

# def reverse(word):
#     reverse_word = []
#     rev_i = len(word) - 1
#     for letter in word:
#         if rev_i >= 0:
#             reverse_word.append(word[rev_i])
#             rev_i -= 1
#         else:
#             break
#     result = ''.join(reverse_word)
#     return result
    
    
# text = "Volo Tom"

# print reverse(text)



