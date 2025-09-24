numbers = []

user_input = input("Enter your number (press Enter to quit): ")
while user_input != "":
    numbers.append(user_input)
    user_input = input("Enter your number (press Enter to quit): ")

if numbers:
    numbers.sort(reverse=True)
    print("The five greatest numbers (descending):", numbers[:5])
else:
    print("No number added, try again!")
