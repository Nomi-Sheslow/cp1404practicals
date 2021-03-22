VALID_LENGTH = 10
password = input("Password: ")
while len(password) != VALID_LENGTH:
    print("Invalid length")
    password = input("Password: ")
print(VALID_LENGTH * "*")
