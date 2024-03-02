# Assignment05 on OOP by Benjamin Saterbak

class BasicMathOperations:

    def __init__(self):
        pass

    def greetUser(self,firstName,lastName):
        print("Welcome to Basic Math Operations, "+str(firstName),str(lastName))

    def addNumbers(self,num1,num2):
        sum = num1 + num2
        print("The Sum is: "+str(sum))

    def performOperator(self,num1,num2,operator):
        outputVal = None
        if operator == "+":
            outputVal = num1 + num2
        elif operator == "-":
            outputVal = num1 - num2
        elif operator == "*":
            outputVal = num1 * num2
        elif operator == "/":
            outputVal = num1 / num2
        else:
            print("Please enter a valid operator (+,-,*,/)")
        print(outputVal)

    def squareNumber(self,num):
        outputVal = num**2
        print(str(num),"Squared is:",str(outputVal))

    def factorial(self,num):
        outputVal = 1
        for i in range(num,0,-1):
            outputVal *= i
        print("The Factorial of",str(num),"is:",str(outputVal))

    def countBetween(self,num1,num2):
        print("The Sequence of numbers between",str(num1),"and",str(num2),"is:")
        for i in range(num1,num2+1):
            print(i)

    def calculateSquare(self,num):
        square = num**2
        return square
    
    def calculateHypotenuse(self,num1,num2):
        num1Sqr = Calc.calculateSquare(num1)
        num2Sqr = Calc.calculateSquare(num2)
        hypotenuse = ((num1Sqr)+(num2Sqr))**(1/2)
        print("The Hypotenuse of a triangle with sides",str(num1),"and",str(num2),"is:",hypotenuse)
        
    def rectangleArea(self,num1,num2):
        area = num1*num2
        print("The Area of a Square with Sides",str(num1),"and",str(num2),"is:",str(area))

Calc = BasicMathOperations()

# Calc.greetUser("Benjamin","Saterbak")

# Calc.addNumbers(4,7)

# Calc.performOperator(9,3,"/")

# Calc.squareNumber(8)

# Calc.factorial(5)

# Calc.countBetween(4,14)

# print(Calc.calculateSquare(4))

# Calc.calculateHypotenuse(5,12)

Calc.rectangleArea(4,7)