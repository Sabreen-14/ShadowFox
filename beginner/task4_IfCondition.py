# ----------- TASK 4 -----------

# PART 1: BMI Calculator

height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kilograms: "))

bmi = weight / (height ** 2)

if bmi >= 30:
    print("Obesity")
elif bmi >= 25:
    print("Overweight")
elif bmi >= 18.5:
    print("Normal")
else:
    print("Underweight")


# PART 2: City to Country

Australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
UAE = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

city = input("\nEnter a city name: ").title()

if city in Australia:
    print(f"{city} is in Australia")
elif city in UAE:
    print(f"{city} is in UAE")
elif city in India:
    print(f"{city} is in India")
else:
    print("City not found")


# PART 3: Same Country Check

city1 = input("\nEnter first city: ").title()
city2 = input("Enter second city: ").title()

if (city1 in India and city2 in India):
    print("Both cities are in India")
elif (city1 in Australia and city2 in Australia):
    print("Both cities are in Australia")
elif (city1 in UAE and city2 in UAE):
    print("Both cities are in UAE")
else:
    print("They don't belong to the same country")