import unittest
import test_functions

class TestUpper(unittest.TestCase):

	def test_upper(self):
		text = 'test_text'
		result = test_functions.upper_text(text)
		self.asserEqual(result, 'dfsf')

if __name__ == '__main__':
    unittest.main()
