class Student:
    def __init__(self, name, age, score):
        self.__name = name
        self.__age = age
        self.__score = score

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_score(self):
        return self.__score

    def set_age(self, age):
        self.__age = age

    def set_score(self, score):
        self.__score = score

    def write_to_file(self, file):
        file.write(self.__name)
        file.write(',')
        file.write(str(self.__age))
        file.write(',')
        file.write(str(self.__score))
        file.write('\n')


