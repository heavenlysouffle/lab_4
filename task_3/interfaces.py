from abc import ABC, abstractmethod


class ITeacher(ABC):
    """Interface implementing the teacher"""

    @property
    @abstractmethod
    def surname(self) -> str:
        """Returns the teacher's surname"""
        pass

    @surname.setter
    @abstractmethod
    def surname(self, surname: str) -> None:
        """Sets the teacher's surname"""
        pass

    @property
    @abstractmethod
    def name(self) -> str:
        """Returns the teacher's name"""
        pass

    @name.setter
    @abstractmethod
    def name(self, name: str) -> None:
        """Sets the teacher's name"""
        pass

    @property
    @abstractmethod
    def patronymic(self) -> str:
        """Returns the teacher's patronymic"""
        pass

    @patronymic.setter
    @abstractmethod
    def patronymic(self, patronymic: str) -> None:
        """Sets the teachers patronymic"""
        pass

    @property
    @abstractmethod
    def birth_date(self) -> str:
        """Returns the teacher's birth date"""
        pass

    @birth_date.setter
    @abstractmethod
    def birth_date(self, birth_date: str) -> None:
        """Sets the teacher's birth date"""
        pass

    @property
    @abstractmethod
    def courses(self) -> list:
        """Returns the list of the teacher's courses"""
        pass

    @abstractmethod
    def add_course(self, course) -> None:
        """Adds the course to the list of the teacher's courses"""
        pass

    @abstractmethod
    def remove_course(self, course) -> None:
        """Removes the course from the list of the teacher's courses"""
        pass


class ICourse(ABC):
    """Interface implementing the course"""

    @property
    @abstractmethod
    def name(self) -> str:
        """Returns the course's name"""
        pass

    @name.setter
    @abstractmethod
    def name(self, name: str) -> None:
        """Sets the course's name"""
        pass

    @property
    @abstractmethod
    def teachers(self) -> str:
        """Returns the list of course's teachers"""
        pass

    @property
    @abstractmethod
    def program(self) -> str:
        """Returns the course's program"""
        pass

    @abstractmethod
    def add_topic(self, *program: list[str]) -> None:
        """Add the topic(s) to the course's program"""
        pass

    @abstractmethod
    def remove_topic(self, *program: list[str]) -> None:
        """Remove the topic(s) from the course's program"""
        pass

    @abstractmethod
    def add_teacher(self, *teachers: list) -> None:
        """Adds the teacher(s) to the list of the course's teachers"""
        pass

    @abstractmethod
    def remove_teacher(self, *teachers: list) -> None:
        """Remove the teacher(s) from the list of the course's teachers"""
        pass


class ILocalCourse(ABC):
    """Interface implementing the local course"""

    @property
    @abstractmethod
    def room(self) -> int:
        """Returns the room number the course is held"""
        pass

    @room.setter
    @abstractmethod
    def room(self, room: int) -> None:
        """Sets the room number the course is held"""
        pass


class IOffsiteCourse(ABC):
    """Interface implementing the offsite course"""

    @property
    @abstractmethod
    def address(self) -> str:
        """Returns the address where course is held"""
        pass

    @address.setter
    @abstractmethod
    def address(self, address: str) -> None:
        """Sets the address where course is held"""
        pass


class ICourseFactory(ABC):
    """Interface implementing the course factory"""

    @staticmethod
    @abstractmethod
    def create_local(name: str, room: int, *program: list[str]):
        """Creates local course"""
        pass

    @staticmethod
    @abstractmethod
    def create_offsite(name: str, address: str, *program: list[str]):
        """Creates offsite course"""
        pass


class ITeacherFactory(ABC):
    """Interface implementing the teacher factory"""

    @staticmethod
    @abstractmethod
    def create_teacher(surname: str, name: str, patronymic: str, birth_date: str):
        """Creates teacher profile"""
        pass
