email_to_name = {}
emails = []
email = input("Email: ")
while email != "":
    emails.append(email)
    split_email = email.split("@")
    name = split_email[0].replace(".", " ").title()
    confirmation = input(f"Is your name {name}? (Y/n) ").lower()
    while confirmation == "n":
        name = input("Name: ").title()
        confirmation = input(f"Is your name {name}? (Y/n) ").lower()
    email_to_name[name] = email
    email = input("Email: ")
for name, email in email_to_name.items():
    print(f"{name} ({email})")
