# Zhyldyz Torogulova
# 11/5/2025
# Write a Python function to multiply all the numbers in a list. Use list [5, 2, 7,1]
list = [5, 4, 3, 2, 1]
def multiply_list(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result


print(multiply_list(list))
