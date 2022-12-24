# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
# x = [2, 3, 6, 10, 12, 16, 5]
# print(x)
# sum = 0
# for i in range(1,len(x),2):
#     sum+= x[i]
# print(sum)

# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# num = [2, 3, 4, 5, 6]
# def ssu (num):
#         print(num)
#         num2 = []
#         size = len(num)
#         for i in range(0,len(num)):
#             while i < len(num)/2 and size > len(num)/2:
#                 size -= 1
#                 a = num[i]*num[size]
#                 num2.append(a)
#                 i+=1
#         print(num2)

# ssu(num)


# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу 
# между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
# from random import uniform

# n = int(input('Введите размер списка '))
# list1 = []
# for i in range(n):
#     f = uniform(0, 9)
#     list1.append(round(f, 2))
# min = list1[0]
# max = 0
# for i in range(len(list1)):
#     if max < list1[i]:
#         max = list1[i]
#     if min > list1[i]:
#         min = list1[i]
# dif = (max - int(max)) - (min - int(min))
# print(list1)
# print(max, min)
# print(round(dif,2))

# 2 Вариант решения
num = [1.1, 1.2, 3.1, 5.2, 10.01]
newnum = [round(i-int(i),2) for i in num]
print(newnum)
print(max(newnum)-min(newnum))


# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

n = int(input("Введите число: "))
def binar(value):
    b = ""
    while value > 0:
        b = str(value%2)+ b
        value //=2
    print(b)
binar(n)

# 2 вариант решения
# n = int(input("Введите число: "))
# print(f"{n} => {format(n, 'b')}")




# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21].
# n = int(input())
# def fib(n):
#     if n in [1,2]:
#         return 1
#     else:
#         return fib(n-1)+fib(n-2)

# def NegaFib(n):
#     if n == 1:                       
#         return 1
#     elif n == 2:                       
#         return -1
#     else:
#         num1, num2 = 1, -1
#         for i in range(2, n):
#             num1, num2 = num2, num1 - num2
#         return num2
# list =[]
# for e in range(1,n+1):
#     list.append(fib(e))
#     list.insert(0,NegaFib(e))
# print(list)