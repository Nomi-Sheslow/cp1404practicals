"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
If the value entered in either the denominator or numerator is a float

2. When will a ZeroDivisionError occur?
If the value entered in the denominator is 0

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Yes
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
