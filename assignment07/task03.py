def sum_list(numbers):
    total = 0
    for n in numbers:
        total += n
    return total

numbers = []
num = int(input("Enter a number (or press Enter to stop): "))

while num != "":
    numbers.append(int(num))
    num = input("Enter a number (or press Enter to stop): ")

print("The sum of the numbers is:", sum_list(numbers))
