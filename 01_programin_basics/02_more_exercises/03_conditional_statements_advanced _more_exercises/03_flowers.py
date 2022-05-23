chrysanthemum_number = int(input())
roses_number = int(input())
tulips_number = int(input())
season = input() #Spring, Summer, Аutumn, Winter
hollyday = input() #Y or N
chrysanthemum_price = 0
roses_price = 0
tulips_price = 0
if season == "Spring" or season == "Summer":
    chrysanthemum_price = 2
    roses_price = 4.1
    tulips_price = 2.5
    if hollyday == "Y":
        chrysanthemum_price *= 1.15
        roses_price *= 1.15
        tulips_price *= 1.15
elif season == "Autumn" or season == "Winter":
    chrysanthemum_price = 3.75
    roses_price = 4.5
    tulips_price = 4.15
    if hollyday == "Y":
        chrysanthemum_price *= 1.15
        roses_price *= 1.15
        tulips_price *= 1.15
bouquet_price = chrysanthemum_price * chrysanthemum_number + roses_number * roses_price + tulips_number * tulips_price
total_flowers = chrysanthemum_number + tulips_number + roses_number
if tulips_number > 7 and season == "Spring":
    bouquet_price *= 0.95
if roses_number >= 10 and season == "Winter":
    bouquet_price *= 0.9
if total_flowers > 20:
    bouquet_price *= 0.8
bouquet_price += 2

print(f"{bouquet_price:.2f}")