# 1. Define the 4 required functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def main():
    try:
        #3. Use float(input()) to read numbers from the user
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        print("\nChoose an operation:")
        print("1. Add\n2. Subtract\n3. Multiply\n4. Divide")
        choice = input("Enter choice (1/2/3/4): ")

        #Perform calculation and handle results
        if choice == '1':
            print(f"Result: {add(num1, num2)}")
        elif choice == '2':
            print(f"Result: {subtract(num1, num2)}")
        elif choice == '3':
            print(f"Result: {multiply(num1, num2)}")
        elif choice == '4':
            #2. Catch ZeroDivisionError without crashing
            try:
                print(f"Result: {divide(num1, num2)}")
            except ZeroDivisionError:
                print("Error: Cannot divide by zero.")
        else:
            print("Invalid selection.")       

    #2. Catch ValueError for invalid input
    except ValueError:
        print("Error: Invalid input. Please enter numeric values only.")  


if __name__ == "__main__":
    main()          

    