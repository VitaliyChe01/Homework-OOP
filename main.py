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
lecturer2.courses_attached += ['Java']

lecturer3 = Lecturer('Ярослав', 'Орденоносец')
lecturer3.courses_attached += ['Python']

lecturer4 = Lecturer('Нестор', 'Махно')
lecturer4.courses_attached += ['Java']

# Студенты
best_student = Student('Тим', 'Бернес-Ли', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.finished_courses += ['Введение в программирование']

student = Student('Евгений', 'Странников', 'your_gender')
student.courses_in_progress += ['Python']
student.finished_courses += ['Введение в программирование']

student2 = Student('Ильич', 'Лен', 'your_gender')
student2.courses_in_progress += ['Java']
student2.finished_courses += ['Введение в программирование']

# Оценки студентов лекторам
best_student.rate_lecturer(lecturer, 'Python', 10)
best_student.rate_lecturer(lecturer, 'Python', 10)
best_student.rate_lecturer(lecturer, 'Python', 10)

best_student.rate_lecturer(lecturer3, 'Python', 5)
best_student.rate_lecturer(lecturer3, 'Python', 8)
best_student.rate_lecturer(lecturer3, 'Python', 7)

student.rate_lecturer(lecturer, 'Python', 10)
student.rate_lecturer(lecturer, 'Python', 9)
student.rate_lecturer(lecturer, 'Python', 10)

student.rate_lecturer(lecturer3, 'Python', 7)
student.rate_lecturer(lecturer3, 'Python', 6)
student.rate_lecturer(lecturer3, 'Python', 1)

student2.rate_lecturer(lecturer2, 'Java', 8)
student2.rate_lecturer(lecturer2, 'Java', 7)
student2.rate_lecturer(lecturer2, 'Java', 9)

student2.rate_lecturer(lecturer4, 'Java', 10)
student2.rate_lecturer(lecturer4, 'Java', 2)
student2.rate_lecturer(lecturer4, 'Java', 4)

# Эксперты
good_reviewer = Reviewer('Some', 'Buddy')
good_reviewer.courses_attached += ['Python']
good_reviewer.courses_attached += ['Java']

bad_reviewer = Reviewer('Some', 'Buddy')
bad_reviewer.courses_attached += ['Python']
bad_reviewer.courses_attached += ['Java']

# Оценки экспертов студентам
good_reviewer.rate_hw(best_student, 'Python', 10)
good_reviewer.rate_hw(best_student, 'Python', 10)
good_reviewer.rate_hw(best_student, 'Python', 10)

good_reviewer.rate_hw(student, 'Python', 9)
good_reviewer.rate_hw(student, 'Python', 6)
good_reviewer.rate_hw(student, 'Python', 3)

bad_reviewer.rate_hw(best_student, 'Python', 8)
bad_reviewer.rate_hw(best_student, 'Python', 9)
bad_reviewer.rate_hw(best_student, 'Python', 8)

bad_reviewer.rate_hw(student, 'Python', 2)
bad_reviewer.rate_hw(student, 'Python', 3)
bad_reviewer.rate_hw(student, 'Python', 1)

good_reviewer.rate_hw(student2, 'Java', 8)
good_reviewer.rate_hw(student2, 'Java', 9)
good_reviewer.rate_hw(student2, 'Java', 9)

bad_reviewer.rate_hw(student2, 'Java', 6)
bad_reviewer.rate_hw(student2, 'Java', 9)
bad_reviewer.rate_hw(student2, 'Java', 10)

# Вывод студентов
print(f'Студенты:\n\n{best_student} \n\n{student}\n\n{student2}\n\n')

# Вывод лекторов
print(f'Леторы:\n\n{lecturer} \n\n{lecturer2}\n\n{lecturer3}\n\n{lecturer4}\n\n')

# Сравнение студентов по средним оценкам
print(f'Результат сравнения студентов по средним оценкам:'
      f'{best_student.name} {best_student.surname} > {student.name} {student.surname} = {best_student > student}\n')

# Сравнение лекторов по средним оценкам
print(f'Результат сравнения лекторов по средним оценкам:'
      f'{lecturer.name} {lecturer.surname} > {lecturer3.name} {lecturer3.surname} = {lecturer > lecturer3}\n')

# Списки студентов и лекторов
student_list = [best_student, student, student2]

lecturer_list = [lecturer, lecturer2, lecturer3, lecturer4]

# Функция для подсчета средней оценки студентов
def student_rating(student_list, course_name):
    sum_all = 0
    count_all = 0
    for stud in student_list:
        if stud.courses_in_progress == [course_name]:
            sum_all += stud.average_grades()
            count_all += 1
    average_for_all = sum_all / count_all
    return average_for_all

# Функция для подсчета средней оценки лекторов
def lecturer_rating(lecturer_list, course_name):
    sum_all = 0
    count_all = 0
    for lect in lecturer_list:
        if lect.courses_attached == [course_name]:
            sum_all += lect.average_grades()
            count_all += 1
    average_for_all = sum_all / count_all
    return average_for_all

# Вывод средних оценок по всем студентам определенного курса
print(f'Средняя оценка по всем студентам по курсу Python: \n{student_rating(student_list,'Python')}\n')
print(f'Средняя оценка по всем студентам по курсу Java: \n{student_rating(student_list,'Java')}\n')

# Вывод средних оценок по всем лекторам определенного курса
print(f'Средняя оценка по всем лекторам по курсу Python: \n{lecturer_rating(lecturer_list,'Python')}\n')
print(f'Средняя оценка по всем лекторам по курсу Java: \n{lecturer_rating(lecturer_list,'Java')}\n')