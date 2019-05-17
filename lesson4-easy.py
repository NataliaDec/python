#1
numbers = [1, 2, 4, 0]
numbers_new = [x ** 2 for x in numbers]
print(numbers_new)

#2
fruits_first = ['яблоко', 'банан', 'киви', 'арбуз']
fruits_second = ['банан', 'ананас', 'арбуз']
fruits_new = [x for x in fruits_first if x in fruits_second]
print(fruits_new)

#3
numbers_int = [3, 4, 6, 7, 12, 23, 88, 77, 66]
numbers_new_int = [x for x in numbers_int if x%3 == 0 and x >= 0 and x%4 != 0]
print(numbers_new_int)