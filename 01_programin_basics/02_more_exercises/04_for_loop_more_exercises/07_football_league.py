stadium_seats = int(input())
fans_number = int(input())
section_a = 0
section_b = 0
section_v = 0
section_g = 0
for number in range(fans_number):
    staduim_section = input()
    if staduim_section=="A":
        section_a += 1
    elif staduim_section=="B":
        section_b += 1
    elif staduim_section=="V":
        section_v += 1
    elif staduim_section=="G":
        section_g += 1
section_a_rate = section_a / fans_number * 100
section_b_rate = section_b / fans_number * 100
section_v_rate = section_v / fans_number * 100
section_g_rate = section_g / fans_number * 100
fans_number_rate = fans_number / stadium_seats * 100
print(f"{section_a_rate:.02f}%")
print(f"{section_b_rate:.02f}%")
print(f"{section_v_rate:.02f}%")
print(f"{section_g_rate:.02f}%")
print(f"{fans_number_rate:.02f}%")