# ----------- TASK 5 -----------

import random

# PART 1: Dice Simulation (at least 20 times)
rolls = []

for i in range(20):
    rolls.append(random.randint(1, 6))

count_6 = 0
count_1 = 0
consecutive_6 = 0

for i in range(len(rolls)):
    if rolls[i] == 6:
        count_6 += 1
    if rolls[i] == 1:
        count_1 += 1

for i in range(len(rolls) - 1):
    if rolls[i] == 6 and rolls[i + 1] == 6:
        consecutive_6 += 1

print("Rolls:", rolls)
print("Number of 6s:", count_6)
print("Number of 1s:", count_1)
print("Two 6s in a row:", consecutive_6)


# PART 2: Jumping Jacks Workout

total = 0

for i in range(1, 11):
    print("\nDo 10 jumping jacks")
    total += 10

    tired = input("Are you tired? (yes/no): ").lower()

    if tired == "yes" or tired == "y":
        skip = input("Do you want to skip the remaining sets? (yes/no): ").lower()
        
        if skip == "yes" or skip == "y":
            print(f"You completed a total of {total} jumping jacks")
            break

    remaining = 100 - total

    if remaining > 0:
        print(f"{remaining} jumping jacks remaining")

else:
    print("\nCongratulations! You completed the workout")