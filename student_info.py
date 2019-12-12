from student import Student

def add_stu(L):
    try:
        name = input('请输入学生姓名：')
        age = int(input('请输入学生年龄：'))
        score = int(input('请输入学生成绩：'))
    except ValueError:
        print('输入不合法，请重新输入!')
    except:
        print('发生其他错误')
    else:
        stu = Student(name, age, score)
        L.append(stu)
        __write_to_file(L)
        print('添加学生信息成功')

def show_stu(L):
    print('----------------------------')
    print('|%s|%s|%s|' % ('name'.center(8), 'age'.center(8), 'score'.center(8)))
    print('----------------------------')
    for stu in L:
        print('|%s|%s|%s|' % (stu.get_name().center(8), str(stu.get_age()).center(8), str(stu.get_score()).center(8)))
    print('----------------------------')

def modify_stu(L):
    name = input('请输入修改学生姓名：')
    for stu in L:
        if stu.get_name() == name:
            try:
                age = int(input('请输入修改年龄：'))
                score = int(input('请输入修改成绩：'))
                stu.set_age(age)
                stu.set_score(score)
                __write_to_file(L)
            except ValueError:
                print('输入不合法，请重新输入!')
            else:
                print('修改学生信息成功')
            return
    else:
        print('该学生尚未录入信息')

def del_stu(L):
    name = input('请输入删除学生姓名：')
    for stu in L:
        if stu.get_name() == name:
            L.remove(stu)
            print('删除学生信息成功')
            __write_to_file(L)
            return
    else:
        print('该学生尚未录入成绩')


def sort_stu_high(L):
    stu_list = sorted(L, key=lambda d:d.get_score(), reverse=True)
    show_stu(stu_list)

def sort_stu_low(L):
    stu_list = sorted(L, key=lambda d:d.get_score())
    show_stu(stu_list)

def __write_to_file(L):
    try:
        with open('student.txt', 'w') as f:
            for stu in L:
                stu.write_to_file(f)
    except:
        print('写入文件失败')
    else:
        print('写入文件成功')

def read_from_file():
    L = []
    try:
        with open('student.txt') as f:
            for line in f:
                line = line.strip()
                name, age, score = line.split(',')
                stu = Student(name, int(age), int(score))
                L.append(stu)
        return L
    except:
        print('文件读取失败')