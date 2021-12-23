from classes import LocalCourse, OffsiteCourse, Teacher
from interfaces import ICourseFactory, ITeacherFactory


class CourseFactory(ICourseFactory):
    """Factory to create offsite and local courses"""

    @staticmethod
    def create_local(name: str, room: int, *program: list[str]) -> LocalCourse:
        """Returns created local course"""
        return LocalCourse(name, room, *program)

    @staticmethod
    def create_offsite(name: str, address: str, *program: list[str]) -> OffsiteCourse:
        """Returns created offsite course"""
        return OffsiteCourse(name, address, *program)


class TeacherFactory(ITeacherFactory):
    """Factory to create teacher profile"""

    @staticmethod
    def create_teacher(surname: str, name: str, patronymic: str, birth_date: str) -> Teacher:
        """Returns created Teacher profile"""
        return Teacher(surname, name, patronymic, birth_date)
