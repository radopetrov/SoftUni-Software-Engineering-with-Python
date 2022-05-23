budget = float(input())
season = input()

destination = "" # Bulgaria, Balkans or Europe
location = "" #Camp or Hotel

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        location = "Camp"
        budget *= 0.3
    elif season == "winter":
        location = "Hotel"
        budget *= 0.7
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        location = "Camp"
        budget *= 0.4
    elif season == "winter":
        location = "Hotel"
        budget *= 0.8
elif budget > 1000:
    destination = "Europe"
    location = "Hotel"
    budget *= 0.9

print(f"Somewhere in {destination}")
print(f"{location} - {budget:.2f}")