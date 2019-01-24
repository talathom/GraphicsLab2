def shortWords(strings):
	shortStrings = list()
	for word in strings:
		if len(word) <= 2:
			shortStrings.append(word)
	return shortStrings
			
print(shortWords(["I","python", "to", "or", "candy", "as"]))
print(shortWords(["wonder", "to", "beach", "me"]))
print(shortWords(["toolong", "waytoolong"]))
			
	