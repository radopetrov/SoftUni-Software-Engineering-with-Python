breed = input()
sex = input()
years = 0
breeds = ["British Shorthair", "Siamese", "Persian", "Ragdoll", "American Shorthair", "Siberian"]
if breed == "British Shorthair":
    if sex == "m":
        years = 13
    elif sex == "f":
        years = 14
elif breed == "Siamese":
    if sex == "m":
        years = 15
    elif sex == "f":
        years = 16
elif breed == "Persian":
    if sex == "m":
        years = 14
    elif sex == "f":
        years = 15
elif breed == "Ragdoll":
    if sex == "m":
        years = 16
    elif sex == "f":
        years = 17
elif breed == "American Shorthair":
    if sex == "m":
        years = 12
    elif sex == "f":
        years = 13
elif breed == "Siberian":
    if sex == "m":
        years = 11
    elif sex == "f":
        years = 12
cat_months = (years * 12) / 6
if breed in breeds:
    print(f"{cat_months:.0f} cat months")
else:
    print(f"{breed} is invalid cat!")