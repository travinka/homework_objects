

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __lt__(self, other):

        return self.mean_g < other.mean_g

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]


    def __str__(self):
        return f'Имя: {self.name},\n'\
               f'Фамилия: {self.surname} \n' \
               f'Средняя оценка за домашние задания: {self.grades}\n' \
               f'Курсы в процессе изучения:{self.courses_in_progress}\n' \
               f'Завершенные курсы: Введение в программирование '

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}

    def __str__(self):
        return f'Имя: {self.name},\n'\
               f'Фамилия: {self.surname} \n' \
               f'Средняя оценка за лекции: {self.grades}\n' \


    def __lt__(self, other):
        return self.mean_g < other.mean_g


class Reviewer(Mentor):
     def rate_hw(self, student, course, grade):
         if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
             if course in student.grades:
                 student.grades[course] += [grade]
             else:
                student.grades[course] = [grade]

     def __str__(self):
        return f'Имя: {self.name},\n'\
               f'Фамилия: {self.surname} \n' \


def mean_grades(arr):
    for a in arr.values():
        mean_g = sum(a)/len(a)
        return mean_g




our_lecturer1 = Lecturer('Ivan','Petrov')
our_lecturer1.courses_attached += ['Python']

our_lecturer2 = Lecturer('Nikola','Poh')
our_lecturer2.courses_attached += ['Python']

best_student = Student('Ruoy', 'Eman', 'female')
best_student.courses_in_progress += ['Python']
best_student.rate_lecturer(our_lecturer1, 'Python', 5)
best_student.rate_lecturer(our_lecturer2, 'Python', 3)
cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 6)
print(best_student.grades)
print(mean_grades(best_student.grades))

bad_student = Student('Mike', 'Badboy', 'male')
bad_student.courses_in_progress += ['Python']
bad_student.rate_lecturer(our_lecturer1, 'Python', 10)
bad_student.rate_lecturer(our_lecturer2, 'Python', 7)

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(bad_student, 'Python', 6)

bad_mentor = Reviewer('Mad', 'DOG')
bad_mentor.courses_attached += ['Python']
bad_mentor.rate_hw(best_student, 'Python', 6)
bad_mentor.rate_hw(bad_student, 'Python', 2)

print(cool_mentor)
print(bad_mentor)

print(our_lecturer1)
print(our_lecturer2)

print(best_student)
print(bad_student)

print(best_student.grades)
print(bad_student.grades)
print(our_lecturer1.grades)
print(our_lecturer2.grades)



print(mean_grades(best_student.grades) > mean_grades(bad_student.grades))

print(mean_grades(our_lecturer1.grades) > mean_grades(our_lecturer2.grades))










