# ----------- TASK 2: NUMBERS (WITH USER INPUT) -----------

# PART 1: format() function
num = int(input("Enter a number: "))
char = input("Enter a character: ")

result = "Number is {} and letter is {}".format(num, char)
print("Formatted string:", result)


# PART 2: Area of circular pond and water calculation
radius = float(input("\nEnter radius of pond: "))

pi = 3.14
area = pi * radius * radius
print("Area of pond:", int(area))

water = area * 1.4
print("Total water in pond:", int(water))


# PART 3: Speed calculation
distance = float(input("\nEnter distance in meters: "))
time = float(input("Enter time in minutes: "))

time_seconds = time * 60
speed = distance / time_seconds

print("Speed:", int(speed), "m/s")