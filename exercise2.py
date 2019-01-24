def evens(numbers):
	evenNums = list()
	for i in numbers:
		if i % 2 == 0:
			evenNums.append(i)
	return evenNums
	
print(evens([3, 9, 4, 5, 2, 8, 9, 2]))
print(evens([6, 6, 3, 12, 5]))
print(evens([3, 5, 9]))