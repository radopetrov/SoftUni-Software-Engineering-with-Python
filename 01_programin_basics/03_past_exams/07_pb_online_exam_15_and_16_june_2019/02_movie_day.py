shooting_time = int(input())
scenes_number = int(input())
scene_lengh = int(input())
total_time = (scene_lengh * scenes_number) + (shooting_time * 0.15)
diference = abs(total_time - shooting_time)
if shooting_time >= total_time:
    print(f"You managed to finish the movie on time! You have {round(diference)} minutes left!")
else:
    print(f"Time is up! To complete the movie you need {round(diference)} minutes.")