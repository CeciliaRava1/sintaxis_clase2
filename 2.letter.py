string = input('Type something to know the quantify of one letter')
quantify_of_letter = 0
reached = 0
letter = ''

while reached != 1:
	letter = input('Type a letter to find in the text')
	if len(letter) == 1:
		reached = 1
	else:
		print('Type only one char, try again')


for i in string:
	if i == letter:
		quantify_of_letter += 1

print(f'The quantify of letter {letter} in the text is {quantify_of_letter}')
