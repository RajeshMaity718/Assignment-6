# Task 1: Safe Division Utility

try:
    # Taking input
    num = float(input("Enter numerator: "))
    den = float(input("Enter denominator: "))

    # Division
    result = num / den

except ValueError:
    print("Error: Please enter valid numbers.")

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

else:
    print("Result:", result)

finally:
    print("Operation Complete")

# Task 2: Bill Calculator

prices = [120, 350, 'abc', 500, -200, 800]

total = 0

for item in prices:
    try:
        if not isinstance(item, (int, float)):
            raise TypeError

        if item < 0:
            raise ValueError("Negative price not allowed")

        total += item

    except TypeError:
        print("Invalid item (not a number):", item)

    except ValueError as e:
        print("Error:", e)


 # Task 3: Age Validator

def check_age(age):
    if age < 1 or age > 120:
        raise ValueError("Age must be between 1 and 120")
    return True

try:
    age = int(input("Enter age: "))
    check_age(age)
    print("Valid age")

except ValueError as e:
    print("Error:", e)


# Task 4: File Reader

filename = input("Enter file name: ")

try:
    file = open(filename, "r")

    print("\nFirst 3 lines:")
    for i in range(3):
        print(file.readline().strip())

    file.close()

except FileNotFoundError:
    print("File not found.")

except PermissionError:
    print("Permission denied.")

finally:
    print("File operation attempted.")

# Task 5: Safe Shopping Cart

cart = []

while True:
    user_input = input("Enter price (or 'q' to quit): ")

    if user_input == 'q':
        break

    try:
        price = float(user_input)

        if price < 0:
            raise ValueError("Price cannot be negative")

        cart.append(price)

    except ValueError as e:
        print("Error:", e)

# Final output
print("\nTotal items:", len(cart))
print("Total bill:", sum(cart))




print("Total Bill:", total)
