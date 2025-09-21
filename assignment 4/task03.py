numbers = []
user_input = input("Enter a number: ")
while user_input != " ":
    numbers.append(user_input)
    user_input = input("Enter a number: ")

if numbers:
    print("Smallest number:", min(numbers))
    print("Largest number:", max(numbers))
else:
    print("No numbers were entered.")

