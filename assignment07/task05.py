import math
def price_per_m2(diameter, price):
    radius = (diameter / 2 )/ 100
    area = math.pi * radius ** 2
    return price / area
d1 = float(input("Enter diameter of first pizza (cm): "))
p1 = float(input("Enter price of first pizza (€): "))

d2 = float(input("Enter diameter of second pizza (cm): "))
p2 = float(input("Enter price of second pizza (€): "))

pizza1 = price_per_m2(d1, p1)
pizza2 = price_per_m2(d2, p2)

print(f"First pizza: €{pizza1:.2f} per m²")
print(f"Second pizza: €{pizza2:.2f} per m²")


if pizza1 < pizza2:
    print("The first pizza is better value.")
elif pizza2 < pizza1:
    print("The second pizza is better value.")
else:
    print("Both pizzas have the same value.")
