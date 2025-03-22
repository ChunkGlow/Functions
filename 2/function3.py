def add(X, Y):
    return X + Y

def subtract(X, Y):
    return X - Y

def multiply(X, Y):
    return X * Y

def divide(X, Y):
    return X / Y

def power(X, Y):
    return X ** Y

def root(X, Y):
    return X ** (1/Y)

def factorial(X):
    if X == 0:
        return 1
    else:
        return X * factorial(X-1)

print("Please Select Operation:")

print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Power")
print("6. Root")
print("7. Factorial")

choice = input("Enter Choice (1/2/3/4/5/6/7) : ")

num1 = int(input("Enter 1st Number: "))
num2 = int(input("Enter 2nd Number: "))

if choice == '1':
    print(num1, "+", num2, "=", add(num1, num2))

elif choice == '2':
    print(num1, "-", num2, "=", subtract(num1, num2))

elif choice == '3':
    print(num1, "*", num2, "=", multiply(num1, num2))

elif choice == '4':
    print(num1, "/", num2, "=", divide(num1, num2))

elif choice == '5':
    print(num1, "^", num2, "=", power(num1, num2))

elif choice == '6':
    print(num1, "root", num2, "=", root(num1, num2))

elif choice == '7':
    print(num1, "!", "=", factorial(num1))

else:
    print("Invalid Input")


add(2, 3)
subtract(2, 3)
multiply(2, 3)
divide(2, 3)
power(2, 3)
root(2, 3)
factorial(2)
