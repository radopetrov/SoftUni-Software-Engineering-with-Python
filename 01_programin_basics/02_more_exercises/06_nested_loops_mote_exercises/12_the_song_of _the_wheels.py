control_number = int(input())
counter = 0
password = ""
is_a_password = False
for digit_a in range(1, 10):
    for digit_b in range(1, 10):
        for digit_c in range(1, 10):
            for digit_d in range(1, 10):
                if digit_a * digit_b + digit_c * digit_d == control_number:
                    if digit_a < digit_b and digit_c > digit_d:
                        counter += 1
                        print(f"{digit_a}{digit_b}{digit_c}{digit_d} ", end = "")
                        if counter == 4:
                            is_a_password = True
                            password = f"{digit_a}{digit_b}{digit_c}{digit_d}"
print()
if is_a_password:
    print(f"Password: {password}")
else:
    print("No!")

