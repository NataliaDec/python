#1
fruits = ['яблоко', 'банан', 'киви', 'арбуз']
maxword = (max(fruits, key = len));
lenmaxword = len(maxword);
i = 0
for fruit in fruits:
    i += 1
    result = '{}'.format(fruit)
    f= result.rjust(lenmaxword, ' ')
    print(str(i) + '. ' + f)

#2
firstlist = ['number', 56, 'first', 24]
secondlist = ['ok', 'forest', 'number']
setfirstlist = set(firstlist)
setsecondlist = set(secondlist)
compare = setfirstlist & setsecondlist
formatcompare = ((str(compare)[2:-2]))
indexformatcompare = (firstlist.index(formatcompare))
firstlist.pop(indexformatcompare)
print(firstlist)

#3
numbers = [2, 5, 6, 8, 3, 22, 15, 10]
numbersnew = []
for number in numbers:
    if number % 2 == 0:
        newnumber = number / 4
    else:
        newnumber = number * 2
    numbersnew.append(newnumber)
print(numbersnew)