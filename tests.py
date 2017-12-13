from  addition import sum
from  subtraction import sub
from  division import div
from  multiplication import mul


try:
    import unittest2 as unittest
except ImportError:
    import unittest

class SimpleTest(unittest.TestCase):

	def test_add(self):
		self.assertEqual(sum(7,3), 7 + 3)

	def test_sub(self):
		self.assertEqual(sub(7,3), 7-3)

	def test_mul(self):
		self.assertEqual(mul(7,3), 7*3)

	def test_div(self):
		self.assertEqual(div(7,3), 7//3)

if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(SimpleTest)
	unittest.TextTestRunner(verbosity=2).run(suite)