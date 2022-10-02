# a = 1 # переменная "a" не является коробкой в, которую мы кладем 1. Переменная хранит в себе путь к единице, а не саму её.
# b = a # В этом случае мы записываем в переменную "b" путь к переименной "a", в которой хранится путь к 1.

# # ЭТО ВАЖНО ЗАПОМНИТЬ!!!!!!


# print (1, 3, 5, sep = "---", end = "^.^.^.^") 
# # print  имеет 2 аргумента, первый из них это "sep - который указывает чем будут разделены между собой элементы" и второй "end - 
# # который показывает чем заканчивается строка. По умолчанию она закнчивается \n, который говорит
# #  что следующая сторока начинается с новой стороки"
# print (2, 4, 4)


# Task 1
# a = int(input ("add new number: "))
# b = int(input ("add new number 2: "))

# if b == a * a : print (f'{a} * {a} = {b} -> True')
# elif a == b**2: print (f'{b} * {b} = {a} -> True')
# elif b != a**2: print (f'{a} * {a} != {b} -> FALSE')
# else : print (f'{b} * {b} != {a} -> FALSE')


#Task 2
#напишите прогграмму , которая на вход принимает число N  и возвращает все числра от -N до N

# a = int(input("Add new number: ")) 
# b = -a

# while b <= a : 
#     print(b) 
#     b+=1
# else : print ("Stop")


#Task 3

#напишите программу которая будет принримать на вход дробное число и показывать первую цифру дробного числа.

# a = float(input("Add new number: "))
# b = round(a, 2)
# c = int((b * 10) %10)
# print(b)
# print(c)

numbers = list(map(int, input("Add new numbers: ").split()))#[1, 2, 3, 4, 5, 6]
i = 0
j = len(numbers)
num = 0
while i < j:
    num = numbers[i] * numbers[j - 1]
    print(num)
    i+=1
    j-=1
else: print ("Stop")






