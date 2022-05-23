season = str(input())
group_type = str(input())
students_number = int(input())
days = int(input())
price_per_day = 0
sport = ""
if season == "Winter":
    if group_type == "boys" or group_type == "girls":
        price_per_day = 9.6
        if group_type == "girls":
            sport = "Gymnastics"
        else:
            sport = "Judo"
    elif group_type == "mixed":
        price_per_day = 10
        sport = "Ski"
elif season == "Spring":
    if group_type == "boys" or group_type == "girls":
        price_per_day = 7.2
        if group_type == "girls":
            sport = "Athletics"
        else:
            sport = "Tennis"
    elif group_type == "mixed":
        price_per_day = 9.5
        sport = "Cycling"
elif season == "Summer":
    if group_type == "boys" or group_type == "girls":
        price_per_day = 15
        if group_type == "girls":
            sport = "Volleyball"
        else:
            sport = "Football"
    elif group_type == "mixed":
        price_per_day = 20
        sport = "Swimming"
total_cost = students_number * price_per_day * days
if students_number >= 50:
    total_cost *= 0.5
elif students_number >= 20 and students_number < 50:
    total_cost *= 0.85
elif students_number >= 10 and students_number < 20:
    total_cost *= 0.95
print(f"{sport} {total_cost:.2f} lv.")