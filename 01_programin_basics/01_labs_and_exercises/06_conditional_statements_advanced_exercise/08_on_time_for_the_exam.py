start_hour = int(input())
start_minutes = int(input())
arival_hour = int(input())
arival_minutes= int(input())

start_time = start_hour * 60 + start_minutes
arival_time = arival_hour * 60 + arival_minutes
time_difference = abs(start_time - arival_time)
hours = time_difference // 60
minutes = time_difference % 60

if start_time < arival_time:
    print("Late")
elif start_time == arival_time or (start_time > arival_time and time_difference <= 30):
    print("On time")
elif start_time > arival_time and time_difference > 30:
    print("Early")

if start_time > arival_time and time_difference < 60:
    print(f"{minutes} minutes before the start")
elif start_time > arival_time and time_difference >= 60:
    print(f"{hours}:{minutes:02d} hours before the start")
elif start_time < arival_time and time_difference < 60:
    print(f"{minutes} minutes after the start")
elif start_time < arival_time and time_difference >= 60:
    print(f"{hours}:{minutes:02d} hours after the start")