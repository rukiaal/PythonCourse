cabin_class=input("enter your cabin class(LUX, A, B, or C): ").upper()
if cabin_class =="LUX":
    print("Upper-deck cabin with a balcony.")
elif cabin_class =="A":
    print("Cabin above the car deck with a window")
elif cabin_class =="B":
    print("Windowless cabin above the car deck")
elif cabin_class=="C":
    print("Windowless cabin below the car deck")
else:
    print("Invalid cabin class")