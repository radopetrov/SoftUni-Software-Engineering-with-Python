import sys

movies_number = int(input())
top_rated_movie_title = ""
lowest_rated_movie_title = ""
top_rating = -sys.maxsize
lowest_rating = sys.maxsize
total_rating = 0
for number in range(movies_number):
    movie_title = input()
    movie_rating = float(input())
    total_rating += movie_rating
    if movie_rating > top_rating:
        top_rating = movie_rating
        top_rated_movie_title = movie_title
    if movie_rating < lowest_rating:
        lowest_rating = movie_rating
        lowest_rated_movie_title = movie_title
average_rating = total_rating / movies_number
print(f"{top_rated_movie_title} is with highest rating: {top_rating:.1f}")
print(f"{lowest_rated_movie_title} is with lowest rating: {lowest_rating:.1f}")
print(f"Average rating: {average_rating:.1f}")
