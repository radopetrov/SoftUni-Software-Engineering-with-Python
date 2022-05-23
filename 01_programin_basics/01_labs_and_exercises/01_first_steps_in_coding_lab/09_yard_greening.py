kvm = float(input())

#The final price is: {крайна цена на услугата} lv.
#The discount is: {отстъпка} lv.
price_total = kvm * 7.61
disc = price_total * 0.18
price_final = price_total - disc

print(f'The final price is: {price_final} lv.')
print(f'The discount is: {disc} lv.')