#Sort Array Of Fractions

#list of fractions represented by tuples with no more than 2 members
def validate_sort_array_of_fractions_arguments(fractions = None):

	if fractions is None:
		return True

	if type(fractions) is not list:
		raise Exception("Bad type. Expected list of tuples.")

	for fraction in fractions:

		if type(fraction) is not tuple:
			raise Exception("Bad fraction type. Expected tuple.")

		if len(fraction) > 2:
			raise Exception("Fraction with more than 2 members.")

		if len(fraction) == 0:
			raise Exception("Empty fraction.")

		for member in fraction:
			if type(member) is not int:
				raise Exception("Non-integer fraction member.")

	return True

#relies on validated input
def format_fraction(fraction):
	if len(fraction) == 2:
		return fraction

	elif len(fraction) == 1:
		return (fraction[0], 1)

	else:
		return (0, 1)

#relies on validated input
def is_greater_than(f1, f2):

	numerator1, denominator1 = format_fraction(f1)
	numerator2, denominator2 = format_fraction(f2)

	if denominator1 == 0 or denominator2 == 0:
		raise Exception("Zero division!")

	if denominator1 < 0:
		numerator1 *= -1
		denominator1 *= -1

	if denominator2 < 0:
		numerator2 *= -1
		denominator2 *= -1

	return numerator1 * denominator2 > numerator2 * denominator1

	return False

#relies on validated input
def getpos_min(array = None):
	if array is None:
		return None

	buf = None
	pos = None

	for i in range(len(array)):
		if buf is None:
			buf = array[i]
			pos = i
		else:
			if is_greater_than(buf, array[i]):
				buf = array[i]
				pos = i

	return pos


#relies on validated input
def find_max(array = None):
	if array is None:
		return None

	m = None

	for i in range(len(array)):
		if m is None:
			m = array[i]
		else:
			if is_greater_than(array[i], m):
				m = array[i]

	return m

#sorting in another array
def sort_array_of_fractions(fractions = None, ascending = True):

	
	validate_sort_array_of_fractions_arguments(fractions)

	if fractions is None or fractions == list():
		return []

	fractionsC = fractions[:]

	sortedArray = []
	biggest = find_max(fractionsC)

	for i in range(len(fractionsC) - 1):
		indexOfSmallest = getpos_min(fractionsC)
		smallest = fractionsC[indexOfSmallest]

		sortedArray.append(smallest)
		fractionsC[indexOfSmallest] = biggest

	sortedArray.append(biggest)

	if ascending:
		return sortedArray
	else:
		return sortedArray[::-1]

def main():
	pass

if __name__ == '__main__':
	main()