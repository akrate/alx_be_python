import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()
    def test_addition(self):
        self.assertEqual(self.calc.add(5,4),9)
        self.assertEqual(self.calc.add(1,2),3)
        self.assertEqual(self.calc.add(0,8),8)
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(1,1),0)
        self.assertEqual(self.calc.subtract(2,3),-1)
        self.assertEqual(self.calc.subtract(3,2),1)
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(1,1),1)
        self.assertEqual(self.calc.multiply(0,7),0)
        self.assertEqual(self.calc.multiply(5,5),25)
    def test_divide(self):
        self.assertEqual(self.calc.divide(25,5),5)
        self.assertEqual(self.calc.divide(9,3),3)
        self.assertEqual(self.calc.divide(8,2),4)
if __name__ == "__main__":
    unittest.main()
