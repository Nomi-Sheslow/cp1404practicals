from prac_06.guitar import Guitar


def main():
    guitar_1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    guitar_2 = Guitar("Another guitar", 2013)
    guitar_3 = Guitar("", (2020 - 50))
    print(guitar_1.get_age())       # Expected 98
    print(guitar_2.get_age())       # Expected 7
    print(guitar_1.is_vintage())    # Expected True
    print(guitar_2.is_vintage())    # Expected False
    print(guitar_3.is_vintage())    # Expected True


main()
