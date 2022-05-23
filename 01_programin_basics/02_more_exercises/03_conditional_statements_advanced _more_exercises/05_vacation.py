budget = float(input())
season = str(input())
place_type = ""
location = ""
if budget <= 1000:
    place_type = "Camp"
    if season == "Summer":
        budget *= 0.65
        location = "Alaska"
    elif season == "Winter":
        budget *= 0.45
        location = "Morocco"
elif budget <= 3000:
    place_type = "Hut"
    if season == "Summer":
        budget *= 0.8
        location = "Alaska"
    elif season == "Winter":
        budget *= 0.6
        location = "Morocco"
elif budget > 3000:
    place_type = "Hotel"
    budget *= 0.9
    if season == "Summer":
        location = "Alaska"
    elif season == "Winter":
        location = "Morocco"
print(f"{location} - {place_type} - {budget:.2f}")