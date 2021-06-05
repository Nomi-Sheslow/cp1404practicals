from prac_08.taxi import Taxi

""" 
-- Test 1 -- 
Expected results:
prius 1, fuel = 60, odometer = 40, 40km on current fare, $1.23/km
Fare cost: $49.20
"""
prius_1 = Taxi("prius 1", 100)
prius_1.drive(40)
print(prius_1)
print(f"Fare cost: ${prius_1.get_fare():.2f}")

""" 
-- Test 2 -- 
Expected results:
prius 1, fuel = 0, odometer = 100, 60km on current fare, $1.23/km
Fare cost: $73.80
"""
prius_1.start_fare()
prius_1.drive(100)
print(prius_1)
print(f"Fare cost: ${prius_1.get_fare():.2f}")
