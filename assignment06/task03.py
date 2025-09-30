airports = {}

while True:
    print("\n1. Enter a new airport")
    print("2. Fetch airport information")
    print("3. Quit")
    choice = input("Your choice: ")

    if choice == "1":
        code = input("Enter ICAO code: ")
        name = input("Enter airport name: ")
        airports[code] = name
    elif choice == "2":
        code = input("Enter ICAO code:  ")
        if code in airports:
            print("Airport name:", airports[code])
        else:
            print("Not found")
    elif choice == "3":
        break
