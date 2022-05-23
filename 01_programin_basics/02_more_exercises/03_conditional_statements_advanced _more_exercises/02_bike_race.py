junior_bikers = int(input())
senior_bikers = int(input())
track_type = input()
junior_fee = 0
senior_fee = 0
total_bikers = junior_bikers + senior_bikers
if track_type == "trail":
    junior_fee = 5.5
    senior_fee = 7
elif track_type == "cross-country":
    junior_fee = 8
    senior_fee = 9.5
    if total_bikers >= 50:
        junior_fee *= 0.75
        senior_fee *= 0.75
elif track_type == "downhill":
    junior_fee = 12.25
    senior_fee = 13.75
elif track_type == "road":
    junior_fee = 20
    senior_fee = 21.5
total_income = (junior_fee * junior_bikers + senior_bikers * senior_fee) * 0.95
print(f"{total_income:.2f}")