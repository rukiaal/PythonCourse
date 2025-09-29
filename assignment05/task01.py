import random
dice_num = int(input("How many dice you want to roll: "))
total = 0
print("Rolling the dice...")
for i in range(dice_num):
    roll = random.randint(1, 6)
    print(f"Die {i+1}: {roll}")
    total += roll
print(f"Sum of {dice_num} dice: {total}")
