from interfaces import ICourse, ILocalCourse, IOffsiteCourse


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
            if not isinstance(teacher, str):
                raise TypeError
            if not teacher:
                raise ValueError("No data")
            self.__teachers.append(teacher)

    def remove_teacher(self, *teachers):
        if len(self.teachers) <= 0:
            raise IndexError("The list of teachers is empty")
        for teacher in teachers:
            if not isinstance(teacher, str):
                raise TypeError
            if not teacher:
                raise ValueError("No data")
            self.__teachers.remove(teacher)


class LocalCourse(Course, ILocalCourse):
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


class OffsiteCourse(Course, IOffsiteCourse):
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
