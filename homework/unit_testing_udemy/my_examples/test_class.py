import unittest
import test_func

class TestStringMethods(unittest.TestCase):
	def testing(self):
		text = 'text'
		result = test_func.test_func(text)
		self.assertEqual(result, 'TeXT')

if __name__ == '__main__':
	unittest.main()
