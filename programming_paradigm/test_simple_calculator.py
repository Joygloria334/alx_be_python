import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase)
 def setup(self)
  self.calc = SimpleCalculator()
 def test_addition(self):
    self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-1, -1), -2)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(100, -50), 50)

    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(-1, 1), -2)
        self.assertEqual(self.calc.subtract(-1, -1), 0)
        self.assertEqual(self.calc.subtract(0, 0), 0)
        self.assertEqual(self.calc.subtract(10, -5), 15)

    def test_multiplication(self):
        """Test the multiplication method."""
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-1, 1), -1)
        self.assertEqual(self.calc.multiply(-2, -3), 6)
        self.assertEqual(self.calc.multiply(0, 5), 0)
        self.assertEqual(self.calc.multiply(10, 0), 0)
        self.assertEqual(self.calc.multiply(1, 1), 1)

    def test_division(self):
        """Test the division method."""
        # Normal division cases
        self.assertEqual(self.calc.divide(6, 3), 2.0)
        self.assertEqual(self.calc.divide(-6, 3), -2.0)
        self.assertEqual(self.calc.divide(-6, -3), 2.0)
        self.assertEqual(self.calc.divide(0, 5), 0.0)
        self.assertEqual(self.calc.divide(7, 2), 3.5)
        
        # Division by zero case
        self.assertIsNone(self.calc.divide(5, 0))
        self.assertIsNone(self.calc.divide(-5, 0))
        self.assertIsNone(self.calc.divide(0, 0))

if __name__ == "__main__":
    unittest.main()
