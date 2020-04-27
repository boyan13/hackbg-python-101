import unittest
from my_sort import my_sort

class test_my_sort(unittest.TestCase):
	def test_with_passed_noniterable_arg_raise_bad_type_exception(self):
		#ARRANGE
		e = None
		object_to_sort = {}

		#ACT
		try:
			result = my_sort(object_to_sort)
		except Exception as err:
			e = err

		#ASSERT
		self.assertIsNotNone(e) #Something was caught
		self.assertEqual(str(e),"Type must be a list or a tuple!")

	def test_with_passed_empty_iterable_return_it(self):
		#ARRANGE
		e = None
		object_to_sort = []

		#ACT
		try:
			result = my_sort(object_to_sort)
		except Exception as err:
			e = err

		#ASSERT
		self.assertIsNone(e) #Nothing was caught
		self.assertEqual([], result)

	def test_with_passed_list_return_it_sorted(self):
		#ARRANGE
		e = None
		object_to_sort = [17, 'G',  3, "FREEMAN", "Gordon"]

		expected = [3, 17, "FREEMAN", 'G', "Gordon"]

		#ACT
		try:
			result = my_sort(object_to_sort)
		except Exception as err:
			e = err

		#ASSERT
		self.assertIsNone(e) #Nothing was caught
		self.assertEqual(expected, result)

	def test_with_passed_tuple_return_it_sorted(self):
		#ARRANGE
		e = None
		object_to_sort = (17, 'G',  3, "FREEMAN", "Gordon")

		expected = (3, 17, "FREEMAN", 'G', "Gordon")

		#ACT
		try:
			result = my_sort(object_to_sort)
		except Exception as err:
			e = err

		#ASSERT
		self.assertIsNone(e) #Nothing was caught
		self.assertEqual(expected, result)

	def test_descending_rule_returns_reversed_sort(self):
		#ARRANGE
		e = None
		object_to_sort = [17, 'G',  3, "FREEMAN", "Gordon"]
		descending = False

		expected = ["Gordon", 'G', "FREEMAN", 17, 3]

		#ACT
		try:
			result = my_sort(object_to_sort, descending)
		except Exception as err:
			e = err

		#ASSERT
		self.assertIsNone(e) #Nothing was caught
		self.assertEqual(expected, result)


	def test_with_passed_listdict_and_key_return_it_sorted(self):
		#ARRANGE
		e = None
		object_to_sort = [
			{"name" :    "God", "age" : "immortal"}, 
			{"name" :   "Gman", "age" : "unknown"},
			{"name" : "Gordon", "age" : 27},
			{"name" :  "Jimmy", "age" : 20}
		]
		key = "age"

		expected = [
			{"name" :  "Jimmy", "age" : 20},
			{"name" : "Gordon", "age" : 27},
			{"name" :    "God", "age" : "immortal"}, 
			{"name" :   "Gman", "age" : "unknown"}
		]
		#ACT
		try:
			result = my_sort(iterable=object_to_sort, key=key)
		except Exception as err:
			e = err

		#ASSERT
		self.assertIsNone(e) #Nothing was caught
		self.assertEqual(expected, result)

	def test_with_passed_dict_without_key_raise_no_key_exception(self):
		#ARRANGE
		e = None
		object_to_sort = [
			{"name" :  "God", "age" : "immortal"}, 
			{"name" :  "Jimmy", "age" : 20}
		]

		#ACT
		try:
			result = my_sort(object_to_sort)
		except Exception as err:
			e = err

		#ASSERT
		self.assertIsNotNone(e) #Something was caught
		self.assertEqual(str(e), "Must provide a key when passing a list dictionary!")

	def test_with_passed_list_dictionary_with_other_types_raise_mixed_types_exception(self):
		#ARRANGE
		e = None
		object_to_sort = [
			{"name" :  "God", "age" : "immortal"}, 
			{"name" :  "Jimmy", "age" : 20},
			120,
			"car"
		]

		#ACT
		try:
			result = my_sort(object_to_sort)
		except Exception as err:
			e = err

		#ASSERT
		self.assertIsNotNone(e) #Something was caught
		self.assertEqual(str(e), "List dictionary contains non-dictionary types!")

	def test_with_passed_bogus_key_raise_bogus_key_exception(self):
		#ARRANGE
		e = None
		object_to_sort = [
			{"name" :    "God", "age" : "immortal"}, 
			{"name" :   "Gman", "age" : "unknown"},
			{"name" : "Gordon", "age" : 27},
			{"name" :  "Jimmy", "age" : 20}
		]
		key = "problematic"

		#ACT
		try:
			result = my_sort(iterable=object_to_sort, key=key)
		except Exception as err:
			e = err

		#ASSERT
		self.assertIsNotNone(e) #Something was caught
		self.assertEqual(str(e), "A list dictionary member is missing passed key!")

if __name__ == '__main__':
	unittest.main()