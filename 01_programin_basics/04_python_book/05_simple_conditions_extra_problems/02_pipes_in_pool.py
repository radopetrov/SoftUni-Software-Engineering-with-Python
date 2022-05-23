from math import  trunc

pool_volume = int(input())
first_pipe_flow_rate = int(input())
second_pipe_flow_rate = int(input())
hours = float(input())
first_pipe_water = first_pipe_flow_rate * hours
second_pipe_water = second_pipe_flow_rate * hours
total_water = first_pipe_water + second_pipe_water
first_pipe_share_rate = first_pipe_water / total_water * 100
second_pipe_share_rate = second_pipe_water / total_water * 100
pool_rate = total_water / pool_volume * 100
if total_water <= pool_volume:
    print(f"The pool is {trunc(pool_rate)}% full. Pipe 1: {trunc(first_pipe_share_rate)}%. Pipe 2: {trunc(second_pipe_share_rate)}%.")
else:
    diff = abs(pool_volume - total_water)
    print(f"For {hours} hours the pool overflows with {diff:.0f} liters.")
