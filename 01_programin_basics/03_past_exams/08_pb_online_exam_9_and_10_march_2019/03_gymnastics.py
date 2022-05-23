country = input()
apparatus = input()
difficulty = 0
performance = 0
if country == "Russia":
    if apparatus == "ribbon":
        difficulty = 9.1
        performance = 9.4
    elif apparatus == "hoop":
        difficulty = 9.3
        performance = 9.8
    elif apparatus == "rope":
        difficulty = 9.6
        performance = 9
elif country == "Bulgaria":
    if apparatus == "ribbon":
        difficulty = 9.6
        performance = 9.4
    elif apparatus == "hoop":
        difficulty = 9.55
        performance = 9.75
    elif apparatus == "rope":
        difficulty = 9.5
        performance = 9.4
elif country == "Italy":
    if apparatus == "ribbon":
        difficulty = 9.2
        performance = 9.5
    elif apparatus == "hoop":
        difficulty = 9.45
        performance = 9.35
    elif apparatus == "rope":
        difficulty = 9.7
        performance = 9.15
total_points = difficulty + performance
rate = (20 - total_points) / 20 * 100
print(f"The team of {country} get {total_points:.3f} on {apparatus}.")
print(f"{rate:.2f}%")