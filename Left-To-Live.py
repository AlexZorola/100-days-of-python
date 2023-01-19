# Ask the user for their current age.
age = input("What is your current age?")

# Calculate how long they have left to live based on an average life span (90).
years = 90 - int(age)
months = round(years * 12)
weeks = round(years * 52)
days = round(years * 365)

# Print out the remaining time the user has left to live!
print(f"You have {days} days, {weeks} weeks, and {months} months left...tread carefully!")