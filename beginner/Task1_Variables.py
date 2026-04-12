# ----------- TASK 1: VARIABLES (WITH USER INPUT) -----------

# PART 1: Value of PI
pi = 22 / 7
print("Value of pi:", pi)
print("Datatype of pi:", type(pi))


# PART 2: Reserved Keyword Test



for_value = int(input("\nEnter a value for variable: "))
print("Valid variable (for_value):", for_value)


# PART 3: Simple Interest

principal = float(input("\nEnter principal amount: "))
rate = float(input("Enter rate of interest: "))
time = float(input("Enter time (in years): "))

simple_interest = (principal * rate * time) / 100

print("Simple Interest:", simple_interest)
