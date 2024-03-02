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


Calc = BasicMathOperations()

# Calc.greetUser("Benjamin","Saterbak")

# Calc.addNumbers(4,7)

Calc.performOperator(9,3,"/")
