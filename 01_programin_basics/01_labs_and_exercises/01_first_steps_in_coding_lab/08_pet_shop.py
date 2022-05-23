count_dog = int(input())
count_cat = int(input())
#една опаковка храна за кучета е на цена 2.50 лв, а опаковка храна за котки струва 4 лв.
price_dog = count_dog * 2.50
price_cat = count_cat * 4
total_price = price_dog + price_cat
print(f"{total_price} lv.")