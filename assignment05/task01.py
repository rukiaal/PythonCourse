import random
dice_num = int(input("How many dice you want to roll: "))
total = 0
for i in range(dice_num):
    roll = random.randint(1,6)
    total += roll
print(f"Sum of {dice_num} dice: {total}")