#1
import re

name = input('Введите имя: ')
surname = input('Введите фамилию: ')
email = input('Введите e-mail: ')
pattern = '([a-z_0-9+@[a-z_0-9]+\.[a-z]+)'
pattern1 = 'ru$'
pattern2 = 'org$'
pattern3 = 'com$'
pattern_name = '^[A-Z]'
test = re.match(pattern,email).group(1)
test1 = re.search(pattern1,email) is not None
test2 = re.search(pattern2,email) is not None
test3 = re.search(pattern3,email) is not None
test4 = re.match(pattern_name, name) is not None
test5 = re.match(pattern_name, surname) is not None
if test4 == False:
    print("Имя введено не с заглавной буквы")
else:
    print('Имя введено с заглавной буквы')
if test5 == False:
    print("Фамилия введена не с заглавной буквы")
else:
    print('Фамилия введена с заглавной буквы')
if test != email or (test1 == False and test2 == False and test3 == False):
    print('Неверно указан e-mail')
elif test == email  and (test1 or test2 or test3):
    print('E-mail введен верно')

#2

some_str = '''
Мороз и солнце; день чудесный!
Еще ты дремлешь, друг прелестный —
Пора, красавица, проснись:
Открой сомкнуты негой взоры
Навстречу северной Авроры,
Звездою севера явись!
Вечор, ты помнишь, вьюга злилась,
На мутном небе мгла носилась;
Луна, как бледное пятно,
Сквозь тучи мрачные желтела,
И ты печальная сидела —
А нынче... погляди в окно:
Под голубыми небесами
Великолепными коврами,
Блестя на солнце, снег лежит;
Прозрачный лес один чернеет,
И ель сквозь иней зеленеет,
И речка подо льдом блестит.
Вся комната янтарным блеском
Озарена. Веселым треском
Трещит затопленная печь.
Приятно думать у лежанки.
Но знаешь: не велеть ли в санки
Кобылку бурую запречь?
Скользя по утреннему снегу,
Друг милый, предадимся бегу
Нетерпеливого коня
И навестим поля пустые,
Леса, недавно столь густые,
И берег, милый для меня.'''

pattern_text = '...'
test = re.findall(pattern_text, some_str) is not None
if test:
    print('... присутствует в тексте')
else:
    print('... отсутствует в тексте')
