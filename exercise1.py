def boogle(words):
	points = 0
	for i in range(0, len(words)):
		if len(words[i]) <= 4:
			points += 1
		elif len(words[i]) == 5:
			points += 2
		elif len(words[i]) == 6:
			points += 3
		elif len(words[i]) == 7:
			points += 5
		elif len(words[i]) > 7:
			points += 11
	return points
	
print(boogle(["cat", "tea", "mate", "computer", "ale", "bat"]))
print(boogle(["honest", "yelps", "yelp", "python", "pythons"]))

