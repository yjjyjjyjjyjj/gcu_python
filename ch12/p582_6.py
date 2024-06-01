class Department:
    def __init__(self, department_name):
        self.department_name = department_name
        self.courses = []

    def add_course(self, course_name, course_credit):
        c = Course(course_name, course_credit)
        self.courses.append(c)
        return c

class Course:
    def __init__(self, course_name, course_credit):
        self.course_name = course_name
        self.course_credit = course_credit

    # def __str__(self):
    #     return "과목 이름 : "+str(self.course_name)+"\n이수 학점 : "+str(self.course_credit)

class Student:
    def __init__(self, name, Id):
        self.name = name
        self.Id = Id
        self.courses = []

    def enroll(self, course):
        self.courses.append(course)

dept = Department("컴퓨터")
math1 = dept.add_course("공업수학", 3)
math2 = dept.add_course("이산수학", 2)

kim = Student("kim", 20200001)
kim.enroll(math1)