#Turn a list of digits into a number
def to_number(digits):
	buf = "".join([str(d) for d in digits])
	return int(buf)

print( to_number([1, 2, 3])  		 ) #123
print( to_number([9, 9, 9, 9, 9])    ) #99999
print( to_number([1, 2, 3, 0, 2, 3]) ) #123023
print( to_number([21, 2, 33]) 		 ) #21233