fuel_type = str(input())
tank_fuel_l = float(input())
fuels = fuel_type == "Diesel" or fuel_type == "Gasoline" or fuel_type == "Gas"
if fuels:
    if tank_fuel_l >= 25:
        print(f"You have enough {fuel_type.lower()}.")
    else:
        print(f"Fill your tank with {fuel_type.lower()}!")
else:
    print("Invalid fuel!")