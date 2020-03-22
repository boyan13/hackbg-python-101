#Generate file with random integers
import sys
from random import randint

def generate_numbers(filename, numbers):
	try:
		numbers = int(numbers)
		if (numbers < 0):
			print("Negative numbers are illegal!")
	except TypeError:
		print("Second argument must be a positive integer value!")
	except:
		print("Something somewhere went terribly wrong!")

	f = open(filename, "w")

	for i in range(numbers):
		f.write(str(randint(0, 1000)))
		f.write(" ")

	f.close()


def main():
	try:
		generate_numbers(sys.argv[1], sys.argv[2])
	except IndexError as e:
		print("Too few arguments!")

if __name__ == "__main__":
	main()