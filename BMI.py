# Ask the user for their height and weight to be used towards the calculation of their BMI
height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

# Calulate the BMI
bmi = round(weight / (height * height))

# Return the results and inform the user of the state of their health.
if bmi <= 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi <= 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi <= 30:
    print(f"Your BMI {bmi}, you are slightly overweight.")
elif bmi <= 35:
    print(f"Your BMI is {bmi}, your are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")