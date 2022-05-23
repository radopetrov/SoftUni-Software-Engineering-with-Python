v = int(input())  # Обема на басейна в литри
p1 = int(input())  # Дебит на първата тръба за час
p2 = int(input())  # Дебит на втората трба за час
h = float(input())  # Часовете които работникът отсъства

pipe_1 = p1 * h
pipe_2 = p2 * h
pool = pipe_1 + pipe_2

pipe_1_percent = (pipe_1 / pool) * 100
pipe_2_percent = (pipe_2 / pool) * 100
total_percent = (pool / v) * 100
overflow = abs(pool - v)

if pool <= v:
    print(f"The pool is {total_percent:.2f}% full. Pipe 1: {pipe_1_percent:.2f}%. Pipe 2: {pipe_2_percent:.2f}%.")
else:
    print(f"For {h:.2f} hours the pool overflows with {overflow:.2f} liters.")
