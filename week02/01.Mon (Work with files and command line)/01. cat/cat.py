#implement the cat command - Print file contents
import sys

def cat(arguments):
	try:
		with open(arguments, "r") as f:
			text = f.read()
			print(text)
	except FileNotFoundError:
		print("File not found!")
	except:
		print("Error opening file!")

def main():
	try:
		cat(sys.argv[1])
	except IndexError:
		print("No argument was provided!")

if __name__ == "__main__":
	main()