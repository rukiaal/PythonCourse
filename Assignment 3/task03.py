gender=input("please inter your biological gender(male or female): ").lower()
hemoglobin_level=float(input("please inter your hemoglobin level : "))
if gender == "female":
    if hemoglobin_level <117:
        print("low hemoglobin level")
    elif hemoglobin_level >155:
        print("high hemoglobin level")
    else:
        print("normal range!")
if gender == "male":
    if hemoglobin_level <134:
        print("low hemoglobin level")
    elif hemoglobin_level >167:
        print("high hemoglobin level")
    else:
        print("normal range1")