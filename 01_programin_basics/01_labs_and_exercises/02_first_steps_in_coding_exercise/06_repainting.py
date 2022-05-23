plastic = int(input())
paint = int(input())
paint_thiner = int(input())
work_hours = int(input())

supplies = (plastic + 2) * 1.50 + (paint + paint * 0.1) * 14.50 + paint_thiner * 5.00 + 0.40
workers_payment = work_hours * (supplies * 0.30)
total_cost = supplies + workers_payment

print(total_cost)
