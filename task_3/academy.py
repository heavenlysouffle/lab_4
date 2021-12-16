import sqlite3
from classes import LocalCourse, OffsiteCourse


class Academy:
    __db_location = "D:\\sqlite\\db\\python_courses.db"
    __id_course = 1

    def __init__(self):
        self.__connection = sqlite3.connect(Academy.__db_location)
        self.__cursor = self.__connection.cursor()

    def close(self):
        self.__connection.close()

    def commit(self, query):
        self.__cursor.execute(query)
        self.__connection.commit()

    # TODO: дописать sql операции
    def insert_local(self, course):
        if not isinstance(course, LocalCourse):
            raise TypeError
        self.commit(f"INSERT INTO Courses VALUES({self.__id_course}, \"{course.name}\", \"Local\");")
        for topic in course.program:
            self.commit(f"INSERT INTO Program VALUES({self.__id_course}, \"{topic}\")")
        for id_teacher in course.teachers:
            self.commit(f"INSERT INTO CoursesTeachers VALUES({self.__id_course}, \"{id_teacher}\")")
        self.__id_course += 1

# a = LocalCourse("foo", 4, "Python", "OOP")
# b = Academy()
# b.insert_local(a)
# b.close()