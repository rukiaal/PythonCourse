names = set()

name = input("Enter a name (press Enter to quit): ")
while name != "":
    if name in names:
        print("Existing name")
    else:
        print("New name")
        names.add(name)
    name = input("Enter a name (press Enter to quit): ")

print("\nUnique names entered: ")
for n in names:
    print(n)
