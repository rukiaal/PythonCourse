def remove_odd(numbers):
    even_numbers = []
    for n in numbers:
        if n % 2 == 0:
            even_numbers.append(n)
    return even_numbers
numbers = []
num = input("Enter a number (press Enter to stop): ")

while num != "":
    numbers.append(int(num))
    num = input("Enter a number (press Enter to stop): ")
filtered = remove_odd(numbers)
print("Original list:", numbers)
print("List without odd numbers:", filtered)
