import random
#Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

#randomizing who will pay for the dinner from the list created by the user
#Current code requires that a comma and space be used after each name
num_names = len(names)
who_pays = random.randint(0, num_names - 1)
person_who_will_pay = names[who_pays]
print(person_who_will_pay + " is going to buy the meal today!")