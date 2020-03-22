#Turn a number into a list of digits
def to_digits(n):
	return [int(i) for i in str(n)]

print( to_digits(123)    ) #ans: [1, 2, 3]
print( to_digits(99999)  ) #ans: [9, 9, 9, 9, 9]
print( to_digits(123023) ) #ans: [1, 2, 3, 0, 2, 3]