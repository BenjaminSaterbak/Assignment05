# Assignment05 on OOP by Benjamin Saterbak

class BasicMathOperations:

    def __init__(self):
        pass

    def greetUser(self,firstName,lastName):
        print("Welcome to Benjamin's Python Calculator, "+str(firstName),str(lastName))

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
        print(str(num1)+str(operator)+str(num2),"=",str(outputVal))

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
        num1Sqr = self.calculateSquare(num1)
        num2Sqr = self.calculateSquare(num2)
        hypotenuse = ((num1Sqr)+(num2Sqr))**(1/2)
        print("The Hypotenuse of a triangle with sides",str(num1),"and",str(num2),"is:",hypotenuse)
        
    def rectangleArea(self,num1,num2):
        area = num1*num2
        print("The Area of a Square with Sides",str(num1),"and",str(num2),"is:",str(area))

    def numberPower(self,num1,num2):
        power = num1**num2
        print(str(num1)+"^"+str(num2),"=",str(power))

    def getType(self,variable):
        return type(variable)


def main():
    Calc = BasicMathOperations()
    while True:
        print("""
Benjamin's Python Calculor
---------------------------
Please Select an Option Below (1-10)
1) User Greeting
2) Add Two Numbers
3) Operator Calculations with Two Numbers
4) Square a Number
5) Find the Factorial of a Number
6) Counting between Two Values
7) Hypotenuse Calculator
8) Rectangle Area Calculator
9) Number Power Calculator
10) Get Data Type
---------------------------""")
        try:
            userChoice = int(input("Selection?: "))
            if (userChoice > 0) and (userChoice < 11):
                break
        except ValueError:
            print("Invalid Input. Please enter an integer 1-10.")
    print("---------------------------")
    if userChoice == 1:
        firstName = input("Please input your first name: ")
        lastName = input("Please input your last name: ")
        Calc.greetUser(firstName,lastName)

    elif userChoice == 2:
        while True:
        # Error code from: https://pieriantraining.com/python-tutorial-how-to-take-an-integer-input-in-python/#:~:text=In%20Python%2C%20we%20can%20take%20user%20input%20using%20the%20%60input,returns%20it%20as%20a%20string.&text=In%20the%20code%20above%2C%20we,input()%60%20into%20an%20integer.
            try:
                num1 = int(input("Please input your first number: "))
                num2 = int(input("Please enter your second number: "))
                break
            except ValueError:
                print("Invalid input. Please enter integers")
        
        Calc.addNumbers(num1,num2)

    elif userChoice == 3:
        while True:
            try:
                num1 = int(input("Please input your first number: "))
                operator = str(input("Please enter an operator (+,-,*,/): "))
                num2 = int(input("Please enter your second number: "))
                
                if num2 == 0 and operator == "/":
                    print("Cannot divide by zero")
                elif operator == "+" or "-" or "*" or "/":
                    break
            except ValueError:
                print("Invalid input. Please enter integers and a valid operator (+,-,*,/)")

        Calc.performOperator(num1,num2,operator)

    elif userChoice == 4:
        while True:
            try:
                num1 = int(input("Please input a number: "))
                break
            except ValueError:
                print("Invalid input. Please enter integers")
        
        Calc.squareNumber(num1)

    elif userChoice == 5:
        while True:
            try:
                num1 = int(input("Please input a positive number: "))
                if num1 >= 0:
                    break
                else:
                    print("Invalid input. Please enter a positive number.")
            except ValueError:
                print("Invalid input. Please enter integers")
        
        Calc.factorial(num1)

    elif userChoice == 6:
        while True:
            try:
                num1 = int(input("Please input your first number: "))
                num2 = int(input("Please enter your second number: "))
                break
            except ValueError:
                print("Invalid input. Please enter integers")
        if num1 < num2:
            pass
        else:
            num2,num1=num1,num2
        Calc.countBetween(num1,num2)

    elif userChoice == 7:
        while True:
            try:
                num1 = int(input("Please input your first positive number: "))
                num2 = int(input("Please enter your second positive number: "))
                if (num1 and num2) > 0:
                    break
                else:
                    print("Invalid input. Please enter positive integers")
            except ValueError:
                print("Invalid input. Please enter integers")
        
        Calc.calculateHypotenuse(num1,num2)

    elif userChoice == 8:
        while True:
            try:
                num1 = int(input("Please input your first number: "))
                num2 = int(input("Please enter your second number: "))
                if (num1 and num2) > 0:
                    break
                else:
                    print("Invalid input. Please enter positive integers")
            except ValueError:
                print("Invalid input. Please enter integers")
        
        Calc.rectangleArea(num1,num2)

    elif userChoice == 9:
        while True:
            try:
                num1 = int(input("Please input your first number: "))
                num2 = int(input("Please enter your second number: "))
                break
            except ValueError:
                print("Invalid input. Please enter integers")
        
        Calc.numberPower(num1,num2)

    elif userChoice == 10:
        value = input("Please enter your data: ")
        print("Your data type is: "+str(Calc.getType(value)))



# Calc.greetUser("Benjamin","Saterbak")

# Calc.addNumbers(4,7)

# Calc.performOperator(9,3,"/")

# Calc.squareNumber(8)

# Calc.factorial(5)

# Calc.countBetween(4,14)

# print(Calc.calculateSquare(4))

# Calc.calculateHypotenuse(5,12)

# Calc.rectangleArea(4,7)

# Calc.numberPower(2,4)

# print(Calc.getType([1,4,5]))
        

main()