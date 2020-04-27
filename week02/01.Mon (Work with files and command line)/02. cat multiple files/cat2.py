#Cat multiple files
import sys

def cat2(arguments):
	for arg in range(len(arguments)):
		print('\n')
		try:
			with open(arguments[arg], "r") as f:
				text = f.read()
				print(text)
		except FileNotFoundError:
			print("File not found!")
		except:
			print("Error opening file!")

def main():
	li = []

	for arg in range(1, len(sys.argv)):
		li.append(sys.argv[arg])
		
	cat2(li)


if __name__ == "__main__":
	main()