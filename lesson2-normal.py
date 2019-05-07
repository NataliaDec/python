#1
numbers = [25, 11, 169, -7, -10, 55]
newnumbers = []
for number in numbers:
    sqrtnumber = number ** 0.5
    complexnumbers = isinstance(sqrtnumber, complex)
    if complexnumbers != True:
        balance = sqrtnumber % 1
        if balance == 0:
            intsqrtnumber = int(sqrtnumber)
            newnumbers.append(intsqrtnumber)
print(newnumbers)

#2

today = '07.05.2019'
day = int(today[:2])
month = int(today[3:5])
year = today[-4:]
daylist = {1: 'первое', 2: 'второе', 3: 'третье', 4: 'четвертое', 5: 'пятое', 6: 'шестое', 7: 'седьмое', 8: 'восьмое', 9: 'девятое', 10: 'десятое', 11: 'одиннадцатое', 12: 'двенадцатое', 13: 'тринадцатое',
           14: 'четырнадцатое', 15: 'пятнадцатое', 16: 'шестнадцатое', 17: 'семнадцатое', 18: 'восемнадцатое', 19: 'девятнадцатое', 20: 'двадцатое', 21: 'двадцать первое', 22: 'двадцать второе', 23: 'двадцать третье',
            24: 'двадцать четвертое', 25: 'двадцать пятое', 26: 'двадцать шестое', 27: 'двадцать седьмое', 28: 'двадцать восьмое', 29: 'двадцать девятое', 30: 'тридцатое', 31: 'тридцать первое'}
monthlist = {1: 'января', 2: 'февраля', 3: 'марта', 4: 'апреля', 5: 'мая', 6: 'июня', 7: 'июля', 8: 'августа', 9: 'сентября', 10: 'октября', 11: 'ноября', 12: 'декабря'}
daystr = daylist.get(day)
monthstr = monthlist.get(month)
strformat = '{} {} {} года.'.format(daystr, monthstr, year)
print(strformat)

#3
import random

randomlist = []
while len(randomlist) < 20:
    randomnumber = random.randint(-100, 100)
    randomlist.append(randomnumber)
print(randomlist)

#4a
newlist = [34, 45, 6, 7, 2, 3, 2, 2, 3]
setnewlist = set(newlist)
newlist2 = list(setnewlist)
print(newlist2)

#4b
newlist = [34, 45, 6, 7, 2, 3, 2, 2, 3]
newlist3 = []
for element in newlist:
    if newlist.count(element) == 1:
        newlist3.append(element)
print(newlist3)
