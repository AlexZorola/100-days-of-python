#Prompt the user to give their students scores, which will be used to generate a list
student_scores = input("Input a list of student scores: ").split(", ")

#Generate the list using a for loop from the user input
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

#Traverse the list and determine which was the highest score
highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score
print(f"The highest score in the classs is: {highest_score}")