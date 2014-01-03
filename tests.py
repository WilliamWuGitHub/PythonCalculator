__author__ = 'William T Ng'
#__name__ = '__main__'
import unittest
from basiccalc import Calculator


class Test(unittest.TestCase):
    # A list holding pairs

    def setUp(self):
        self.calculator = Calculator()

    @unittest.skip("Not testing yet.")
    def testRepeatedOperations(self):
        inputCases = [1, 2, 43, 54, 42, 1]  # The input classes
        # Enter an expression with more than two terms
        self.calculator.modifyDisplay(inputCases[0])
        self.calculator.add()
        self.calculator.modifyDisplay(inputCases[1])
        self.calculator.add()
        self.calculator.modifyDisplay(inputCases[2])
        self.calculator.divide()
        self.calculator.modifyDisplay(inputCases[3])
        self.calculator.multiply()
        self.calculator.modifyDisplay(inputCases[4])
        self.calculator.subtact()
        self.calculator.modifyDisplay(inputCases[5])
        self.calculator.add()
        self.calculator.modifyDisplay(inputCases[6])


        self.assertEquals(self.calculator.result == 10)

    def testOperations(self):

        inputCases = [(13, 132), (-12, 2), (12, -2), (1, 0), (0, 1)]  # The input classes

        for i in inputCases:
            # Test addition
            self.calculator.modifyDisplay(i[0])
            self.calculator.add()
            self.calculator.modifyDisplay(i[1])
            self.calculator.calculate()
            self.assertEqual(self.calculator.result, i[0]+i[1])
            # Test subtraction
            self.calculator.modifyDisplay(i[0])
            self.calculator.subtract()
            self.calculator.modifyDisplay(i[1])
            self.calculator.calculate()
            self.assertEqual(self.calculator.result,i[0]-i[1])
            # Test multiplication
            self.calculator.modifyDisplay(i[0])
            self.calculator.multiply()
            self.calculator.modifyDisplay(i[1])
            self.calculator.calculate()
            self.assertEqual(self.calculator.result, i[0]*i[1])
            # Test division
            self.calculator.modifyDisplay(i[0])
            self.calculator.divide()
            self.calculator.modifyDisplay(i[1])
            self.calculator.calculate()
            self.assertEqual(self.calculator.result, i[0]/i[1])


if __name__ == '__main__':
    unittest.main()