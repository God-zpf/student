from menu import show_menu
from student_info import *

def main():
    stu_info = []
    while True:
        show_menu()
        stu_info = read_from_file()
        command = input('请选择：')
        if command == '1':
            add_stu(stu_info)
        elif command == '2':
            show_stu(stu_info)
        elif command == '3':
            modify_stu(stu_info)
        elif command == '4':
            del_stu(stu_info)
        elif command == '5':
            sort_stu_high(stu_info)
        elif command == '6':
            sort_stu_low(stu_info)
        elif command.lower() == 'q':
            print('退出学生系统成功')
            break
        else:
            print('输入有误，请重新输入!')

if __name__ == '__main__':
    main()