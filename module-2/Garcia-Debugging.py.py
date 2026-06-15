def add_numbers(a, b):
    return a + b

def main():
    print("Simple Calculator")
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    result = add_numbers(x, y)
    print("The result is:", result)

main()