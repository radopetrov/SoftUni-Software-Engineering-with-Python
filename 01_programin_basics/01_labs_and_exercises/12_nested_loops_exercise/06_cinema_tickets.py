movie_title = input()
students_tickets_count = 0
standard_tickets_count = 0
kid_tickets_count = 0
total_ticket_counter = 0
while movie_title != "Finish":
    hall_seats = int(input())
    ticket_type = input()
    current_movie_ticket_counter = 0
    while ticket_type != "End":
        total_ticket_counter += 1
        current_movie_ticket_counter += 1
        if ticket_type == "student":
            students_tickets_count += 1
        elif ticket_type == "standard":
            standard_tickets_count += 1
        elif ticket_type == "kid":
            kid_tickets_count += 1
        if current_movie_ticket_counter == hall_seats:
            break
        ticket_type = input()
    percentage_of_hall_filled = current_movie_ticket_counter/ hall_seats * 100
    print(f"{movie_title} - {percentage_of_hall_filled:.2f}% full.")
    movie_title = input()
student_tickets_share = students_tickets_count / total_ticket_counter * 100
standard_tickets_share = standard_tickets_count / total_ticket_counter * 100
kid_tickets_share = kid_tickets_count / total_ticket_counter * 100
print(f"Total tickets: {total_ticket_counter}")
print(f"{student_tickets_share:.2f}% student tickets.")
print(f"{standard_tickets_share:.2f}% standard tickets.")
print(f"{kid_tickets_share:.2f}% kids tickets.")
