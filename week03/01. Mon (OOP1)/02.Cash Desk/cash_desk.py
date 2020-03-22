#Cash Desk

class Bill:
	
	#DUNDERS
	def __init__ (self, amount):
		if type(amount) is not int:
			raise TypeError("A non-integer bill.")

		if amount <= 0:
			raise ValueError("Negative or zero bill.")

		self.__amount = amount

	def __str__ (self):
		return f"A {self.__amount}$ bill."

	def __repr__ (self):
		return f"Bill amount={self.__amount}"

	def __eq__ (self, other):
		return self.__amount == other.__amount

	def __lt__ (self, other):
		return self.__amount < other.__amount

	def __hash__ (self):
		return hash(self.__amount)

	def __setattr__ (self, name, value):
		if name is "__amount":
			raise AttributeError("Can't change bill amount!")

		self.__dict__[name] = value

	#METHODS
	def _get_val(self):
		return self.__amount


class BatchBill:
	
	#DUNDERS
	def __init__ (self, bills):
		if type(bills) is not list:
			raise TypeError("Type is not list.")

		for bill in bills:
			if type(bill) is not Bill:
				raise TypeError("Non-bill bill.")

		self.bills = bills

	def __len__ (self):
		return len(self.bills)

	def __getitem__ (self, index):
		return self.bills[index]

	def __eq__ (self, other):
		return self.total() == other.total()

	#METHODS
	def total(self):
		total = 0

		for bill in self.bills:
			total += bill._get_val()

		return total

class CashDesk:
	
	#DUNDERS
	def __init__ (self):
		self.money = []

	#METHODS
	def take_money(self, money):
		if type(money) is not Bill and type(money) is not BatchBill:
			raise TypeError("Non-bill type.")

		self.money.append(money)

	def total(self):
		total = 0

		for item in self.money:
			if type(item) is Bill:
				total += item._get_val()
			elif type(item) is BatchBill:
				total += item.total()
			else:
				raise TypeError("Corruption in CashDesk contents!")

		return total

	def inspect(self):
		print(f"We have a total of {self.total()}$ in the desk")
		print("We have the following count of bills, sorted in ascending order:")
		
		counter = {}

		for item in self.money:
			if type(item) is Bill:
				if item not in counter.keys():
					counter[item] = 1
				else:
					counter[item] += 1

			else:
				for bill in item:
					if bill not in counter.keys():
						counter[bill] = 1
					else:
						counter[bill] += 1

		for bill in sorted(counter):
			print(f"{bill._get_val()}$ bills:", counter[bill])

	def str_inspect(self):
		result = f"We have a total of {self.total()}$ in the desk\n"
		result += "We have the following count of bills, sorted in ascending order:\n"

		counter = {}

		for item in self.money:
			if type(item) is Bill:
				if item not in counter.keys():
					counter[item] = 1
				else:
					counter[item] += 1

			else:
				for bill in item:
					if bill not in counter.keys():
						counter[bill] = 1
					else:
						counter[bill] += 1

		for bill in sorted(counter):
			result += (f"{bill._get_val()}$ bills: " + str(counter[bill])) + '\n'

		result = result[:-1] #delete the last '\n' char
		return result

def main():
	pass

if __name__ == '__main__':
	main()