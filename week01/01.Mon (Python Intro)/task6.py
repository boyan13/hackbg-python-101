#Vowels in a string
def count_vowels(s):
	vows = {'a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'Y'}
	sum = 0
	for i in s:
		if i in vows:
			sum += 1

	return sum

print( count_vowels("Python")              ) #2
print( count_vowels("Theistareykjarbunga") ) #8 (It's a volcano name lol)
print( count_vowels("grrrrgh!") 		   ) #0
print( count_vowels("""Github is the second 
					best thing that happend 
					to programmers, after 
					the keyboard!""") 	   ) #22
print( count_vowels("A nice day to code!") ) #8