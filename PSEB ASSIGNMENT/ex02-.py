age = int(input("Enter your age: "))

if age >= 18:
    print(age, "Eligible to vote")
else:
    years_left = 18 - age
    print("Not eligible, wait", years_left, "more years")