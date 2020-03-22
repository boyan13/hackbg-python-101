#Consonants in a string
def count_consonants(s):
	s = str(s)
	sum = 0
	vows = ('a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'Y')

	for i in range(len(s)):
		if (not(s[i] in vows) and ((s[i] > 'a' and s[i] <= 'z') or (s[i] > 'A' and s[i] <= 'Z'))):
			sum+=1

	return sum

print( count_consonants("Python")              ) #4
print( count_consonants("Theistareykjarbunga") ) #11 (It's a volcano name lol)
print( count_consonants("grrrrgh!") 		   ) #7
print( count_consonants("""Github is the second 
						   best thing that happend 
						   to programmers, after 
						   the keyboard!""")   ) #44
print( count_consonants("A nice day to code!") ) #6