import sqlite3
from classes import LocalCourse, OffsiteCourse, Teacher


def get_courses_dec(func):
    def wrapper(self):
        courses = func(self)
        result = ""
        for course in courses:
            result += self.get_course_str(course['id_course']) + '\n'
        return result

    return wrapper


def check_dec(func):
    def wrapper(self, value):
        if not isinstance(value, int):
            raise TypeError
        if value <= 0:
            raise ValueError("Teacher ID, Course ID or room number must be integer and above 0")
        return func(self, value)

    return wrapper


class Academy:
    __db_location = "D:\\sqlite\\db\\python_courses.db"
    __password = "admin"
    __id_course = 1

    def __init__(self):
        self.__connection = sqlite3.connect(Academy.__db_location)
        self.__connection.row_factory = self.dict_factory
        self.__cursor = self.__connection.cursor()

    def close(self):
        self.__connection.close()

    def commit(self, queries):
        self.__cursor.executescript(queries)
        self.__connection.commit()

    def fetchall(self, queries):
        self.__cursor.execute(queries)
        return self.__cursor.fetchall()

    def fetchone(self, query):
        self.__cursor.execute(query)
        return self.__cursor.fetchone()

    @property
    def id_course(self):
        return Academy.__id_course

    @staticmethod
    def dict_factory(cursor, row):
        dictionary = {}
        for ind, col_name in enumerate(cursor.description):
            dictionary[col_name[0]] = row[ind]
        return dictionary

    @staticmethod
    def password_match(password):
        if password == Academy.__password:
            return True
        return False

    def clear_all(self):
        self.commit("DELETE FROM Courses;"
                    "DELETE FROM LocalCourses;"
                    "DELETE FROM OffsiteCourses;"
                    "DELETE FROM CoursesTeachers;"
                    "DELETE FROM Program;"
                    "DELETE FROM Rooms;"
                    "DELETE FROM Teachers;"
                    "DELETE FROM Topics;")

    def __insert(self, course):
        for topic in course.program:
            self.commit(f"INSERT OR IGNORE INTO Program VALUES({self.__id_course}, \"{topic}\"); \
                        INSERT OR IGNORE INTO Topics VALUES(\"{topic}\");")
        for teacher in course.teachers:
            self.add_teacher(teacher)
            self.commit(f"INSERT OR IGNORE INTO CoursesTeachers VALUES({self.__id_course}, \
                        (SELECT id_teacher FROM Teachers WHERE surname == \"{teacher.surname}\" AND \
                        name == \"{teacher.name}\" AND patronymic == \"{teacher.patronymic}\" AND \
                        birth_date == \"{teacher.birth_date}\"));")
        self.__id_course += 1

    def insert_local(self, course):
        while self.fetchone(f'SELECT id_course FROM Courses WHERE id_course == {self.__id_course}'):
            self.__id_course += 1
        if not isinstance(course, LocalCourse):
            raise TypeError
        room = course.room
        self.commit(f"INSERT INTO Courses VALUES({self.__id_course}); \
                    INSERT OR IGNORE INTO LocalCourses VALUES({self.__id_course}, \"{course.name}\", \
                    CASE WHEN {room} IN (SELECT * FROM Rooms) THEN {room} END);")
        self.__insert(course)

    def insert_offsite(self, course):
        while self.fetchone(f'SELECT id_course FROM Courses WHERE id_course == {self.__id_course}'):
            self.__id_course += 1
        if not isinstance(course, OffsiteCourse):
            raise TypeError
        self.commit(f"INSERT INTO Courses VALUES({self.__id_course}); \
                    INSERT OR IGNORE INTO OffsiteCourses VALUES({self.__id_course}, \"{course.name}\", \
                                                                                            \"{course.address}\");")
        self.__insert(course)

    def get_all_courses(self):
        return {'Local': self.get_all_local(), 'Offsite': self.get_all_offsite()}

    def get_all_courses_str(self):
        result = Academy.get_all_local_str(self)
        result += Academy.get_all_offsite_str(self)
        return result

    def get_all_local(self):
        return self.fetchall("SELECT * FROM LocalCourses")

    @get_courses_dec
    def get_all_local_str(self):
        return self.get_all_local()

    def get_all_offsite(self):
        return self.fetchall("SELECT * FROM OffsiteCourses")

    @get_courses_dec
    def get_all_offsite_str(self):
        return self.get_all_offsite()

    @check_dec
    def get_course(self, id_course):
        local = self.fetchone(f"SELECT * FROM LocalCourses WHERE id_course == {id_course}")
        if local:
            return local
        offsite = self.fetchone(f"SELECT * FROM OffsiteCourses WHERE id_course == {id_course}")
        if offsite:
            return offsite
        # TODO: приём None в приложении

    def get_course_str(self, id_course):
        course = Academy.get_course(self, id_course)
        result = f"{course['id_course']} |\n\"{course['name']}\" "
        if 'room' in course.keys():
            result += f"- local course\nRoom: {course['room']}\n"
        if 'address' in course.keys():
            result += f"- offsite course\nAddress: {course['address']}\n"
        result += "Teachers: " + Academy.get_course_teachers_str(self, id_course)
        result += "Program: " + Academy.get_program_str(self, id_course)
        return result

    def get_all_teachers(self):
        return self.fetchall("SELECT * FROM Teachers")

    def get_all_teachers_str(self):
        result = ""
        for teacher in self.get_all_teachers():
            result += Academy.get_teacher_str(self, teacher['id_teacher']) + '\n'
        return result

    @check_dec
    def get_teacher(self, id_teacher):
        return self.fetchone(f"SELECT * FROM Teachers WHERE id_teacher == {id_teacher}")

    @check_dec
    def get_teacher_str(self, id_teacher):
        teacher = Academy.get_teacher(self, id_teacher)
        return f"{teacher['surname']} {teacher['name']} {teacher['patronymic']} ({teacher['birth_date']})"

    @check_dec
    def get_teacher_courses(self, id_teacher):
        return self.fetchall(f"SELECT id_course FROM CoursesTeachers WHERE id_teacher == {id_teacher}")

    @check_dec
    def get_teacher_courses_str(self, id_teacher):
        result = ""
        for course in Academy.get_teacher_courses(self, id_teacher):
            result += self.get_course_str(course['id_course']) + '\n'
        return result

    @check_dec
    def get_course_teachers(self, id_course):
        return self.fetchall(f"SELECT id_teacher FROM CoursesTeachers WHERE id_course == {id_course}")

    @check_dec
    def get_course_teachers_str(self, id_course):
        teachers = Academy.get_course_teachers(self, id_course)
        result = ""
        for teacher in teachers:
            result += Academy.get_teacher_str(self, teacher['id_teacher']) + '\n'
        return result

    def get_topics(self):
        return self.fetchall("SELECT * FROM Topics")

    def get_topics_str(self):
        result = ""
        for topic in self.get_topics():
            result += '#' + topic['id_topic'] + ' '
        return result

    def get_rooms(self):
        return self.fetchall("SELECT * FROM Rooms")

    def get_rooms_str(self):
        result = ""
        for room in self.get_rooms():
            result += '№' + room + ' '
        return result

    @check_dec
    def add_room(self, id_room):
        self.commit(f"INSERT INTO Rooms VALUES({id_room})")

    @check_dec
    def get_program(self, id_course):
        return self.fetchall(f"SELECT id_topic FROM Program WHERE id_course == {id_course}")

    @check_dec
    def get_program_str(self, id_course):
        program = Academy.get_program(self, id_course)
        result = ""
        for topic in program:
            result += '#' + topic['id_topic'] + ' '
        return result

    def add_teacher(self, teacher):
        if not isinstance(teacher, Teacher):
            raise TypeError
        if not teacher:
            raise ValueError("No data")
        self.commit(f"INSERT OR IGNORE INTO Teachers(surname, name, patronymic, birth_date) \
                        VALUES(\"{teacher.surname}\", \"{teacher.name}\", \"{teacher.patronymic}\", \
                        \"{teacher. birth_date}\")")
