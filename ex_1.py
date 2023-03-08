import math

def ex1():                                             #Calculate the area of a circle
    radius = input("Input radius:")
    area = float(math.pi * int(radius) ** 2)
    print(area)


def ex2():                                             #Calculate the factorial of a number
    number = input("Input Number:")
    number = int(number)
    for i in range (1,number):
        number = number * i
    print(number)


def ex3():                                             #Find the maximum of three numbers
    number1 = int(input("Input first number:"))
    number2 = int(input("Input second number:"))
    number3 = int(input("Input third number:"))
    print(max(number1,number2,number3))


def ex4():                                             #Check if a number is prime or not
    number = int(input("Input number:"))
    if number <= 1:
        print("Number is not prime")
        return
    for i in range(2, int(number ** (1 / 2)) + 1):
        if number % i == 0:
            print("Number is not prime")
            return
    print("Number is prime")


def ex5():                                             #Print the Fibonacci sequence
    firstNumber = 0
    secondNumber = 1
    nr = int(input("Input number:"))
    while secondNumber < nr:
        print(secondNumber, ' ')
        x = firstNumber
        firstNumber = secondNumber
        secondNumber = secondNumber + x
