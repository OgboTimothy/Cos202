

print("===== CGPA CALCULATOR =====")

num_courses = int(input("Enter the number of courses: "))

total_grade_points = 0
total_course_units = 0

# Grade to Point Mapping
grade_points = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2,
    "E": 1,
    "F": 0
}

for i in range(1, num_courses + 1):
    print(f"\nCourse {i}")

    course_unit = int(input("Enter course unit: "))
    grade = input("Enter grade (A, B, C, D, E, F): ").upper()

    while grade not in grade_points:
        print("Invalid grade!")
        grade = input("Enter grade (A, B, C, D, E, F): ").upper()

    total_grade_points += course_unit * grade_points[grade]
    total_course_units += course_unit

cgpa = total_grade_points / total_course_units

print("\n===== RESULT =====")
print("Total Course Units:", total_course_units)
print("Total Grade Points:", total_grade_points)
print(f"CGPA: {cgpa:.2f}")
