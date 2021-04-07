import random

NUMBER_OF_COLUMNS = 6
MIN_NUMBER = 1
MAX_NUMBER = 45

numbers = []
number_of_picks = int(input("How many quick picks? "))
for i in range(number_of_picks):
    for j in range(NUMBER_OF_COLUMNS):
        random_number = random.randint(MIN_NUMBER, MAX_NUMBER)
        while random_number in numbers:
            random_number = random.randint(MIN_NUMBER, MAX_NUMBER)
        numbers.append(random_number)
        numbers.sort()
    print(numbers)
    numbers = []
