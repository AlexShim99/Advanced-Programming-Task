#!/usr/bin/python3

class Student(object):
    def __init__(self, first='', last='', id=0):
        self.first_name_str = first
        self.last_name_str = last
        self.id_int = id

    def update(self, first='', last='', id=0):
        if first:
            self.first_name_str = first
        if last:
            self.last_name_str = last
        if id:
            self.id_int = id

    def __str__(self):
        return "{} {}, ID:{}".format(self.first_name_str, self.last_name_str, self.id_int)

#my_name = Student()
#my_name.__init__('Chung Siong','Shim')
#my_name.__str__()

s1 = Student(last='Python', first='Monty')
print(s1.last_name_str)
print(str(s1))
print(s1.__str__())
s1.update('Alibi')
print(s1.__str__())
