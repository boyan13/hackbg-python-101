#simplify_fraction

from math import gcd

#we want a tuple with no more than 2 integers
def validate_simplify_fraction_arguments(fraction = None):
	if fraction is None:
		return True

	if type(fraction) is not tuple:
		raise Exception("Argument must be of type tuple.")

	if len(fraction) > 2:
		raise Exception("Fraction contains more than 2 members.")

	for member in fraction:
		if type(member) is not int:
			raise Exception("Non-integer member in fraction.")

	return True


def simplify_fraction(fraction = None):
	try:
		validate_simplify_fraction_arguments(fraction)
	except Exception as exc:
		raise Exception(str(exc))


	if fraction is None or fraction == tuple():
		return (0,)

	if len(fraction) == 1:
		return fraction

	numerator, denominator = fraction

	if numerator == 0:
		return (0,)

	if denominator == 0:
		raise Exception("Zero division!")

	if numerator == denominator:
		return (1,1)

	if numerator < denominator:
		buf = numerator
	else:
		buf = denominator

	if (numerator / buf) % 1 == 0 and (denominator / buf) % 1 == 0:
		numerator //= buf
		denominator //= buf
		return (numerator, denominator) 
	
	buf = gcd(numerator, denominator)
	while (buf != 1):
		numerator //= buf
		denominator //= buf
		buf = gcd(numerator, denominator)

	return (numerator, denominator) 

def main():
	pass

if __name__ == '__main__':
	main()