movie_title = input()
total_tickets = 0
student_counter = 0
standard_counter = 0
kid_counter = 0
while movie_title != "Finish":
    free_seats = int(input())
    taken_seats = 0
    ticket_type = input()
    while ticket_type != "End":
        taken_seats += 1
        total_tickets += 1
        if ticket_type == "student":
            student_counter += 1
        elif ticket_type == "standard":
            standard_counter += 1
        elif ticket_type == "kid":
            kid_counter += 1
        if taken_seats == free_seats:
            break
        ticket_type = input()
    hall_rate = taken_seats / free_seats * 100
    print(f"{movie_title} - {hall_rate:.2f}% full.")
    movie_title = input()
standard_share = standard_counter / total_tickets * 100
student_share = student_counter / total_tickets * 100
kid_share = kid_counter / total_tickets * 100
print(f"Total tickets: {total_tickets}")
print(f"{student_share:.2f}% student tickets.")
print(f"{standard_share:.2f}% standard tickets.")
print(f"{kid_share:.2f}% kids tickets.")