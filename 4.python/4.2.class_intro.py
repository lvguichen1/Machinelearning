#!/usr/bin/python
# -*- coding:utf-8 -*-


class People:
    def __init__(self, n, a, s):
        self.name = n
        self.age = a
        self.__score = s
        self.print_people()

    def print_people(self):
        str = u'%s的年龄为：%d，成绩为：%.2f' % (self.name, self.age, self.__score)
        print str

    __print_people = print_people


class Student(People):
    def __init__(self, n, a, w):
        People.__init__(self, n, a, w)
        self.name = 'Student ' + self.name

    def print_people(self):
        str = u'%s的年龄为：%d' % (self.name, self.age)
        print str


def func(p):
    p.age = 11


if __name__ == '__main__':
    p = People('Tom', 18, 89)
    p.print_people()    # p传入的是引用类型
    print

    # 注意分析下面语句的打印结果，是否觉得有些“怪异”？
    j = Student('Jerry', 15, 90)
    print

    # 成员函数
    p.print_people()
    j.print_people()
    print

    People.print_people(p)
    People.print_people(j)