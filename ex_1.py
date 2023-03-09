import math
import unittest
from io import StringIO
from unittest.mock import patch


def ex1():                                             #Calculate the area of a circle
    radius = input("Input radius:")
    try:
        radius = int(radius)
        if radius < 0:
            raise ValueError("Radius must be non-negative")
        area = math.pi * radius ** 2
        print(f"{area:.2f}")
    except ValueError as e:
        print(e)


def ex2():                                             #Calculate the factorial of a number
    number = input("Input Number:")
    number = int(number)
    if number < 0:
        print("Factorial is not defined for negative numbers")
        return
    elif number == 0:
        print(1)
        return
    else:
        factorial = 1
        for i in range(1, number + 1):
            factorial *= i
        print(factorial)


def ex3():                                             #Find the maximum of three numbers
    number1 = int(input("Input first number:"))
    number2 = int(input("Input second number:"))
    number3 = int(input("Input third number:"))
    print(max(number1,number2,number3))


def ex4(number):                                             #Check if a number is prime or not
    if number <= 1:
        return "Number is not prime"
    for i in range(2, int(number ** (1 / 2)) + 1):
        if number % i == 0:
            return "Number is not prime"
    return "Number is prime"


def ex5(nr):                                             #Print the Fibonacci sequence
    firstNumber = 0
    secondNumber = 1
    result = []
    while secondNumber <= nr:
        result.append(secondNumber)
        x = firstNumber
        firstNumber = secondNumber
        secondNumber = secondNumber + x
    return result

#Tests

class TestEx1(unittest.TestCase):
    def test_area_with_radius_zero(self):
        expected_output = "0.00\n"
        with patch('sys.stdout', new=StringIO()) as fake_output:
            with patch('builtins.input', return_value="0"):
                ex1()
        self.assertEqual(fake_output.getvalue(), expected_output)

    def test_area_with_radius_one(self):
        expected_output = f"{math.pi:.2f}\n"
        with patch('sys.stdout', new=StringIO()) as fake_output:
            with patch('builtins.input', return_value="1"):
                ex1()
        self.assertEqual(fake_output.getvalue(), expected_output)

    def test_area_with_large_radius(self):
        expected_output = f"{math.pi * 100 ** 2:.2f}\n"
        with patch('sys.stdout', new=StringIO()) as fake_output:
            with patch('builtins.input', return_value="100"):
                ex1()
        self.assertEqual(fake_output.getvalue(), expected_output)

    def test_area_with_negative_radius(self):
        expected_output = "Radius must be non-negative\n"
        with patch('sys.stdout', new=StringIO()) as fake_output:
            with patch('builtins.input', return_value="-5"):
                ex1()
        self.assertEqual(fake_output.getvalue(), expected_output)

    def test_area_with_noninteger_radius(self):
        expected_output = "invalid literal for int() with base 10: '5.5'\n"
        with patch('sys.stdout', new=StringIO()) as fake_output:
            with patch('builtins.input', return_value="5.5"):
                ex1()
        self.assertEqual(fake_output.getvalue(), expected_output)


class TestEx2(unittest.TestCase):
    def test_factorial_with_zero(self):
        expected_output = "1\n"
        with patch('sys.stdout', new=StringIO()) as fake_output:
            with patch('builtins.input', return_value="0"):
                ex2()
        self.assertEqual(fake_output.getvalue(), expected_output)

    def test_factorial_with_one(self):
        expected_output = "1\n"
        with patch('sys.stdout', new=StringIO()) as fake_output:
            with patch('builtins.input', return_value="1"):
                ex2()
        self.assertEqual(fake_output.getvalue(), expected_output)

    def test_factorial_with_small_number(self):
        expected_output = "120\n"
        with patch('sys.stdout', new=StringIO()) as fake_output:
            with patch('builtins.input', return_value="5"):
                ex2()
        self.assertEqual(fake_output.getvalue(), expected_output)

    def test_factorial_with_large_number(self):
        expected_output = "2432902008176640000\n"
        with patch('sys.stdout', new=StringIO()) as fake_output:
            with patch('builtins.input', return_value="20"):
                ex2()
        self.assertEqual(fake_output.getvalue(), expected_output)

    def test_factorial_with_negative_number(self):
        expected_output = "Factorial is not defined for negative numbers\n"
        with patch('sys.stdout', new=StringIO()) as fake_output:
            with patch('builtins.input', return_value="-5"):
                ex2()
        self.assertEqual(fake_output.getvalue(), expected_output)


class TestEx3(unittest.TestCase):
    def test_max_with_positive_numbers(self):
        expected_output = "10\n"
        with patch('sys.stdout', new=StringIO()) as fake_output:
            with patch('builtins.input', side_effect=[2, 10, 6]):
                ex3()
        self.assertEqual(fake_output.getvalue(), expected_output)

    def test_max_with_negative_numbers(self):
        expected_output = "-2\n"
        with patch('sys.stdout', new=StringIO()) as fake_output:
            with patch('builtins.input', side_effect=[-2, -5, -4]):
                ex3()
        self.assertEqual(fake_output.getvalue(), expected_output)

    def test_max_with_mixed_numbers(self):
        expected_output = "5\n"
        with patch('sys.stdout', new=StringIO()) as fake_output:
            with patch('builtins.input', side_effect=[-2, 5, 0]):
                ex3()
        self.assertEqual(fake_output.getvalue(), expected_output)

    def test_max_with_identical_numbers(self):
        expected_output = "10\n"
        with patch('sys.stdout', new=StringIO()) as fake_output:
            with patch('builtins.input', side_effect=[10, 10, 10]):
                ex3()
        self.assertEqual(fake_output.getvalue(), expected_output)


class TestEx4(unittest.TestCase):


    def test_prime_numbers(self):
        self.assertEqual(ex4(2), "Number is prime")
        self.assertEqual(ex4(3), "Number is prime")
        self.assertEqual(ex4(5), "Number is prime")
        self.assertEqual(ex4(7), "Number is prime")
        self.assertEqual(ex4(11), "Number is prime")
        self.assertEqual(ex4(13), "Number is prime")

    def test_non_prime_numbers(self):
        self.assertEqual(ex4(1), "Number is not prime")
        self.assertEqual(ex4(4), "Number is not prime")
        self.assertEqual(ex4(6), "Number is not prime")
        self.assertEqual(ex4(8), "Number is not prime")
        self.assertEqual(ex4(9), "Number is not prime")
        self.assertEqual(ex4(10), "Number is not prime")


class TestEx5(unittest.TestCase):
    def test_fibonacci_sequence(self):
        self.assertEqual(ex5(0), []) # empty list if nr is 0
        self.assertEqual(ex5(1), [1]) # base case for nr = 1
        self.assertEqual(ex5(2), [1, 1]) # general case for nr = 2
        self.assertEqual(ex5(8), [1, 1, 2, 3, 5, 8]) # general case for nr = 8
        self.assertEqual(ex5(13), [1, 1, 2, 3, 5, 8, 13]) # general case for nr = 13

    def test_large_number(self):
        self.assertEqual(ex5(100), [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89])

    def test_negative_number(self):
        self.assertEqual(ex5(-1), [])


if __name__ == '__main__':
    unittest.main()