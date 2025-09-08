import random  # Import the random module
combination_3_digit = [random.randint(0, 9) for _ in range(3)]
combination_4_digit = [random.randint(1, 6) for _ in range(4)]
print("3-digit lock combination (0-9):", combination_3_digit)
print("4-digit lock combination (1-6):", combination_4_digit)
