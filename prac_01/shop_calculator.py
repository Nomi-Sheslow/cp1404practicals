number_of_items = int(input("Number of items: "))
total_price = 0
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))
for item in range(0, number_of_items):
    price = float(input("Price of item: "))
    total_price += price
if total_price > 100:
    total_price = total_price - (total_price * 0.1)
print(f"Total price {number_of_items} items is ${total_price:.2f}")
