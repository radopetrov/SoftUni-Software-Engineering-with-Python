favourite_book = input()
books = input()
book_number = 0
is_book_found = False
while books != "No More Books":
    if favourite_book == books:
        is_book_found = True
        break
    book_number += 1
    books = input()
if is_book_found:
    print(f"You checked {book_number} books and found it.")
else:
    print("The book you search is not here!")
    print(f"You checked {book_number} books.")