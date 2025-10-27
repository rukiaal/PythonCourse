import math
def unit_price(diameter_cm, price_eur):
    radius_m = (diameter_cm / 2) / 100
    area = math.pi * radius_m ** 2
    return price_eur / area
diam1 = float(input("Enter diameter of first pizza (cm): "))
price1 = float(input("Enter price of first pizza (€): "))
up1 = unit_price(diam1, price1)

diam2 = float(input("Enter diameter of second pizza (cm): "))
price2 = float(input("Enter price of second pizza (€): "))
up2 = unit_price(diam2, price2)

print(f"\nUnit price of first pizza: €{up1:.2f} per m²")
print(f"Unit price of second pizza: €{up2:.2f} per m²")

if up1 < up2:
    print("The first pizza provides better value for money.")
elif up2 < up1:
    print("The second pizza provides better value for money.")
else:
    print("Both pizzas have the same value for money.")
