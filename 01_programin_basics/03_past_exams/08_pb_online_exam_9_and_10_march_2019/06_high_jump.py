desired_height = int(input())
is_successful = True
start_height = desired_height - 30
attempt_fails = 0
attempt_counter = 0
last_attempt = 0
while is_successful:
    attempt = int(input())
    attempt_counter += 1
    if attempt > start_height:
        attempt_fails = 0
        if desired_height == start_height:
            last_attempt = start_height
            break
        start_height += 5
    else:
        attempt_fails += 1
        if attempt_fails == 3:
            is_successful = False
            last_attempt = start_height
            break
if is_successful:
    print(f"Tihomir succeeded, he jumped over {last_attempt}cm after {attempt_counter} jumps.")
else:
    print(f"Tihomir failed at {last_attempt}cm after {attempt_counter} jumps.")