class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer,Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grades(self):
        all_grades = []
        for grade in self.grades.values():
            all_grades.extend(grade)
        return round(sum(all_grades) / len(all_grades), 1) if all_grades else 0

    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {self.average_grades()}\n"
                f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n"
                f"Завершённые курсы: {', '.join(self.finished_courses) if self.finished_courses else 'Нет'}")

    # Сравнение оценок студентов
    def __gt__(self, other):
        return self.average_grades() > other.average_grades()

    def __lt__(self, other):
        return self.average_grades() < other.average_grades()

    def __eq__(self, other):
        return self.average_grades() == other.average_grades()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return (f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}")

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grades(self):
        all_grades = []
        for grades in self.grades.values():
            all_grades.extend(grades)
        return round(sum(all_grades) / len(all_grades), 1) if all_grades else 0

    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"средняя оценка за лекции: {self.average_grades()}")

    # Сравнение оценок лекторов
    def __gt__(self, other):
        return self.average_grades() > other.average_grades()

    def __lt__(self, other):
        return self.average_grades() < other.average_grades()

    def __eq__(self, other):
        return self.average_grades() == other.average_grades()

# Лекторы
lecturer = Lecturer('Олег', 'Смирнов')
lecturer.courses_attached += ['Python']
lecturer2 = Lecturer('Владислав', 'Бывалый')
lecturer2.courses_attached += ['Python']

# Студенты
best_student = Student('Тим', 'Бернес-Ли', 'your_gender')
best_student.courses_in_progress += ['Python']

student = Student('Евгений', 'Странников', 'your_gender')
student.courses_in_progress += ['Python']

# Оценки студентов лекторам
best_student.rate_lecturer(lecturer, 'Python', 10)
best_student.rate_lecturer(lecturer, 'Python', 10)
best_student.rate_lecturer(lecturer, 'Python', 10)

student.rate_lecturer(lecturer2, 'Python', 7)
student.rate_lecturer(lecturer2, 'Python', 6)
student.rate_lecturer(lecturer2, 'Python', 1)

# Эксперты
good_reviewer = Reviewer('Some', 'Buddy')
good_reviewer.courses_attached += ['Python']
bad_reviewer = Reviewer('Some', 'Buddy')
bad_reviewer.courses_attached += ['Python']

# Оценки экспертов студентам
good_reviewer.rate_hw(best_student, 'Python', 10)
good_reviewer.rate_hw(best_student, 'Python', 10)
good_reviewer.rate_hw(best_student, 'Python', 10)

bad_reviewer.rate_hw(student, 'Python', 2)
bad_reviewer.rate_hw(student, 'Python', 3)
bad_reviewer.rate_hw(student, 'Python', 1)

# Средние оценки Лекторов
print(lecturer.average_grades())
print(lecturer2.average_grades())

# Средние оценки студентов
print(best_student.average_grades())
print(student.average_grades())

# Сравнение оценок лекторов
print(lecturer > lecturer2)
print(lecturer == lecturer2)
print(lecturer < lecturer2)

# Сравнение оценок студентов
print(best_student > student)
print(best_student == student)
print(best_student < student)

# Вывод информации лекторов
print(lecturer)
print(lecturer2)

# Вывод информации экспертов
print(good_reviewer)
print(bad_reviewer)

# Вывод информации студентов
print(student)
print(best_student)