width = int(input())
length = int(input())
total_cake_pieces = width * length
command = input()
total_grabbed_pieces = 0
while command != "STOP":
    current_number_of_pieces = int(command)
    total_grabbed_pieces += current_number_of_pieces
    if total_grabbed_pieces > total_cake_pieces:
        break
    command = input()
diff = abs(total_grabbed_pieces - total_cake_pieces)
if total_grabbed_pieces > total_cake_pieces:
    print(f"No more cake left! You need {diff:.0f} pieces more.")
else:
    print(f"{diff:.0f} pieces are left.")