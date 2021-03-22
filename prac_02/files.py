"""
1) Write code that asks the user for their name, then opens a file called "name.txt" and writes that name to it.
"""
name = "name.txt"
out_file = open(name, 'w')
name = input("What is your name? ")
out_file.write(name)
out_file.close()

"""
2) Write code that opens "name.txt" and reads the name (as above) then prints,
"Your name is Bob" (or whatever the name is in the file).
"""
in_file = open("name.txt", 'r')
name = in_file.readline()
print("Your name is {}".format(name))
in_file.close()

"""
3) Create a text file called numbers.txt and save it in your prac_02 directory. Put the following three numbers on
separate lines in the file and save it:
17
42
400
"""
in_file = open("numbers.txt", 'r')
print(in_file.readline(), end="")       # To print the first number and remove space after number
for line in in_file:
    print(line, end="")                 # To print the rest of the lines and remove space after each entry
in_file.close()

"""
4) Write code that opens "numbers.txt", reads only the first two numbers and adds them together then prints the result, 
which should be... 59.
"""
numbers = "numbers.txt"
in_file = open(numbers, 'r')
number_1 = in_file.readline()
number_2 = in_file.readline()
total = int(number_1) + int(number_2)
print(f"\n{total}")                     # Enters value on next line so it does not interfere with the previous activity
in_file.close()

"""
5) Now write a fourth block of code that prints the total for all lines in numbers.txt or a file with any number of 
numbers.
"""
numbers = "numbers.txt"
in_file = open(numbers, 'r')
total = int(in_file.readline())         # Sets first value in file to total
for line in in_file:
    total += int(in_file.readline())    # Adds each subsequent line to the total
print("Total = {}".format(total))
