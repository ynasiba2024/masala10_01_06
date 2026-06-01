#10-masala
class University:
    def __init__(self, name, students):
        self.name = name
        self.__students = students

    @property
    def students(self):
        return self.__students

    @students.setter
    def students(self, count):
        self.__students = count

u1 = University("TATU", 10000)

print(u1.students)

u1.students = 12000
print(u1.students)
