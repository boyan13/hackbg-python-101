import sys
from polynomial import Polynomial, PolyTerm

def main():
	parsed = PolyTerm.parse(sys.argv[1])
	terms = []

	for term in parsed:
		terms.append(PolyTerm(term))

	p = Polynomial(terms)
	derivative = p.derivative()

	print(derivative)


if __name__ == '__main__':
	main()