reached = 0
word_list = []
possible_combination = []
words = ''
init = 0
end = 0
word = ''
language_1 = ''
language_2 = ''
list_language_1 = []
list_language_2 = []

print('Language 1 = quantify of symbols than language 2')
#Type first language
while reached != 1:
	language_1 = input('Type syllabes for the first language, between "{}" and separates with ","')
	if language_1[0] == "{" and language_1[-1] == "}" and language_1 not in ' ':
		reached = 1

#Type second language
reached = 0
while reached != 1:
	language_2 = input('Type syllabes for the second language, between "{}" and separates with ","')
	if language_2[0] == "{" and language_2[-1] == "}" and language_2 not in ' ':
		if len(language_1) != len(language_2):
			print(f'Language 2 must have {len(language_1)} elements. Try again')
		else:
			reached = 1

#Type words
reached = 0
while reached != 1:
	words = input('Type words between "{}" and separates with ",". Two syllabes')
	if words[0] == "{" and words[-1] == "}" and words not in ' ':
		reached = 1

#Separate words in list
for i in range(1, len(words)-1):
	if words[i] != ',' and words[i] != "{" and words[i] != "}":
		end += 1
		word += words[i]
	else:
		word_list.append(word)
		reached = 1
		init = end+1
		end = 0
		word = ''
word_list.append(word)

word = ''
init = 0
end = 0
reached = 0
#Save syllabes in list language 1
for i in range(1, len(language_1)-1):
	if language_1[i] != ',' and language_1[i] != "{" and language_1[i] != "}":
		end += 1
		word += language_1[i]
	else:
		list_language_1.append(word)
		reached = 1
		init = end+1
		end = 0
		word = ''
list_language_1.append(word)

word = ''
#Save syllabes in list language 2
for i in range(1, len(language_2)-1):
	if language_2[i] != ',' and language_2[i] != "{" and language_2[i] != "}":
		end += 1
		word += language_2[i]
	else:
		list_language_2.append(word)
		reached = 1
		init = end+1
		end = 0
		word = ''
list_language_2.append(word)

#Possible combinations in list
word = ''
position = 0
for i in list_language_1:
	position = 0
	word = ''
	while position < len(list_language_1):
		word = i + list_language_2[position]
		possible_combination.append(word)
		position += 1

#Word in possible combination?
for i in word_list:
	if i in possible_combination:
		print(f"{i} it's a possible combination")
	else:
		print(f"{i} it's not a possible combination")
