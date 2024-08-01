import math
from tqdm import tqdm

def find_min_expression(N):
    # Calculate p
    p = 10 ** math.ceil(len(str(N)) / 5)
    
    min_value = float('inf')
    optimal_a = 1
    optimal_b = N
    optimal_c = 0
    
    for a in tqdm(range(1, N + 1), desc="Calculations Progress"):
        b = N // a
        c = N - a * b
        current_value = a + b + c * p
        if current_value < min_value:
            min_value = current_value
            optimal_a = a
            optimal_b = b
            optimal_c = c
    
    return optimal_a, optimal_b, optimal_c, p, min_value

# Continuous loop for user input
while True:
    user_input = input("Enter the value of N (or type 'exit' to quit): ")
    if user_input.lower() == "exit":
        break

    try:
        N = int(user_input)
    except ValueError:
        print("Please enter a valid integer for N.")
        continue

    a, b, c, p, min_value = find_min_expression(N)
    
    # Print results
    print(f"N = {N}\na * b + c = {a} * {b} + {c}\np = 10^⌈len(N)/5⌉ = {p}\nSmallest a + b + c * p = {min_value}")

print("Exiting program.")