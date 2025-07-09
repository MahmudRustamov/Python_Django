from file_manager import FileManager

class Student:
    def __init__(self, name, email, phone_number, course_name):
        self.students_manager = FileManager("students")
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.course_name = course_name


    def get_next_id(self):
        students = self.students_manager.read()
        if students:
            last_student = students[-1]
            return last_student["student_id"] + 1
        else:
            return 1


    def add_student(self):
        students = self.students_manager.read()
        data = {
            "name": self.name,
            "email": self.email,
            "phone_number": self.phone_number,
            "course_name": self.course_name,
            "student_id": self.get_next_id()
        }
        students.append(data)
        self.students_manager.write(students)


class Teacher:
    def __init__(self, name, phone_number, experience, profession, age):
        self.teachers_manager = FileManager("teachers")
        self.name = name
        self.phone_number = phone_number
        self.experience = experience
        self.profession = profession
        self.age = age


    def add_teacher(self):
        teachers = self.teachers_manager.read()
        data = {
            "name": self.name,
            "phone_number": self.phone_number,
            "experience": self.experience,
            "profession": self.profession,
            "age": self.age
        }
        teachers.append(data)
        self.teachers_manager.write(teachers)
        print("New teacher is added!!!!")


    def delete_teacher(self):
        teachers = self.teachers_manager.read()
        phone_number = input("Enter teacher's phone number: ").strip()
        is_found = False
        for index, teacher in enumerate(teachers):
            if teacher["phone_number"].strip() == phone_number:
                teachers.pop(index)
                is_found = True
                break

        if is_found:
            self.teachers_manager.write(teachers)
            print("Teacher is deleted successfully!!")
        else:
            print("Teacher is not found!!!")


class Course:
    def __init__(self, name, price, teacher_phone_number):
        self.course_manager = FileManager("courses")
        self.teacher_info = FileManager("teachers")
        self.name = name
        self.price = price
        self.student_data = FileManager("students")
        self.teacher_phone_number = teacher_phone_number


    def get_teacher(self):
        teachers = self.teacher_info.read()
        for teacher in teachers:
            if teacher["phone_number"].strip() == self.teacher_phone_number:
                return teacher
        return None


    def create_course(self):
        courses = self.course_manager.read()
        if self.get_teacher():
            data = {
                "name": self.name,
                "price": self.price,
                "teacher": self.get_teacher()
            }
            courses.append(data)
            self.course_manager.write(courses)
            print("New course is added!!!")
        else:
            print("Teacher is not found!!!")


    def register_course(self):
        self.show_all_courses()
        option = input("Which course would you like to register for: ").strip().lower()
        courses = self.course_manager.read()
        if courses:
            is_found = False
            for course in courses:
                if course["name"].lower() == option:
                    is_found = True
                    break

            if is_found:
                name = input("Student's name: ")
                email = input("Enter email: ")
                phone_number = input("Enter phone number: ")
                student = Student(name=name,email=email, phone_number=phone_number,course_name=option)
                student.add_student()
                print("Student is registered!!!")
            else:
                print("Course is not found!!!!")
        else:
            print("Courses are not available!!")


    def delete_course(self):
        name = input("Enter the course name: ")
        courses = self.course_manager.read()
        is_found = False
        for index, course in enumerate(courses):
            if course["name"] == name:
                courses.pop(index)
                is_found = True
                break

        if is_found:
            self.course_manager.write(courses)
            print("Course is deleted successfully!!!")
        else:
            print("Course name is not found!!!")


    def get_users_by_course(self):
        students = self.student_data.read()
        if students:
            course_name = input("Enter the course name: ").lower().strip()
            for student in students:
                if student["course_name"].strip().lower() == course_name:
                    print(f"ID: {student["student_id"]}  Student's name: {student["name"]}  Email: {student["email"]}  Phone Number: {student["email"]}  Course Name: {student["course_name"]}")
        else:
            print("Students not found!!!")


    def get_registered_courses(self):
        students = self.student_data.read()
        if students:
            phone_number = input("Phone number: ").lower().strip()
            for student in students:
                if student["phone_number"].strip().lower() == phone_number:
                    print(f"ID: {student["student_id"]}  Student's name: {student["name"]}  Email: {student["email"]}  Phone Number: {student["email"]}  Course Name: {student["course_name"]}")
        else:
            print("Students not found!!!")


    def show_all_courses(self):
        courses = self.course_manager.read()
        if courses:
            for course in courses:
                print(f"Course: {course["name"]}  Price: {course["price"]}  Teacher: {course["teacher"]["name"]}  Experience: {course["teacher"]["experience"]}")







