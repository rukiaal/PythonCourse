length=float(input("Enter the length of the zander in centimeters: "))
legal_zander_length=42.0
if length<legal_zander_length:
    print("The zander is too small and must be released back into the lake.")
    short_by=legal_zander_length -length
    print(f"{short_by:.2f} cm under the legal length")

else:
    print("you can take!! ")