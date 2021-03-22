import random
print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

"""
What did you see on line 1?
7
What was the smallest number you could have seen, what was the largest?
smallest: 5, largest: 19

What did you see on line 2?
7
What was the smallest number you could have seen, what was the largest?
smallest: 3, largest: 9
Could line 2 have produced a 4?
no

What did you see on line 3?
5.3564461045119245
What was the smallest number you could have seen, what was the largest?
smallest: 2.5, largest: 5.49999999999999999999...
"""

print(random.randrange(101))
