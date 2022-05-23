company_name = str(input())
adult_tickets_num = int(input())
kids_tickets_num = int(input())
adult_tickets_price_net = float(input())
service_fee = float(input())

kids_tickets_price_net = adult_tickets_price_net * 0.3

total = (adult_tickets_num*(adult_tickets_price_net + service_fee))+(kids_tickets_num*(kids_tickets_price_net+service_fee))
profit = total * 0.2

print(f"The profit of your agency from {company_name} tickets is {profit:.2f} lv.")