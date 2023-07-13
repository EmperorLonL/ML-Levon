import matplotlib.pyplot as plt
import random

random.seed(50)


subject = ["Math", "Science", "History", "English", "Pyhsics", "Biology", "Geography", "Chemistry"]
grade = [80, 90, 75, 85, 92, 88, 82, 78]
color = ['red', 'blue', 'yellow', 'orange', 'pink', 'purple', 'green', 'black']

num = 0

for i in grade:
	num += i
average = num / len(grade)

print(f"The average is {average}")

plt.bar(subject, grade, color = color)

plt.xlabel("Subject")
plt.ylabel("Grade")
plt.title('Grades')
plt.show()

