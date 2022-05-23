months = int(input())
water_bill_per_month = 20
internet_bill_per_month = 15
electricity_total_bill = 0
other_bills_total = 0
for number in range(months):
    electricity_bill_per_mont = float(input())
    electricity_total_bill += electricity_bill_per_mont
    other_bills_total += (electricity_bill_per_mont + internet_bill_per_month + water_bill_per_month) * 1.2
water_bills_total = water_bill_per_month * months
internet_bills_total = internet_bill_per_month * months
total_bills = water_bills_total + internet_bills_total + electricity_total_bill + other_bills_total
average_bills_per_month = total_bills / months
print(f"Electricity: {electricity_total_bill:.02f} lv")
print(f"Water: {water_bills_total:.02f} lv")
print(f"Internet: {internet_bills_total:.02f} lv")
print(f"Other: {other_bills_total:.02f} lv")
print(f"Average: {average_bills_per_month:.02f} lv")