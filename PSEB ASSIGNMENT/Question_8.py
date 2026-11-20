student = ("BSIT-12", "Sara", 88)

# Part 1: Unpacking
roll_no, name, marks = student

print(f"Roll Number: {roll_no}")
print(f"Name: {name}")
print(f"Marks: {marks}")

# Part 2: Error
# student[2] = 95

# Part 3: Convert tuple into list
student_list = list(student)

student_list[2] = 95

student = tuple(student_list)

print(student)
