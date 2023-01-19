# Ask the user to choose a year they'd like to know if it was a leap year.
year = int(input("Which year do you want to check? "))

# Calculate if the year is a leap year.
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap Year!")
        else:
            print("Not a Leap Year!")
    else:
        print("Leap Year!")
else:
    print("Not a Leap Year!")