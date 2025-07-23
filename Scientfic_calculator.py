import math

def add(x,y):
    return x+y 
    
    
def subtract(x,y):
    return x-y
    
def multiply(x,y):
   return x*y
def divide(x,y):
    if y == 0:
        return "Error! cannot divide be zero"
    return x/y
def modular(x,y):
     return x%y
def square(x):
    return x **2
def cube (x):
   return x ** 3
def power (x,y):
   return x^ y
def square_root(x):
   return math.sqrt(x)
    
    
def show_menu():
    print("\n---*Calculator app menu*---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modular")
    print("6. Square")
    print("7. Cube")
    print("8. Power")
    print("9. Square root")
    print("10. Exit")
    
def calculator():
    while True:
        show_menu()
        choice = input("Enter your choice(1-10):")
        if choice == "5": 
          print("Exiting Calculator Goodbye :)")
          break
      
        num1 = float(input("Enter first number:"))
        num2 = float(input("Enter second number:"))
      
        if choice =="1":
          print("Result:", add(num1,num2))
        elif choice == "2":
          print("Result:", subtract(num1,num2))
        elif choice =="3":
          print("Result:", multiply(num1,num2))
        elif choice == "4":
          print("Result:", divide(num1,num2))
        elif choice == "5":
           print("Result:", modular(num1,num2))
        elif choice == "6":
           print("Result:", square(num1))
        elif choice == "7":
           print("Result:", cube(num1))
        elif choice == "8":
           print("Result:" , power(num1,num2))
        elif choice== "9":
           print("Result:", square_root(num1))
        else:
          print("Invalid input! Please choose from 1-10")
calculator()