number1=float(input("Enter talents:"))
number2=float(input("Enter pounds:"))
number3=float(input("Enter lots:"))
total_grams = (number1 * 8512) + (number2 * 425.6) + (number3 * 13.3)
kilograms = int(total_grams // 1000)
grams = total_grams % 1000
print((f"The weight in modern units is: {kilograms} kilograms and {grams:.2f} grams."))
