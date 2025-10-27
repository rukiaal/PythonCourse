def gallons_to_liters(gallons):
    return gallons * 3.78541
gallons = float(input("Enter gallons (negative to quit): "))
while gallons >= 0:
    print(f"{gallons} gallons is {gallons_to_liters(gallons):.2f} liters")
    gallons = float(input("Enter gallons (negative to quit): "))
