def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


total = multiply(2, 3, 4, 5)
print(total)
