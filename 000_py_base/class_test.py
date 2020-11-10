## https://www.cnblogs.com/bigberg/p/7182741.html
class SchoolMember(object):
    """
    docstring
    """
    member = 0

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
        self.enroll()

    def enroll(self):
        'register'
        print('just enrolled a new scholl member [%s]' % self.name)
        SchoolMember.member += 1

    def tell(self):
        print("----- %s -----" % self.name)
        for k, v in self.__dict__.items():
            print(k, v)
        print('----- end -----')

    def __del__(self):
        print('------------base开除了 【%s】' % self.name)
        SchoolMember.member -= 1


class Teacher(SchoolMember):
    """
    docstring teacher class
    """
    def __init__(self, name, age, sex, salary, course):
        SchoolMember.__init__(self, name, age, sex)
        self.salary = salary
        self.course = course

    def teaching(self):
        print('Teacher [%s] is teaching [%s]' % (self.name, self.course))


class Student(SchoolMember):
    """
    docstring
    """
    def __init__(self, name, age, sex, course, tuition):
        SchoolMember.__init__(self, name, age, sex)
        self.course = course
        self.tuition = tuition
        self.amount = 0

    def pay_tuition(self, amount):
        print('student [%s] has just paied [%s]' % (self.name, self.amount))
        self.amount += amount

    def __del__(self):
        print('------------stu开除了 【%s】' % self.name)


t1 = Teacher('wusir', 28, 'M', 3000, 'python')
t1.tell()
print(SchoolMember.member)
s1 = Student('haitao', 38, 'M', 'python', 30000)
s1.tell()
print(SchoolMember.member)
s2 = Student('lichuang', 12, 'M', 'python', 11000)
s2.tell()
print(SchoolMember.member)

del s2
print(SchoolMember.member)
print('game over')