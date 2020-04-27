#Python sort
def my_sort(iterable = None, ascending = True, key = None): #insertion sort
	if iterable is None:
		iterable = []

	if type(iterable) != list and type(iterable) != tuple:
		raise Exception("Type must be a list or a tuple!")

	if len(iterable) == 0:
		return iterable

	sortedStrings = [] #plaaceholder for sorted strings
	sortedNumerics = [] #placeholder for sorted numbers

	#Check if it's a list-dictionary
	check = [member for member in iterable if type(member) == dict]
	if len(check) == 0: #If no dictionary member was found
		isDictionary = False #This is not a list dictionary

	elif len(check) == len(iterable): #If all members are dictionaries
		isDictionary = True #This is a list dictionary
		if (key == None): 
			raise Exception("Must provide a key when passing a list dictionary!")
		else:
			for member in check:
				if (key not in member.keys()):
					raise Exception("A list dictionary member is missing passed key!")

	else: #Else, the list contains dictionary members mixed with other types
		raise Exception("List dictionary contains non-dictionary types!")

	for thing in iterable:
		i = 0	

		if (isDictionary): #List dictionary case
			if (type(thing[key]) == str): #If value is a string

				#Find its place in the relevant sorted list
				while (i < len(sortedStrings)):
					if (thing[key] > sortedStrings[i][key]):
						i += 1
					else:
						break

				#Insert it in the appropriate place
				sortedStrings.insert(i, thing)

			else: #Else, when value is a number

				#Find its place in the relevant sorted list
				while (i < len(sortedNumerics)):
					if (thing[key] > sortedNumerics[i][key]):
						i += 1
					else:
						break

				#Insert it in the appropriate place
				sortedNumerics.insert(i, thing)


		else: #Regular case
			if (type(thing) == str): #If value is a string

				#Find its place in the relevant sorted list
				while (i < len(sortedStrings)):
					if (thing > sortedStrings[i]):
						i += 1
					else:
						break

				#Insert it in the appropriate place
				sortedStrings.insert(i, thing)

			else: #Else, when value is a number

				#Find its place in the relevant sorted list
				while (i < len(sortedNumerics)):
					if (thing > sortedNumerics[i]):
						i += 1
					else:
						break

				#Insert it in the appropriate place
				sortedNumerics.insert(i, thing)

	sortedIterable = sortedNumerics + sortedStrings

	if (not ascending):
		sortedIterable = sortedIterable[::-1]

	if (type(iterable) == list):
		return sortedIterable
	else:
		return tuple(sortedIterable)


def main():
	pass
		

if __name__ == '__main__':
	main()