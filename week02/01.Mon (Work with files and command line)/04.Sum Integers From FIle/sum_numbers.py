#Sum integers from file
import sys

def sum_of_integers(filename):
	try:
		f = open(filename, "r")
	except FileNotFoundError:
		print("File not found.")

	ftext = f.read()
	f.close()
	li = ftext.strip().split(" ");
	summ = 0

	for i in range(len(li)):
		try:
			summ += int(li[i])
		except TypeError:
			print("Type conversion failed along the way! Check file contents for non-numeric data.")
		except BaseException:
			print("This happened:", e)

	print(summ)

def main():
	try:
		sum_of_integers(sys.argv[1])
	except IndexError:
		print("No argument was provided.")
	except BaseException as e:
		print("This happened:", e)

if __name__ == "__main__":
	main()