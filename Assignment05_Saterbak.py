# Assignment05 on OOP by Benjamin Saterbak

class BasicMathOperations:

    def __init__(self):
        pass

    def greetUser(self,firstName,lastName):
        print("Welcome to Basic Math Operations, "+str(firstName),str(lastName))

    def addNumbers(self,num1,num2):
        sum = num1 + num2
        print("The Sum is: "+str(sum))




Calc = BasicMathOperations()

# Calc.greetUser("Benjamin","Saterbak")

Calc.addNumbers(4,7)


