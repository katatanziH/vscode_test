import math
import os
import random

# Sum of natural numbers up to num
name = input("Your Name! ")
print("Hello !", name, "Solve this problem")


num = 16

if num < 0:
    print("Enter a positive number")
else:
    sum = 0
    # use while loop to iterate until zero
    while num > 0:
        sum += num
        num -= 1
    print("The sum is", sum)

