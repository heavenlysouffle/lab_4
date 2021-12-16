from classes import LocalCourse, OffsiteCourse
from interfaces import ICourseFactory


class CourseFactory(ICourseFactory):
    @staticmethod
    def create_local(name, room, *program):
        return LocalCourse(name, room, *program)

    @staticmethod
    def create_offsite(name, address, *program):
        return OffsiteCourse(name, address, *program)
