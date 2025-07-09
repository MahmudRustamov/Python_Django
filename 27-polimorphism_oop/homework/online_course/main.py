from utils import Teacher, Course



def main():
    print("""
    1. Create a new teacher
    2. Create a course
    3. Register to course
    4. Delete a course
    5. Delete a teacher
    6. Get registered courses: phone_number
    7. Get users by course: course_name
    8. Show all courses
    9. Exit
    """)

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter teacher's name: ")
        phone_number = input("Phone number: ")
        experience = input("Experience: ")
        profession = input("Profession: ")
        age = input("Age: ")
        teacher = Teacher(name=name, phone_number=phone_number, experience=experience, profession=profession, age=age)
        teacher.add_teacher()

    elif choice == "2":
        name = input("Enter the course name: ")
        price = input("Price: ")
        teacher_phone_number = input("Phone number: ")
        course = Course(name=name, price=price, teacher_phone_number=teacher_phone_number)
        course.create_course()

    elif choice == "3":
        course = Course(name="", price="", teacher_phone_number="")
        course.register_course()

    elif choice == "4":
        course = Course(name="", price="", teacher_phone_number="")
        course.delete_course()

    elif choice == "5":
        teacher = Teacher(name="", phone_number="", experience="", profession="", age="")
        teacher.delete_teacher()

    elif choice == "6":
        course = Course(name="", price="", teacher_phone_number="")
        course.get_registered_courses()

    elif choice == "7":
        course = Course(name="", price="", teacher_phone_number="")
        course.get_users_by_course()
    elif choice == "8":
        course = Course(name="", price="", teacher_phone_number="")
        course.show_all_courses()
    elif choice == "9":
        print("Good Bye!!")
        return None
    else:
        print("Invalid choice!!!")
    return main()


if __name__ == "__main__":
    main()