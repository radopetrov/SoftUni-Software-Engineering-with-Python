movie_title = input()
movie_counter = 0
is_movie_limit_reached = False
best_movie = ""
best_movie_point = 0
while movie_title != "STOP":
    movie_counter += 1
    current_movie_points = 0
    for current_letter in movie_title:
        current_movie_points += ord(current_letter)
        if 65 <= ord(current_letter) <= 90:  #upper letters
            current_movie_points -= len(movie_title)
        elif ord(current_letter) == 32:
            continue
        elif 97 <= ord(current_letter) <= 122:   #lower letters
            current_movie_points -= (len(movie_title) * 2)
    if current_movie_points > best_movie_point:
        best_movie = movie_title
        best_movie_point = current_movie_points
    if movie_counter == 7:
        is_movie_limit_reached = True
        break
    else:
        movie_title = input()
if is_movie_limit_reached:
    print("The limit is reached.")
print(f"The best movie for you is {best_movie} with {best_movie_point} ASCII sum.")