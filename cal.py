import math
import sys

# Utility functions
def clear_screen():
    print("\n" * 50)

def pause():
    input("\nPress Enter to continue...")

# Menu display
def show_main_menu():
    print("==== PYTHON CALCULATOR ====")
    print("1. Basic Operations (+, -, *, /, %)")
    print("2. Scientific Operations")
    print("3. Exit")

def show_scientific_menu():
    print("\n--- Scientific Operations ---")
    print("1. Square Root")
    print("2. Power (x^y)")
    print("3. Sine (degrees)")
    print("4. Cosine (degrees)")
    print("5. Tangent (degrees)")
    print("6. Log base 10")
    print("7. Back to Main Menu")

# Basic operations
def basic_calculator():
    try:
        num1 = float(input("Enter first number: "))
        op = input("Enter operator (+, -, *, /, %): ").strip()
        num2 = float(input("Enter second number: "))

        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        elif op == '/':
            if num2 == 0:
                print("Error: Division by zero!")
                return
            result = num1 / num2
        elif op == '%':
            if num2 == 0:
                print("Error: Division by zero!")
                return
            result = num1 % num2
        else:
            print("Invalid operator!")
            return

        print(f"Result: {result}")
    except ValueError:
        print("Invalid input!")

# Scientific operations
def scientific_calculator():
    while True:
        show_scientific_menu()
        choice = input("Choose operation: ")

        try:
            if choice == '1':
                num = float(input("Enter number: "))
                if num < 0:
                    print("Error: Cannot compute square root of negative number.")
                else:
                    print(f"Result: {math.sqrt(num)}")

            elif choice == '2':
                base = float(input("Enter base: "))
                exp = float(input("Enter exponent: "))
                print(f"Result: {math.pow(base, exp)}")

            elif choice == '3':
                angle = float(input("Enter angle in degrees: "))
                print(f"Result: {math.sin(math.radians(angle))}")

            elif choice == '4':
                angle = float(input("Enter angle in degrees: "))
                print(f"Result: {math.cos(math.radians(angle))}")

            elif choice == '5':
                angle = float(input("Enter angle in degrees: "))
                print(f"Result: {math.tan(math.radians(angle))}")

            elif choice == '6':
                num = float(input("Enter number: "))
                if num <= 0:
                    print("Error: Logarithm undefined for zero or negative.")
                else:
                    print(f"Result: {math.log10(num)}")

            elif choice == '7':
                break
            else:
                print("Invalid option.")
        except ValueError:
            print("Invalid input.")
        pause()

# Main loop
def main():
    while True:
        clear_screen()
        show_main_menu()
        choice = input("Choose an option (1-3): ")

        if choice == '1':
            basic_calculator()
        elif choice == '2':
            scientific_calculator()
        elif choice == '3':
            print("Goodbye!")
            sys.exit()
        else:
            print("Invalid choice.")

        pause()

if _name_ == "_main_":
    main()
