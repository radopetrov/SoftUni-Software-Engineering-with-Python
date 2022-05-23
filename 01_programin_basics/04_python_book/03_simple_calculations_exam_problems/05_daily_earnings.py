work_days = int(input())
daily_profit = float(input())  # in USD
usd_to_bgn_ex_rate = float(input())
monthly_salary = work_days * daily_profit
bonus = monthly_salary * 2.5
yearly_salary = monthly_salary * 12 + bonus
yearly_salary *= usd_to_bgn_ex_rate
yearly_salary *= 0.75
yearly_salary /= 365
print(f"{yearly_salary:.2f}")