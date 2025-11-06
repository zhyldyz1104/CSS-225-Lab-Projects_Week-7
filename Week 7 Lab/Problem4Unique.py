# Zhyldyz Torogulova
# 11/5/2025
# Write a Python function that takes a list of numbers and returns a new list with
# unique elements of the first list. Use list [1, 3, 3, 3, 6, 2, 3, 5]. Use the append
# function.

original_list = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6]


def append_number(list):
    new_list = []
    for num in list:
        if num not in new_list:
            new_list.append(num)
    return new_list


print(append_number(original_list))
