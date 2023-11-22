import unittest


class SampleTestNG(unittest.TestCase):
	def test_case_1(self):
		print('Executing the first test case ')
		self.assertEquals(5 + 6, 11)
	
	def test_case_2(self):
		print('Executing the second test case ')
		self.assertEquals('Hanu', 'Hanu')
