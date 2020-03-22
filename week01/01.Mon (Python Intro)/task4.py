#Factorial Digits
def fact_digits(n):
	li = [int(i) for i in str(n)]
	sum = 0

	for i in li:
		buf = i
		ssum = 1

		while (buf > 0):
			ssum *= buf
			buf -= 1

		sum += ssum

	return sum

print( fact_digits(111) ) #3
print( fact_digits(145) ) #145
print( fact_digits(999) ) #1088640