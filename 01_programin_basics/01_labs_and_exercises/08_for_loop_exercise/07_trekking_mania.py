groups_number = int(input())
musala = 0
monblan = 0
kilimandjaro = 0
k2 = 0
everest = 0
for i in range(groups_number):
    hikers_in_group = int(input())
    if hikers_in_group <= 5:
        musala += hikers_in_group
    elif hikers_in_group <= 12:
        monblan += hikers_in_group
    elif hikers_in_group <= 25:
        kilimandjaro += hikers_in_group
    elif hikers_in_group <= 40:
        k2 += hikers_in_group
    elif hikers_in_group >= 41:
        everest += hikers_in_group
total_hikers = musala + monblan + kilimandjaro + k2 + everest
musala_percent = musala / total_hikers * 100
monblan_percent = monblan / total_hikers * 100
kilimandjaro_percent = kilimandjaro / total_hikers * 100
k2_percent = k2 / total_hikers * 100
everest_percent = everest / total_hikers * 100

print(f"{musala_percent:.2f}%\n{monblan_percent:.2f}%\n{kilimandjaro_percent:.2f}%\n{k2_percent:.2f}%\n{everest_percent:.2f}%")