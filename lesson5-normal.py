import sys
print('sys.argv = ', sys.argv)
from lesson5_easy import*

menu = print("__________________Меню:_________________"'\n'
    "1.  Перейти в папку"  '\n'
    "2.  Просмотреть содержимое текущей папки" '\n'
    "3.  Удалить папку" '\n'
    "4.  Создать папку"'\n')

menu = input("Выберите пункт меню: ")
try:
    menu = int(menu)
except:
    print('Введите число!')

if  menu == 1:
    change_dir()
elif menu == 2:
    files_dir()
elif menu == 3:
    remove_dir()
elif menu == 4:
    make_dir()
else:
    print("Нет такого пункта меню")