# A6 - Create a function that can accept a series of numbers and a mathematical
# operand. Return the result of calculating the expression. E.g.:
#    calculate(1, 2, 3, 4, operand = "multiply")
#    calculate(65, 200, 84, 12, operand = "add")

def calculator(*args, operand = "+"):
    total = args[0]
    for arg in args[1:]:
        if operand == "+":
            total += arg
        elif operand == "*":
            total *= arg

    return total


print(calculator(1, 2))
print(calculator(1, 2, 3, 4, 5, 6))
print(calculator(4, 5, operand = "*"))
