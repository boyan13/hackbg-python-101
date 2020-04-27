#Credit card validation
def is_credit_card_valid(number):
	number = str(number)
	if len(number)%2 == 0:
		return False

	even = [ int(ch) for ch in number[::2] if (ch>='0' and ch<='9')]
	ods = [ int(ch) for ch in number[1::2] if (ch>='0' and ch<='9')]
	
	#in case number contained non-numerics
	if (len(ods)+1 != len(even)):
		return "Input was not a number"

	even[0] = int(even[0])

	for i in range(len(ods)):
		ods[i] = int(ods[i]) * 2
		even[i+1] = int(even[i+1])

	#to avoid using multiple loops,
	#summ is initialized with the last element of even[],
	#since the variance of size between even[] and ods[] is 1,
	#in favor of even[]
	summ = even[len(even)-1] 

	for i in range(len(ods)):
		summ += ods[i]
		summ += even[i]

	if summ % 10 == 0:
		return True

	return False

print( is_credit_card_valid("6161-16"))	   #Input was not a number
print( is_credit_card_valid(79927398713) ) #False
print( is_credit_card_valid(79927398715) ) #True