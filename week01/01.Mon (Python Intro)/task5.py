#Palindrome
def palindrome(n):
	li1 = [str(i) for i in str(n)]
	li2 = []
	for i in range(len(li1)-1,-1,-1):
		li2.append(li1[i])

	for i,j in zip(li1,li2):
		if i != j:
			return False

	return True

print( palindrome(121) 	   ) #True
print( palindrome("kapak") ) #True
print( palindrome("baba")  ) #False