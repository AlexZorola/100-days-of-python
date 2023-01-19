#Prompt the user for the heights of their students
student_heights = input("Input a list of students heights: ").split(", ")

#Generate a list based on the information provided by the user
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

#Calculate the total height of the students from the previously generated list
total_height = 0
for height in student_heights:
    total_height += height

#Calculate the total number of students from the previously generated list
number_of_students = 0
for student in student_heights:
    number_of_students += 1

#Calculate the average height based on the total height and total number of students
average_height = round(total_height / number_of_students)
print(average_height)