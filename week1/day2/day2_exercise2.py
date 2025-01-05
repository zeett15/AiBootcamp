# simple calculator
def add(a, b):
    return a + b

def subtract (a, b):
    return a - b

def multiply (a, b):
    return a * b

def divide (a, b):
    if b == 0:
        print ("cannot divide by zero")
    else:
        return a / b
    
while True:
    print("\nmenu:")
    print("1. addition")
    print("2. subtraction")
    print("3. multiplication")
    print("4. division")
    print("5. exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 5:
        print("exiting program. thank you")
        break
    
    num1 = float(input("Enter frist number: "))
    num2 = float(input("Enter second number: "))
    
    if choice == 1:
        print("result: ", add (num1, num2))
    if choice == 2:
        print("result: ", subtract (num1, num2))
    if choice == 3:
        print("result: ", multiply (num1, num2))
    if choice == 4:
        print("result: ", divide (num1, num2))