import unittest
from cash_desk import (Bill, BatchBill, CashDesk)

class test_Bill(unittest.TestCase):
    
    def test_init_dunder(self):
        e = None

        try:
            bill = Bill(10)
        except Exception as exc:
            e = exc

        self.assertIsNone(e)
        self.assertEqual(10, getattr(bill, "_Bill__amount"))

    def test_init_dunder_with_bad_type(self):
        e = None

        try:
            Bill("stringiboi")
        except Exception as exc:
            e = exc

        self.assertIsNotNone(e)
        self.assertEqual(str(e), "A non-integer bill.")

    def test_init_dunder_with_bad_integer_value(self):
        e1 = None
        e2 = None

        try:
            Bill(-10)
        except Exception as exc:
            e1 = exc

        try: 
            Bill(0)
        except Exception as exc:
            e2 = exc

        self.assertIsNotNone(e1)
        self.assertEqual(str(e1), "Negative or zero bill.")

        self.assertIsNotNone(e2)
        self.assertEqual(str(e2), "Negative or zero bill.")

    def test_eq_dunder(self):
        self.assertNotEqual(Bill(10), Bill(1))
        self.assertEqual(Bill(25), Bill(25))

    def test_lt_dunder(self):
        self.assertFalse(Bill(10) < Bill(1))
        self.assertFalse(Bill(25) < Bill(25))
        self.assertTrue(Bill(1) < Bill(2))

    def test_hash_dunder(self):
        e = None
        bill1 = Bill(1)
        bill2 = Bill(1)
        di = dict()

        try:
            di[bill1] = 1
            di[bill2] = 2
        except Exception as exc:
            e = exc

        self.assertIsNone(e)
        self.assertEqual(1, len(di))
        self.assertNotEqual(2, len(di))
        self.assertEqual(di[bill1], 2)

    def test_hash_dunder_with_mutation(self):
        e = None
        bill1 = Bill(1)
        bill2 = Bill(2)
        di = dict()

        try:
            di[bill1] = 1
            di[bill2] = 2
            setattr(bill2, "__amount", 1)
        except AttributeError as exc:
            e = exc
        
        self.assertIsNotNone(e)
        self.assertEqual(str(e), "Can't change bill amount!")
        self.assertEqual(di[bill1], 1)
        self.assertEqual(di[bill2], 2)

class test_BatchBill(unittest.TestCase):

    def test_init_dunder(self):
        e = None
        bill5 = Bill(5)
        bill10 = Bill(10)

        try:
            batch1 = BatchBill([bill5, bill10])
            batch2 = BatchBill([bill5])
        except Exception as exc:
            e = exc

        self.assertIsNone(e)
        self.assertEqual(bill5, batch1.__dict__["bills"][0])
        self.assertEqual(bill10, batch1.__dict__["bills"][1])
        self.assertEqual(bill5, batch2.__dict__["bills"][0])

    def test_init_dunder_with_non_list(self):
        e = None

        try:
            BatchBill({})
        except TypeError as exc:
            e = exc

        self.assertIsNotNone(e)
        self.assertEqual(str(e), "Type is not list.")

    def test_init_dunder_with_list_of_non_bills(self):
        e = None

        try:
            BatchBill([Bill(5), Bill(10), "stringiboi", Bill(15)])
        except TypeError as exc:
            e = exc

        self.assertIsNotNone(e)
        self.assertEqual(str(e), "Non-bill bill.")

    def test_len_dunder(self):
        e = None

        try:
            billList = [Bill(value) for value in range(1,5)]
            batch = BatchBill(billList)
            res = len(batch)
        except Exception as exc:
            e = exc

        self.assertIsNone(e)
        self.assertEqual(4, res)

    def test_getitem_dunder(self):
        e = None
        billList = [Bill(i) for i in range(1,5)]
        batch = BatchBill(billList)
        res = []
        expected = [Bill(1), Bill(2), Bill(3), Bill(4)]

        try:
            for item in batch:
                res.append(item)
        except Exception as exc:
            e = exc

        self.assertIsNone(e)
        self.assertEqual(expected, res)

    def test_eq_dunder(self):
        e = None
        val1 = [1, 2, 3]
        val2 = [3, 2, 1]
        val3 = [1, 3, 5]
        bills1 = [Bill(val) for val in val1]
        bills2 = [Bill(val) for val in val2]
        bills3 = [Bill(val) for val in val3]
        batch1 = BatchBill(bills1)
        batch2 = BatchBill(bills2)
        batch3 = BatchBill(bills3)

        self.assertTrue(batch1 == batch2, "Unexpectedly, Batch1 != Batch2")
        self.assertFalse(batch2 == batch3, "Unexpectedly, Batch2 == Batch3")
        self.assertFalse(batch1 == batch3, "Unexpectedly, Batch1 == Batch3")

    def test_total(self):
        e = None

        try:
            billList = [Bill(value) for value in range(1,5)]
            batch = BatchBill(billList)
            res = batch.total()
        except Exception as exc:
            e = exc

        print(res)
        self.assertIsNone(e)
        self.assertEqual(10, res)

class test_CashDesk(unittest.TestCase):
    
    def test_init_dunder(self):
        e = None

        try:
            desk = CashDesk()
        except Exception as exc:
            e = exc

        self.assertIsNone(e)

    def test_take_money_with_bad_type(self):
        e = None
        bad = dict()
        desk = CashDesk()

        try:
            desk.take_money(bad)
        except TypeError as exc:
            e = exc

        self.assertIsNotNone(e)
        self.assertEqual(str(e), "Non-bill type.")

    def test_take_money_with_bad_bill_type(self):
        e = None
        badBills = [Bill(1), Bill(2), 3]
        desk = CashDesk()

        try:
            desk.take_money(badBills)
        except TypeError as exc:
            e = exc 

        self.assertIsNotNone(e)
        self.assertEqual(str(e), "Non-bill type.")

    def test_take_money(self):
        e = None
        values = [10, 20, 50, 100, 100, 100]
        bills = [Bill(value) for value in values]
        batch = BatchBill(bills)
        extraBill = Bill(10)
        desk = CashDesk()
        expected = [BatchBill(bills), Bill(10)]
        
        try:
            desk.take_money(batch)
            desk.take_money(extraBill)
        except Exception as exc:
            e = exc

        self.assertIsNone(e)
        self.assertEqual(expected, desk.__dict__["money"])

    def test_total(self):
        e = None
        values = [10, 20, 50, 100, 100, 100]
        bills = [Bill(value) for value in values]
        batch = BatchBill(bills)
        desk = CashDesk()
        desk.take_money(batch)
        
        try:
            res = desk.total()
        except Exception as exc:
            e = exc

        self.assertIsNone(e)
        self.assertEqual(380, res)

    def test_str_inspect(self):
        e = None
        values = [10, 20, 50, 100, 100, 100]
        bills = [Bill(value) for value in values]
        batch = BatchBill(bills)
        extraBill1 = Bill(10)
        extraBill2 = Bill(500)
        desk = CashDesk()
        desk.take_money(batch)
        desk.take_money(extraBill1)
        desk.take_money(extraBill2)
        expected = "We have a total of 890$ in the desk\nWe have the following count of bills, sorted in ascending order:\n10$ bills: 2\n20$ bills: 1\n50$ bills: 1\n100$ bills: 3\n500$ bills: 1"

        try:
            res = desk.str_inspect()
        except Exception as exc:
            e = exc

        self.assertIsNone(e)
        self.assertEqual(expected, res)

if __name__ == '__main__':
    unittest.main()