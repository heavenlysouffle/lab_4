from classes import LocalCourse, OffsiteCourse, Teacher
from interfaces import ICourseFactory, ITeacherFactory


class CourseFactory(ICourseFactory):
    @staticmethod
    def create_local(name, room, *program):
        return LocalCourse(name, room, *program)

    @staticmethod
    def create_offsite(name, address, *program):
        return OffsiteCourse(name, address, *program)


class TeacherFactory(ITeacherFactory):
    @staticmethod
    def create_teacher(surname, name, patronymic, birth_date):
        return Teacher(surname, name, patronymic, birth_date)
