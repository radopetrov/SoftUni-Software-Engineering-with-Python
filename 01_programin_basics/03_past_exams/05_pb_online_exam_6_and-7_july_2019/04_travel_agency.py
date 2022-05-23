city = input() #"Bansko", "Borovets", "Varna" или "Burgas"
package_type = input() #"noEquipment", "withEquipment", "noBreakfast" или "withBreakfast"
vip_discount = input() #"yes" или "no"
days = int(input())
cities = city == "Bansko" or city == "Borovets" or city == "Varna" or city == "Burgas"
packages = package_type == "noEquipment" or package_type == "withEquipment" or package_type == "noBreakfast" or package_type == "withBreakfast"
package_price_per_day = 0
if city == "Bansko" or city == "Borovets":
    if package_type == "withEquipment":
        package_price_per_day = 100
        if vip_discount == "yes":
            package_price_per_day *= 0.9
    elif package_type == "noEquipment":
        package_price_per_day = 80
        if vip_discount == "yes":
            package_price_per_day *= 0.95
elif city == "Varna" or city == "Burgas":
    if package_type == "withBreakfast":
        package_price_per_day = 130
        if vip_discount == "yes":
            package_price_per_day *= 0.88
    elif package_type == "noBreakfast":
        package_price_per_day = 100
        if vip_discount == "yes":
            package_price_per_day *= 0.93

if days > 7:
    days -= 1

total_price = days * package_price_per_day

if days < 1:
    print(f"Days must be positive number!")
elif not cities:
    print(f"Invalid input!")
elif not packages:
    print(f"Invalid input!")
else:
    print(f"The price is {total_price:.02f}lv! Have a nice time!")