from abc import ABC, abstractmethod
from dataclasses import dataclass, field


class EducationFacility(ABC):
    """
    Abstract class for education facilities
    """
    @abstractmethod
    def enroll_person(self, person) -> None:
        """
        Enrolls a person in the education facility

        Args:
            person: person to enroll
        """
        pass

    @abstractmethod
    def graduate_person(self, person) -> None:
        """
        Graduates a person from the education facility

        Args:
            person: person to graduate
        """
        pass

    @abstractmethod
    def hire_teacher(self, teacher) -> None:
        """
        Hires a teacher in the education facility

        Args:
            teacher: person to hire
        """
        pass

    @abstractmethod
    def fire_teacher(self, teacher) -> None:
        """
        Fires a teacher from the education facility
        Args:
            teacher: person to fire
        """
        pass

    @abstractmethod
    def offer_course(self, course) -> None:
        """
        Offers a course in the education facility
        Args:
            course: course to offer
        """
        pass

    @abstractmethod
    def cancel_course(self, course) -> None:
        """
        Cancels a course in the education facility
        Args:
            course: course to cancel
        """
        pass


@dataclass(init=True, frozen=True, repr=True)
class Person(ABC):
    """
    Abstract class for people
    """
    name: str
    age: int


@dataclass(init=True, frozen=True, repr=True)
class Student(Person):
    """
    Student entity
    """
    specialization: str


@dataclass(init=True, frozen=True, repr=True)
class Teacher(Person):
    """
    Teacher entity
    """
    department: str


@dataclass(init=True, repr=True)
class Course:
    """
    Course entity
    """
    name: str
    teacher: Teacher
    _students: list[Student] = field(default_factory=list)

    @property
    def enrolled_students(self) -> list[Student]:
        """
        Gets the list of enrolled students

        Returns:
            list of enrolled students
        """
        return self._students

    def add_student(self, student: Student) -> None:
        """
        Adds a student to the course

        Args:
            student: student to add
        """
        self._students.append(student)

    def remove_student(self, student: Student) -> None:
        """
        Removes a student from the course

        Args:
            student: student to remove
        """
        self._students.remove(student)


@dataclass(init=True, repr=True)
class University(EducationFacility):
    """
    University entity
    """
    students: list[Student] = field(default_factory=list)
    teachers: list[Teacher] = field(default_factory=list)
    courses: list[Course] = field(default_factory=list)

    def enroll_person(self, student: Student) -> None:
        """
        Enrolls a student in the university

        Args:
            student: student to enroll
        """
        self.students.append(student)

    def graduate_person(self, student: Student) -> None:
        """
        Graduates a student from the university

        Args:
            student: student to graduate
        """
        self.students.remove(student)

    def hire_teacher(self, teacher: Teacher) -> None:
        """
        Hires a teacher in the university

        Args:
            teacher: teacher to hire
        """
        self.teachers.append(teacher)

    def fire_teacher(self, teacher: Teacher) -> None:
        """
        Fires a teacher from the university

        Args:
            teacher: teacher to fire
        """
        self.teachers.remove(teacher)

    def offer_course(self, course: Course) -> None:
        """
        Offers a course in the university

        Args:
            course: course to offer
        """
        self.courses.append(course)

    def cancel_course(self, course: Course) -> None:
        """
        Cancels a course in the university

        Args:
            course: course to cancel
        """
        self.courses.remove(course)


if __name__ == '__main__':
    university = University()
