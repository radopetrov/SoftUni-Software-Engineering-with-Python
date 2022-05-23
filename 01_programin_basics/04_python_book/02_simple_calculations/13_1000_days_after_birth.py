import datetime as dt

date_str = input()
date = dt.datetime.strptime(date_str, "%d-%m-%Y").date()
date += dt.timedelta(days = 1000)
print(date.strftime("%d-%m-%Y"))