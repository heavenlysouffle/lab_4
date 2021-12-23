import re
from interfaces import ICourse, ILocalCourse, IOffsiteCourse, ITeacher


def full_name_dec(func):
    def wrapper(self, full_name):
        if not (isinstance(full_name, str) and re.fullmatch('[A-Z][a-z]*(-[A-Z]?[a-z]+)?', full_name)):
            raise TypeError
        if not full_name:
            raise ValueError("No data")
        return func(self, full_name)
    return wrapper


class Teacher(ITeacher):
    def __init__(self, surname, name, patronymic, birth_date):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.birth_date = birth_date
        self.__courses = []

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    @full_name_dec
    def surname(self, surname):
        self.__surname = surname

    @property
    def name(self):
        return self.__name

    @name.setter
    @full_name_dec
    def name(self, name):
        self.__name = name

    @property
    def patronymic(self):
        return self.__patronymic

    @patronymic.setter
    @full_name_dec
    def patronymic(self, patronymic):
        self.__patronymic = patronymic

    @property
    def birth_date(self):
        return self.__birth_date

    @birth_date.setter
    def birth_date(self, birth_date):
        if not (isinstance(birth_date, str) and
                re.fullmatch('(19|20)[0-9]{2}-(([1-9]|1[0-2])|0[1-9])-(([1-9]|2[0-9])|3[0-1]|0[1-9])', birth_date)):
            raise TypeError
        if not birth_date:
            raise ValueError("No data")
        self.__birth_date = birth_date

    @property
    def courses(self):
        return self.__courses

    def add_course(self, course):
        if not isinstance(course, (LocalCourse, OffsiteCourse)):
            raise TypeError
        self.__courses.append(course)

    def remove_course(self, course):
        if len(self.__courses) <= 0:
            raise IndexError("The list of courses is empty")
        if not isinstance(course, (LocalCourse, OffsiteCourse)):
            raise TypeError
        self.__courses.remove(course)

    def courses_str(self):
        result = self.__str__() + ' teaches '
        if len(self.courses) == 0:
            result += 'nothing at the moment'
        for course in self.courses:
            result += f'{course}, '
        return result

    def __str__(self):
        result = f'{self.surname} {self.name} {self.patronymic} ({self.birth_date})'
        return result


class Course(ICourse):
    def __init__(self, name, *program):
        self.name = name
        self.__program = []
        self.__teachers = []
        self.add_topic(*program)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError
        if not name:
            raise ValueError("No data")
        self.__name = name

    @property
    def program(self):
        return self.__program

    @property
    def teachers(self):
        return self.__teachers

    def add_topic(self, *program):
        for topic in program:
            if not isinstance(topic, str):
                raise TypeError
            if not topic:
                raise ValueError("No data")
            self.__program.append(topic)

    def remove_topic(self, *program):
        if len(self.program) <= 0:
            raise IndexError("The program is empty")
        for topic in program:
            if not isinstance(topic, str):
                raise TypeError
            if not topic:
                raise ValueError("No data")
            self.__program.remove(topic)

    def add_teacher(self, *teachers):
        for teacher in teachers:
            if not isinstance(teacher, Teacher):
                raise TypeError
            if not teacher:
                raise ValueError("No data")
            self.__teachers.append(teacher)
            teacher.add_course(self)

    def remove_teacher(self, *teachers):
        if len(self.teachers) <= 0:
            raise IndexError("The list of teachers is empty")
        for teacher in teachers:
            if not isinstance(teacher, Teacher):
                raise TypeError
            if not teacher:
                raise ValueError("No data")
            self.__teachers.remove(teacher)
            teacher.remove_course(self)

    def __str__(self):
        result = f'{self.name}\nProgram: '
        if len(self.program) == 0:
            result += "nothing here yet"
        for topic in self.program:
            result += f'#{topic} '
        result += "\nTeachers: "
        if len(self.teachers) == 0:
            result += "no one here yet"
        for teacher in self.teachers:
            result += f'{teacher} | '
        return result + '\n'


class LocalCourse(Course, ICourse, ILocalCourse):
    def __init__(self, name, room, *program):
        super().__init__(name, *program)
        self.room = room

    @property
    def room(self):
        return self.__room

    @room.setter
    def room(self, room):
        if not isinstance(room, int):
            raise TypeError
        if room <= 0:
            raise ValueError("Number of room must above 0")
        self.__room = room

    def __str__(self):
        return f'Local course (room {self.room}) {super().__str__()}'


class OffsiteCourse(Course, ICourse, IOffsiteCourse):
    def __init__(self, name, address, *program):
        super().__init__(name, *program)
        self.address = address

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address):
        if not isinstance(address, str):
            raise TypeError
        if not address:
            raise ValueError("No data")
        self.__address = address

    def __str__(self):
        return f'Offsite course (room {self.address}) {super().__str__()}'
