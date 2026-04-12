# ----------- TASK 3: LIST -----------
justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]

print("Initial List:", justice_league)


# 1. Number of members
print("Total members:", len(justice_league))


# 2. Add Batgirl and Nightwing
justice_league.append("Batgirl")
justice_league.append("Nightwing")
print("\nAfter adding members:", justice_league)


# 3. Move Wonder Woman to front
justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print("\nAfter making Wonder Woman leader:", justice_league)


# 4. Separate Aquaman and Flash (user choice here)
middle_hero = input("\nEnter hero to place between Aquaman and Flash: ")
middle_hero = middle_hero.title()

if middle_hero in justice_league:
    justice_league.remove(middle_hero)

aquaman_index = justice_league.index("Aquaman")
flash_index = justice_league.index("Flash")

if aquaman_index < flash_index:
    justice_league.insert(aquaman_index + 1, middle_hero)
else:
    justice_league.insert(flash_index + 1, middle_hero)

print("After separating Aquaman and Flash:", justice_league)

# 5. Replace with new team (given in question)
justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print("\nNew team:", justice_league)


# 6. Sort list
justice_league.sort()
print("\nSorted team:", justice_league)

print("New Leader:", justice_league[0])