from prac_08.unreliable_car import UnreliableCar

""" 
-- Test 1 -- 
Expected results:
reliability = 0%
kia, fuel = 100, odometer = 0, 0km driven.
"""
kia = UnreliableCar("kia", 100, 0)
kia.drive(40)
print(kia)

""" 
-- Test 2 -- 
Expected results:
reliability = 100%
kia, fuel = 60, odometer = 40, 40km driven.
"""
kia = UnreliableCar("kia", 100, 100)
kia.drive(40)
print(kia)
