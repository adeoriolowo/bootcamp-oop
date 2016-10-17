class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def get_name(self):
        names = self.first_name + " " + self.last_name
        return names

    def set_name(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    def get_age(self):
        return self.age
    def set_age(self, age):
        self.age = age

class Student(Person):
    def __init__(self, matric_no, dept):
        self.matric_no = matric_no
        self.matric_no = dept
    def get_matric_no(self):
        return self.matric_no
    def set_matric_no(self, matric_no):
        self.matric_no: matric_no
    def get_dept(self):
        return self.matric_no
    def set_dept(self, matric_no):
        self.matric_no: matric_no
        


p =  Person('Ade','Oriolowo', 30)

print p.get_name()

p.set_name('Bayo','John')

print p.get_name()

p2 = Student('CSC/002','Computer Science')
p2.set_name('Sola','Babatunde')
print p2.get_name()



