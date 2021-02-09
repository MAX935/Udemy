import unittest
import upper

class Testing:
	def upper_test_func(self):
		test_string = 'hello'
		result = upper.upper_text(test_string)
		self.isEqual(result, '12312')


if __name__ == '__main__':
    unittest.main()
