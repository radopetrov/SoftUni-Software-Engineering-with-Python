number_1 = int(input())
number_2 = int(input())
oper = input()

# sum = n1 + n2
# sub = n1 - n2
# mult = n1 * n2
# if n2 > 0:
#     div = n1/ n2
# if n2 > 0:
#     divv = n1 % n2
# ev_odd_sum = ""
# ev_odd_sub = ""
# ev_odd_mul = ""
# if sum % 2 == 0:
#     ev_odd_sum = "even"
# else:
#     ev_odd_sum = "odd"
# if sub % 2 == 0:
#     ev_odd_sub = "even"
# else:
#     ev_odd_sub = "odd"
# if mult % 2 == 0:
#     ev_odd_mul = "even"
# else:
#     ev_odd_mul = "odd"
# if oper == "+" or oper == "-" or oper =="*":
#     if oper == "+":
#         print(f"{n1} {oper} {n2} = {sum} - {ev_odd_sum}")
#     elif oper == "-":
#         print(f"{n1} {oper} {n2} = {sub} - {ev_odd_sub}")
#     elif oper == "*":
#         print(f"{n1} {oper} {n2} = {mult} - {ev_odd_mul}")
# elif oper == "/":
#     if n2 > 0:
#         print(f"{n1} / {n2} = {div:.2f}")
#     else:
#         print(f"Cannot divide {n1} by zero")
# elif oper == "%":
#     if n2 > 0:
#         print(f"{n1} % {n2} = {divv}")
#     else:
#         print(f"Cannot divide {n1} by zero")
result = 0
odd_or_even = "odd"
if oper == "+" or oper == "-" or oper =="*":
    if oper == "+":
        result = number_1 + number_2
    elif oper == "-":
        result = number_1 - number_2
    else:
        result = number_1 * number_2
    if result % 2 == 0:
        odd_or_even = "even"
    print(f"{number_1} {oper} {number_2} = {result} - {odd_or_even}")
else:
    if number_2 == 0:
        print(f"Cannot divide {number_1} by zero")
    else:
        if oper == "/":
            result = number_1 / number_2
            print(f"{number_1} / {number_2} = {result:.2f}")
        else:
            result = number_1 % number_2
            print(f"{number_1} % {number_2} = {result}")