# Zhyldyz Torogulova
# 11/5/2025
# Write a Python function to check whether a number is in a given range. Use
# range(1,10). Print whether the number is in or not in the range

def checkRange(num):
    if num in range(1, 10):
        print(f"{num} is in the range.")
    else:
        print(f"{num} is NOT in the range.")
