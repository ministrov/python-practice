""" Модуль для управления статистикой студентов """

from dataclasses import dataclass


@dataclass
class Student:
    name: str
    grade: float


@dataclass
class StudetsPepository:
    students: list[Student]

    def add_student(self, student: Student):
        self.students.append(student)

    def all_students(self):
        return self.students


@dataclass
class StudentsStats:
    pass


@dataclass
class PrintStudetInfo:
    pass
