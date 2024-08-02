import random
import math
import sys
import sympy
import threading
import time

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def pollards_rho(n):
    if n % 2 == 0:
        return 2
    x = random.randint(2, n-1)
    y = x
    c = random.randint(1, n-1)
    d = 1

    while d == 1:
        x = (x*x + c) % n
        y = (y*y + c) % n
        y = (y*y + c) % n
        d = gcd(abs(x-y), n)
        if d == n:
            return n 
    return d

def factorize_number_with_sympy(n):
    return sympy.factorint(n)

def combined_factorization(n):
    start_time = time.time()
    try:
        factors = factorize_number_with_sympy(n)
    except Exception as e:
        factors = {}
        print(f"SymPy failed with exception: {e}")

    if not factors:
        def pollards_rho_with_timeout(n):
            result = [None]
            def factorize():
                result[0] = pollards_rho(n)
            factor_thread = threading.Thread(target=factorize)
            factor_thread.start()
            factor_thread.join(timeout=5)
            if factor_thread.is_alive():
                factor_thread.join() 
                return None
            return result[0]

        def factorize_recursively(n):
            if n == 1:
                return
            factor = pollards_rho_with_timeout(n)
            if factor is None or factor == n:
                return {n: 1}
            else:
                factors[factor] = factors.get(factor, 0) + 1
                sub_factors = factorize_recursively(n // factor)
                for key, value in sub_factors.items():
                    factors[key] = factors.get(key, 0) + value
                return factors

        factors = factorize_recursively(n)
    
    end_time = time.time()
    print(f"Time taken: {end_time - start_time:.6f} seconds")
    return factors

def format_factors(factors):
    formatted_factors = []
    for factor, count in factors.items():
        if count == 1:
            formatted_factors.append(f"{factor}")
        else:
            formatted_factors.append(f"{factor}^{count}")
    return f"[{', '.join(formatted_factors)}]"

def main():
    while True:
        user_input = input("Enter a number to factorize (or type 'e' to close): ")
        if user_input.lower() == 'e':
            print("Exiting the program...")
            break

        try:
            number = int(user_input)
            if number < 1:
                raise ValueError("The number must be greater than 0.")
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a valid positive integer or 'e' to close.")
            continue

        factors = combined_factorization(number)
        formatted_factors = format_factors(factors)
        print(f"Factors: {formatted_factors}")

if __name__ == "__main__":
    main()
