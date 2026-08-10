""" Модуль для управления статистикой студентов """

from dataclasses import dataclass


@dataclass
class Student:
    name: str
    score: int


@dataclass
class StudentRepository:
    students: list[Student]

    def add(self, student: Student):
        self.students.append(student)

    def all_students(self) -> list[Student]:
        return self.students


@dataclass
class StatisticsRepository:
    repository: StudentRepository

    def get_average_score(self) -> float:
        students = self.repository.all_students()
        if not students:
            return 0
        total = sum(s.score for s in students)
        return total / len(students)

    def get_best_student(self) -> Student:
        students = self.repository.all_students()
        return max(students, key=lambda s: s.score)


@dataclass
class ReportStudentInfo:
    repository: StudentRepository
    stats_service: StatisticsRepository

    def print_report(self):
        print("Отчет по студентам")
        for s in self.repository.all_students():
            print(f"{s.name}: {s.score}")
        print(f"Средний балл: {self.stats_service.get_average_score()}")
        best = self.stats_service.get_best_student()
        print(f"Лучший студент: {best.name}")
