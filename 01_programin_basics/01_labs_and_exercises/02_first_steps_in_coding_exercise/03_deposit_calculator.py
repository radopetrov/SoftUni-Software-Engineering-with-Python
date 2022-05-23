deposit = float(input())
months = int(input())
anual_interest_percent = float(input())

#сума = депозирана сума  + срок на депозита * ((депозирана сума * годишен лихвен процент ) / 12)
total_sum = deposit + months * ((deposit * (anual_interest_percent / 100)) / 12)
print(total_sum)