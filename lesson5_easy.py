#1
import os
import sys

def pint_help():
    print("help - получение справки")
    print("chdir <path> - перейти в папку")
    print("filesdir - получить все файлы, находящиеся в текущей директории")
    print("dir - получить все папки, находящиеся в текущей директории")
    print("removedir <path> - удалить папку")
    print("mkdir <path> - создать папку")

def make_dir():
        default = input("Создать 9 папок по умолчанию? | Да/Нет ")
        if default == 'Да':
            n = 10
            i = 1
            while i < n:
                dir_path = os.path.join(os.getcwd(), 'dir_' + str(i))
                try:
                    os.mkdir(dir_path)
                    print('Директория создана')
                except FileExistsError:
                    print('Такая директория уже существует')
                i += 1
        elif default == 'Нет':
            name = input('Будет создана одна папка. Введите название папки: ')
            dir_path = os.path.join(os.getcwd(), name)
            try:
                os.mkdir(dir_path)
                print('Директория создана')
            except FileExistsError:
                print('Такая директория уже существует')
        else: print("Ответ не распознан. Повторите попытку")

#2
def files_dir():
    files = os.listdir()
    print(files)

def dir():
    dir = [x for x in files_dir() if os.path.isdir(os.path.join(x))]
    print(dir)

#3
def copy_file():
    with open(sys.argv[0], 'r') as file:
        file_read = file.read()
        filename = sys.argv[0]
        py = filename[-3:]
        name = filename[:-3] + 'Copy' + py
    with open(name, 'w') as file:
        file.write(file_read)
    print("Выполнена копия файла")

#normal
def change_dir():
    path = input("Укажите полный путь к директории: ")
    try:
        os.chdir(path)
        print("Вы перешли в директорию: " + path)
    except FileExistsError:
        print("Данной директории не существует. Укажите правильный путь")

def remove_dir():
    path = input("Укажите полный путь к папке, которую хотите удалить: ")
    try:
        os.remove(path)
        print("Вы удалили папку: " + path)
    except FileExistsError:
        print("Невозможно удалить папку")

do = {
    "mkdir": make_dir,
    "filesdir": files_dir,
    "copy": copy_file
}
try:
    key = sys.argv[1]
except IndexError:
    key = None
if key:
    if do.get(key):
        do[key] ()
    else:
        print("Задан неверный ключ")