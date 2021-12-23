import sys
from academy import Academy
from factories import CourseFactory, TeacherFactory

if __name__ == '__main__':
    academy = Academy()
    while True:
        print("\t\t___Software Academy___"
              "\n\t\t\tMenu"
              "\n\t1. Insert new local course"
              "\n\t2. Insert new offsite course"
              "\n\t3. Display all courses"
              "\n\t4. Display all local courses"
              "\n\t5. Display all offsite courses"
              "\n\t6. Find course by ID"
              "\n\t7. Display all teachers"
              "\n\t8. Find teacher by ID"
              "\n\t9. Display courses taught by the teacher"
              "\n\t10. Display teachers of the course"
              "\n\t11. Display program of the course"
              "\n\t12. Display topics studied at the Software Academy"
              "\n\t13. Display academy rooms"
              "\n\t14. Add room (only for administrator)"
              "\n\t15. Add teacher (only for administrator)"
              "\n\t16. Clear Academy database (only for administrator)"
              "\n\n\tEnter 0 to exit\n")
        try:
            choice = int(input("Enter number of the option: "))
            if not choice:
                print("Thank you! See you later")
                academy.close()
                sys.exit()
            elif choice == 1 or choice == 2:
                course_name = input("Enter name of the course: ")
                course_program = ' '.join(input("Enter topics studied within the course through , : ").split())
                course_program = course_program.split(',')
                teachers_num = int(input("Enter number of teachers to teach it: "))
                if teachers_num < 0:
                    raise ValueError("Number of teachers cannot be less than 0")
                if choice == 1:
                    room = int(input("Enter number of the room where the course is taught: "))
                    course = CourseFactory.create_local(course_name, room, *course_program)
                    for i in range(0, teachers_num):
                        surname = input("Enter teacher's surname: ")
                        name = input("\tname: ")
                        patronymic = input("\tpatronymic: ")
                        birth_date = input("\tbirth date: ")
                        course.add_teacher(TeacherFactory.create_teacher(surname, name, patronymic, birth_date))
                    academy.insert_local(course)
                else:
                    address = input("Please enter the address where the course is taught")
                    course = CourseFactory.create_offsite(course_name, address, *course_program)
                    for i in range(0, teachers_num):
                        surname = input("Enter teacher's surname: ")
                        name = input("\tname: ")
                        patronymic = input("\tpatronymic: ")
                        birth_date = input("\tbirth date: ")
                        course.add_teacher(TeacherFactory.create_teacher(surname, name, patronymic, birth_date))
                    academy.insert_local(course)
            elif choice == 3:
                print(academy.get_all_courses_str())
            elif choice == 4:
                print(academy.get_all_local_str())
            elif choice == 5:
                print(academy.get_all_offsite_str())
            elif choice == 6 or choice == 10 or choice == 11:
                id_course = int(input("Enter ID of the course: "))
                if choice == 6:
                    print(academy.get_course_str(id_course))
                elif choice == 10:
                    print(academy.get_course_teachers_str(id_course))
                else:
                    print(academy.get_program_str(id_course))
            elif choice == 7:
                print(academy.get_all_teachers_str())
            elif choice == 8 or choice == 9:
                id_teacher = int(input("Enter ID of the teacher: "))
                if choice == 8:
                    print(academy.get_teacher_str(id_teacher))
                else:
                    print(academy.get_teacher_courses_str(id_teacher))
            elif choice == 12:
                print(academy.get_topics_str())
            elif choice == 13:
                print(academy.get_rooms_str())
            elif choice == 14 or choice == 15 or choice == 16:
                password = input("Enter password to do it: ")
                if not Academy.password_match(password):
                    print("Wrong password. Access blocked\n")
                else:
                    if choice == 14:
                        room = int(input("Enter number of the room: "))
                        academy.add_room(room)
                    if choice == 15:
                        surname = input("Enter teacher's surname: ")
                        name = input("\tname: ")
                        patronymic = input("\tpatronymic: ")
                        birth_date = input("\tbirth date")
                        academy.add_teacher(TeacherFactory.create_teacher(surname, name, patronymic, birth_date))
                    if choice == 16:
                        academy.clear_all()
            else:
                print("Unexpected number. Please enter number from the list")
            input("Press something to continue...\n")
        except Exception as err:
            print(f"Oops, caught an error! {err}\n")
