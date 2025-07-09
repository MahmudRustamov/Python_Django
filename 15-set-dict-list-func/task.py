def absent_students(students_attendance: list, id: str):
    absent = 0
    ls = ""
    for leaner in students_attendance:
        if id == leaner['student'][absent]['student_id']:
            if leaner['student'][absent]['absent'] == True:
                ls += f"{leaner['date']} sanada {leaner['student'][absent]["name"]} talaba kelmagan\n"

        absent += 1
    return ls




attendance = [
    {
        "date": "10-10-2025",
        "lesson": "python",
        "student": [
            {
                "student_id": "007",
                "name": "Mahmud",
                "absent": True
            },
            {
                "student_id": "006",
                "name": "Ozodbek",
                "absent": True
            }, 
            {
                "student_id": "008",
                "name": "Olim",
                "absent": False
            }
        ]
    }, 
    {
        "date": "11-10-2025",
        "lesson": "web",
        "student": [
            {
                "student_id": "007",
                "name": "Mahmud",
                "absent": True
            },
            {
                "student_id": "006",
                "name": "Ozodbek",
                "absent": False
            }, 
            {
                "student_id": "006",
                "name": "Olim",
                "absent": False
            }
        ]
    },
    {
        "date": "12-10-2025",
        "lesson": "java",
        "student": [
            {
                "student_id": "007",
                "name": "Mahmud",
                "absent": False
            },
            {
                "student_id": "006",
                "name": "Ozodbek",
                "absent": True
            }, 
            {
                "student_id": "006",
                "name": "Olim",
                "absent": True
            }
        ]
    }
]

st_id = input("Enter your id: ")

print(absent_students(attendance, st_id))