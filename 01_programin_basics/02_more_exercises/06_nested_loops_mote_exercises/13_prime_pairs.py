first_pair_start = int(input())
second_pair_start = int(input())
first_pair_difference = int(input())
second_pair_difference = int(input())
for first_pair in range(first_pair_start, first_pair_start + first_pair_difference + 1):
    for second_pair in range(second_pair_start, second_pair_start + second_pair_difference + 1):
        are_prime_pairs = True
        for number in range(2, 10):
            if first_pair % number == 0 or second_pair % number == 0:
                are_prime_pairs = False
                break
        if are_prime_pairs:
            print(f"{first_pair}{second_pair}")
