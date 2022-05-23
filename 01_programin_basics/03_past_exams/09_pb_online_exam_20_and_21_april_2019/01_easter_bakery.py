flour_price = float(input())
flour_qty = float(input())
sugar_qty = float(input())
eggs_pack_qty = int(input())
yeast_pack_qty = int(input())
sugar_price = flour_price * 0.75
eggs_pack_price = flour_price * 1.1
yeast_price = sugar_price * 0.2
flour_costs = flour_qty * flour_price
sugar_costs = sugar_qty * sugar_price
eggs_pack_costs = eggs_pack_qty * eggs_pack_price
yeast_pack_costs = yeast_pack_qty * yeast_price
total_costs = flour_costs + sugar_costs + eggs_pack_costs + yeast_pack_costs
print(f"{total_costs:.2f}")