processor_price_usd = float(input())
video_card_price_usd = float(input())
ram_memory_usd = float(input())
ram_memory_number = int(input())
interest_discount = float(input())
usd_to_bgn = 1.57
processor_price_bgn = processor_price_usd * usd_to_bgn
video_card_price_bgn = video_card_price_usd * usd_to_bgn
ram_memory_bgn = (ram_memory_usd * usd_to_bgn) * ram_memory_number
processor_price_bgn *= (1 - interest_discount)
video_card_price_bgn *= (1 - interest_discount)
total_costs = processor_price_bgn + ram_memory_bgn + video_card_price_bgn
print(f"Money needed - {total_costs:.2f} leva.")