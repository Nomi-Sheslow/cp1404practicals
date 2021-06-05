from prac_08.silver_service_taxi import SilverServiceTaxi

"""
-- Test 1 --
Expected output:
hummer, fuel = 200, odometer = 0, 0km on current fare, $4.92/km plus flagfall of $4.50
"""
car_1 = SilverServiceTaxi('hummer', 200, 4)
print(car_1)

"""
-- Test 2 --
Expected output:
car, fuel = 182, odometer = 18, 18km on current fare, $2.46/km plus flagfall of $4.50
Fare: $48.78
"""
car_2 = SilverServiceTaxi('car', 200, 2)
car_2.drive(18)
print(car_2)
print(f"Fare: ${car_2.get_fare()}")
