"""
3. Talabalar baholari berilgan:

students = {
    "Aziz": {"Matematika": 4, "Fizika": 5, "Ingliz tili": 3},
    "Bekzod": {"Matematika": 5, "Fizika": 4, "Ingliz tili": 5},
    "Gulnoza": {"Matematika": 3, "Fizika": 4, "Ingliz tili": 4},
}
3.1 Eng yaxshi o'rtacha bahoga ega talabani aniqlang.
3.2 Har bir fan bo'yicha eng yuqori baho olgan talabani toping.
"""







#3.1 Eng yaxshi o'rtacha bahoga ega talabani aniqlang.

students = {
    "Aziz": {"Matematika": 4, "Fizika": 5, "Ingliz tili": 3},
    "Bekzod": {"Matematika": 5, "Fizika": 4, "Ingliz tili": 5},
    "Gulnoza": {"Matematika": 3, "Fizika": 4, "Ingliz tili": 4},
}

student_name = None
highest_average = 0

for student, subjects in students.items():
    avg_score = 0
    for grade in subjects.values():
        avg_score += grade
        
    avg_score = avg_score / len(subjects)
    if avg_score > highest_average:
        highest_average = avg_score
        student_name = student

print("\nStudent With Highest Average Grade")
print(f"Name: {student_name}\nGrade: {highest_average}\n" )


#------------------------------------------------------------------------------------


# 3.2 Har bir fan bo'yicha eng yuqori baho olgan talabani toping.

students = {
    "Aziz": {"Matematika": 4, "Fizika": 5, "Ingliz tili": 3},
    "Bekzod": {"Matematika": 5, "Fizika": 4, "Ingliz tili": 5},
    "Gulnoza": {"Matematika": 3, "Fizika": 4, "Ingliz tili": 4},
}



best_students = {}

for student, subjects in students.items():
    for subject, grade in subjects.items():
        if subject not in best_students or grade>best_students[subject][1]:
            best_students[subject] =(student,grade)

for subject, (name,grade) in best_students.items() :
    print(f"Highest score from {subject}.\nName: {name}\nGrade: {grade}\n")



    




    
    
        