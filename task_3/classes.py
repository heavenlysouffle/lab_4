import re
from interfaces import ICourse, ILocalCourse, IOffsiteCourse, ITeacher


def full_name_dec(func):
    """Decorator to check whether input of surname, name and patronymic is valid"""
    def wrapper(self, full_name):
        if not (isinstance(full_name, str) and re.fullmatch('[A-Z][a-z]*(-[A-Z]?[a-z]+)?', full_name)):
            raise TypeError
        if not full_name:
            raise ValueError("No data")
        return func(self, full_name)
    return wrapper


class Teacher(ITeacher):
    """Class that implements teacher's profile"""

    def __init__(self, surname: str, name: str, patronymic: str, birth_date: str):
        """Constructs Teacher

        Initializes Teacher with surname, name, patronymic and birth date"""
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.birth_date = birth_date
        self.__courses = []

    @property
    def surname(self) -> str:
        """Returns the teacher's surname"""
        return self.__surname

    @surname.setter
    @full_name_dec
    def surname(self, surname: str) -> None:
        """Sets the teacher's surname"""
        self.__surname = surname

    @property
    def name(self) -> str:
        """Returns the teacher's name"""
        return self.__name

    @name.setter
    @full_name_dec
    def name(self, name: str) -> None:
        """Sets the teacher's name"""
        self.__name = name

    @property
    def patronymic(self) -> str:
        """Returns the teacher's patronymic"""
        return self.__patronymic

    @patronymic.setter
    @full_name_dec
    def patronymic(self, patronymic: str) -> None:
        """Sets the teachers patronymic"""
        self.__patronymic = patronymic

    @property
    def birth_date(self) -> str:
        """Returns the teacher's birth date"""
        return self.__birth_date

    @birth_date.setter
    def birth_date(self, birth_date: str) -> None:
        """Sets the teacher's birth date"""
        if not (isinstance(birth_date, str) and
                re.fullmatch('(19|20)[0-9]{2}-(([1-9]|1[0-2])|0[1-9])-(([1-9]|2[0-9])|3[0-1]|0[1-9])', birth_date)):
            raise TypeError
        if not birth_date:
            raise ValueError("No data")
        self.__birth_date = birth_date

    @property
    def courses(self) -> list:
        """Returns the list of the teacher's courses"""
        return self.__courses

    def add_course(self, course) -> None:
        """Adds the course to the list of the teacher's courses"""
        if not isinstance(course, (LocalCourse, OffsiteCourse)):
            raise TypeError
        self.__courses.append(course)

    def remove_course(self, course) -> None:
        """Removes the course from the list of the teacher's courses"""
        if len(self.__courses) <= 0:
            raise IndexError("The list of courses is empty")
        if not isinstance(course, (LocalCourse, OffsiteCourse)):
            raise TypeError
        self.__courses.remove(course)

    def courses_str(self) -> str:
        """Returns the teacher's courses as string"""
        result = self.__str__() + ' teaches '
        if len(self.courses) == 0:
            result += 'nothing at the moment'
        for course in self.courses:
            result += f'{course}, '
        return result

    def __str__(self):
        """Returns string of a Teacher object

        Returns string as
        Surname Name Patronymic (birth_date)"""
        result = f'{self.surname} {self.name} {self.patronymic} ({self.birth_date})'
        return result


class Course(ICourse):
    """Class that implements course"""

    def __init__(self, name, *program):
        """Constructs Course

        Initializes Course with name and tuple of topics studied within it"""
        self.name = name
        self.__program = []
        self.__teachers = []
        self.add_topic(*program)

    @property
    def name(self) -> str:
        """Returns the course's name"""
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        """Sets the course's name"""
        if not isinstance(name, str):
            raise TypeError
        if not name:
            raise ValueError("No data")
        self.__name = name

    @property
    def program(self) -> list[str]:
        """Returns the course's program"""
        return self.__program

    @property
    def teachers(self) -> list[Teacher]:
        """Returns the list of course's teachers"""
        return self.__teachers

    def add_topic(self, *program: list[str]) -> None:
        """Add the topic(s) to the course's program"""
        for topic in program:
            if not isinstance(topic, str):
                raise TypeError
            if not topic:
                raise ValueError("No data")
            self.__program.append(topic)

    def remove_topic(self, *program: list[str]) -> None:
        """Remove the topic(s) from the course's program"""
        if len(self.program) <= 0:
            raise IndexError("The program is empty")
        for topic in program:
            if not isinstance(topic, str):
                raise TypeError
            if not topic:
                raise ValueError("No data")
            self.__program.remove(topic)

    def add_teacher(self, *teachers: list[Teacher]) -> None:
        """Adds the teacher(s) to the list of the course's teachers"""
        for teacher in teachers:
            if not isinstance(teacher, Teacher):
                raise TypeError
            if not teacher:
                raise ValueError("No data")
            self.__teachers.append(teacher)
            teacher.add_course(self)

    def remove_teacher(self, *teachers: list[Teacher]) -> None:
        """Remove the teacher(s) from the list of the course's teachers"""
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
        """Returns string of a Course object

        Returns string as
        Name
        Program: ...
        Teachers: ..."""
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
    """Class that implements local course"""

    def __init__(self, name: str, room: int, *program: list[str]):
        """Constructs LocalCourse

        Initializes LocalCourse with name, room and tuple of topics studied within it"""
        super().__init__(name, *program)
        self.room = room

    @property
    def room(self) -> int:
        """Returns the room number the course is held"""
        return self.__room

    @room.setter
    def room(self, room: int) -> None:
        """Sets the room number the course is held"""
        if not isinstance(room, int):
            raise TypeError
        if room <= 0:
            raise ValueError("Number of room must above 0")
        self.__room = room

    def __str__(self):
        """Returns string of a LocalCourse object

        Returns string  as
        Local course (room Room) Name
        Program: ...
        Teachers: ..."""
        return f'Local course (room {self.room}) {super().__str__()}'


class OffsiteCourse(Course, ICourse, IOffsiteCourse):
    """Class that implements offsite course"""

    def __init__(self, name: str, address: str, *program: list[str]):
        """Constructor of OffsiteCourse

        Initializes OffsiteCourse with name, address and tuple of topics studied within it"""
        super().__init__(name, *program)
        self.address = address

    @property
    def address(self) -> str:
        """Returns the address where course is held"""
        return self.__address

    @address.setter
    def address(self, address: str) -> None:
        """Sets the address where course is held"""
        if not isinstance(address, str):
            raise TypeError
        if not address:
            raise ValueError("No data")
        self.__address = address

    def __str__(self):
        """Returns string of a OffsiteCourse object

        Returns string as
        Offsite course (address) Name
        Program: ...
        Teachers: ..."""
        return f'Offsite course ({self.address}) {super().__str__()}'
