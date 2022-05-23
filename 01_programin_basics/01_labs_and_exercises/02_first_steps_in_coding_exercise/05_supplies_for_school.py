pens = int(input())
markers = int(input())
cleaner = int(input())
discount = int(input())
pens_price = 5.80
markers_price = 7.20
cleaner_price = 1.20

pens_sum = pens * pens_price
markers_sum = markers * markers_price
cleaner_sum = cleaner * cleaner_price

total_sum_bef_dis = pens_sum + markers_sum + cleaner_sum
total_sum = total_sum_bef_dis - (total_sum_bef_dis * discount / 100)
print(total_sum)
