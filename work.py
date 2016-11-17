word_letter = "word"
text_new = '*' * len(word_letter)
print text_new

while "*" in text_new:
	user = raw_input("Enter letter:")
	dop = ""
	for number in range(len(word_letter)):
		if user == word_letter[number]:
			dop = dop + user
		else:
			dop = dop + text_new[number]
			print "No letter"
			break
	text_new = dop
	print text_new
