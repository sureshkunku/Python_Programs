def find_best_average_grade(student_grades):
    if not student_grades:
        return None

    grades = {}
    for student, marks in student_grades:
        if student in grades:
            grades[student] = (grades[student] + int(marks)) / 2
        else:
            grades[student] = int(marks)
    best_student = None
    marks = 0
    for i, j in grades.items():
        if j > marks:
            best_student = i
            marks = j
    return [best_student, marks]


# Test the function
student_grades = [["Mark", "70"], ["Alex", "60"], ["Alex", "62"], ["Stephen", "75"]]
result = find_best_average_grade(student_grades)
print(result)
