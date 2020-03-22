#Implement an alternative to du -h command
import sys
import os

def duhs(path):
	total_size = 0
	for dirpath, dirnames, filenames in os.walk(path):
		for f in filenames:
			fp = os.path.join(dirpath, f) #create path to file
			if not os.path.islink(fp):
				total_size += os.path.getsize(fp)
				total_size *= 0.001 #KB

	print("Total size:", total_size, "K bytes.")

def main():
	try:
		duhsPath = sys.argv[1]
	except BaseException:
		print("This happened:", e)

	duhs(duhsPath)

if __name__ == "__main__":
	main()
