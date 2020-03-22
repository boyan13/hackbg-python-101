#Char Histogram
import string

def char_histogram(text):
	stuff = set()

	for symbol in text:
		if symbol not in string.whitespace:
			stuff.add(symbol)

	histogram = dict() 

	for symbol in sorted(stuff):
		histogram[symbol] = text.count(symbol)

	return histogram

print( char_histogram("Python!") )
print( char_histogram("AAAAaaa!") )