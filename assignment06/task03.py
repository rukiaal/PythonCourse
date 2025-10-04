airports = {}

while True:
    choice = input("\n1 = Add, 2 = Fetch, 3 = Quit: ")

    if choice == "1":
        code = input("ICAO code: ")
        name = input("Airport name: ")
        airports[code] = name
        print("Saved!")

    elif choice == "2":
        code = input("Enter ICAO code: ")
        if code in airports:
            print("Airport:", airports[code])
        else:
            print("Not found.")

    elif choice == "3":
        break

    else:
        print("Invalid choice")
