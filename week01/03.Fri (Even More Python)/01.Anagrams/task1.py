#Anagrams

def anagrams(w1, w2):
	if len(w1) != len(w2):
		return "NOT ANAGRAMS"

	li1 = [i.lower() for i in w1]
	li2 = [i.lower() for i in w2]

	for i in range(len(li2)):
		for j in range(len(li1)):
			if li2[i] == li1[j]:
				del li1[j]
				break
		else:
			return "NOT ANAGRAMS"

	if len(li1) == 0:
		return "ANAGRAMS"
	else:
		return "NOT ANAGRAMS"



userinput = input("Two words: ")
hold = userinput.split(" ")

if(len(hold) > 2):
	print("Too many words!")
	exit()
elif(len(hold) < 2):
	print("Too few words!")
	exit()

print( anagrams(hold[0], hold[1]) )

#e.g. BRADE BEARD (True)
#e.g. ONE TWO 	  (False)
#e.g. BRADE beard (True)