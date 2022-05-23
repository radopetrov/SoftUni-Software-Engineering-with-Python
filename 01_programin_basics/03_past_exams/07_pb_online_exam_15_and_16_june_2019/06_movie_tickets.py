number_a1 = int(input())
number_a2 = int(input())
number_n = int(input())
# symbol_1 = symbol ASCII code from a1 to a2 - 1
# symbol_2 = number from 1 to n - 1
# symbol_3 = number from 1 to n/2 -1
# symbol_4 = number representation of symbol_1 (ASCII code)
for symbol_1 in range(number_a1, number_a2):
    for symbol_2 in range(1, number_n):
        for symbol_3 in range(1, int(number_n / 2)):
            if symbol_1 % 2 != 0 and (symbol_1 + symbol_2 + symbol_3) % 2 != 0:
                print(f"{chr(symbol_1)}-{symbol_2}{symbol_3}{symbol_1}")
