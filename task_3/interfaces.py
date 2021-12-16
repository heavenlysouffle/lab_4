from abc import ABC, abstractmethod


class ICourse(ABC):
    @property
    @abstractmethod
    def name(self):
        pass

    @name.setter
    @abstractmethod
    def name(self, name):
        pass

    @property
    @abstractmethod
    def teachers(self):
        pass

    @property
    @abstractmethod
    def program(self):
        pass

    @abstractmethod
    def add_topic(self):
        pass

    @abstractmethod
    def remove_topic(self):
        pass

    @abstractmethod
    def add_teacher(self):
        pass

    @abstractmethod
    def remove_teacher(self):
        pass


class ILocalCourse(ABC):
    @property
    @abstractmethod
    def room(self):
        pass

    @room.setter
    @abstractmethod
    def room(self, room):
        pass


class IOffsiteCourse(ABC):
    @property
    @abstractmethod
    def address(self):
        pass

    @address.setter
    @abstractmethod
    def address(self, address):
        pass


class ICourseFactory(ABC):
    @staticmethod
    @abstractmethod
    def create_local(name, room, *program):
        pass

    @staticmethod
    @abstractmethod
    def create_offsite(name, address, *program):
        pass
