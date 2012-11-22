__author__ = 'matt'

class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age
    def __repr__(self):
        return repr((self.name, self.grade, self.age))

if __name__ == '__main__':

    student_objects = [
        Student('Jack', 'D', 15),
        Student('john', 'A', 15),
        Student('jane', 'B', 12),
        Student('dave', 'B', 10),
    ]

    print enumerate(student_objects)

    decorated = [(student.grade, i, student) for i, student in enumerate(student_objects)]
    print decorated
    decorated.sort()
    finalSort = [student for grade, i, student in decorated]
    print finalSort

    print '\r\n'

    decorated2 = [(student.grade, i, student) for i in enumerate(student_objects)]
    print decorated2
    decorated2.sort()
    finalSort2 = [student for grade, i, student in decorated2]
    print finalSort2

