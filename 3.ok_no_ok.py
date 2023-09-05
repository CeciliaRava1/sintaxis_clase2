words = ''
char_alphabet = []
word_list = []
words_ok = []
words_no_ok = []
alphabet = ''
init = 0
end = 0
reached = 0
list_char_no_alphabet = []

#Type an alphabet
while reached != 1:
	alphabet = input('Type an alphabet between "{}" and separate elements with ","')
	if alphabet[0] == "{" and alphabet[-1] == "}":
		reached = 1

#Type words
reached = 0
while reached != 1:
	words = input('Type words separates with ",". Type "," in the last char')
	if " " not in words and words[-1] == ',':
		reached = 1

#Save chars of alphabet in list
for i in alphabet:
	if i != "{" and i != "}" and i != ",":
		char_alphabet.append(i)

for i in words:
	if i != ',':
		word_list.append(i)
	else:
		word_list.append(i)

#word_ok and no_ok
no = ''
reached = 1
number_word_no_ok = 0
for i in words:
	if i != ',':
		end += 1
	else:
		for i in range (init,end):
			if words[i] not in alphabet:
				reached = 0
				no += words[i]
				no += ' '
		if reached == 0:
			words_no_ok.append(words[init:end])
			number_word_no_ok += 1
			end += 1
			init = end
			list_char_no_alphabet.append(no)
			no = ''
		else:
			words_ok.append(words[init:end])
			end += 1
			init = end

#Print results
for i in words_ok:
	print(f'{i} "OK"')

position = 0
for i in words_no_ok:
	print(f'{i} NO OK, chars not in alphabet {list_char_no_alphabet[position]}')
	position += 1
