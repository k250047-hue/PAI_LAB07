import numpy as np

marks = np.array([
    [78, 85, 90, 67, 88],
    [45, 55, 60, 50, 48],
    [90, 92, 85, 88, 95],
    [30, 40, 35, 45, 38],
    [65, 70, 75, 80, 72],
    [50, 55, 60, 65, 70],
    [88, 82, 91, 85, 89],
    [40, 45, 48, 42, 50],
    [72, 68, 75, 70, 80],
    [95, 90, 93, 96, 92]
])

student_total = np.sum(marks, axis=1)
student_average = np.mean(marks, axis=1)

subject_average = np.mean(marks, axis=0)

highest_student = np.argmax(student_average) + 1

passed_students = np.sum(student_average >= 50)

result = np.where(student_average >= 50, "Pass", "Fail")

print("Marks of Students:")
print(marks)

print("\nTotal Marks of Each Student:")
print(student_total)

print("\nAverage Marks of Each Student:")
print(student_average)

print("\nAverage Marks of Each Subject:")
print(subject_average)

print("\nStudent with Highest Average:", highest_student)

print("Number of Students with Average >= 50:", passed_students)

print("\nPass/Fail Result:")
print(result)