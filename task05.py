talents = int(input("Enter number of talents (leiviskä): "))
pounds = int(input("Enter number of pounds (naula): "))
lots = int(input("Enter number of lots (luoti): "))
LOTS_IN_POUND = 32
POUNDS_IN_TALENT = 20
GRAMS_IN_LOT = 13.3
total_lots = (talents * POUNDS_IN_TALENT * LOTS_IN_POUND) + (pounds * LOTS_IN_POUND) + lots
total_grams = total_lots * GRAMS_IN_LOT
kilograms = int(total_grams // 1000)
grams = total_grams % 1000
print(f"The weight in modern units is: {kilograms} kilograms and {grams:.2f} grams.")