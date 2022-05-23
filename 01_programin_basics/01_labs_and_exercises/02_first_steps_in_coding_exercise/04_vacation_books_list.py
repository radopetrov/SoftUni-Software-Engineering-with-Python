book_pages = int(input())
pages_per_hour = int(input())
days = int(input())

hours = (book_pages // days) // pages_per_hour
print(hours)