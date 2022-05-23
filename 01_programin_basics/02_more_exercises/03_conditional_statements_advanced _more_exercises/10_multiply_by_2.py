import sys

n = sys.maxsize
for number in range(n):
    numbers = float(input())
    if numbers >= 0:
        result = numbers * 2
        print(f"Result: {result:.2f}")
    elif numbers < 0:
        print("Negative number")
        break