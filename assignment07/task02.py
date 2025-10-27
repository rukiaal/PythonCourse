def gallons_to_liters(gallons):
    return gallons * 3.785
gallons = float(input("Enter volume in gallons (negative number to stop): "))

while gallons >= 0:
    liters = gallons_to_liters(gallons)
    print(f"{gallons} gallons = {liters:.2f} liters\n")
    gallons = float(input("Enter volume in gallons (negative number to stop): "))

print("Program ended.")
