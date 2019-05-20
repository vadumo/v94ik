# 1.  Написати функцію, яка знаходить середнє арифметичне значення довільної кількості чисел.
# def arg(*args):
#     k = 0
#     m = 0
#     for i in args:
#         print(i, k)
#         m += i
#         k += 1
#         print(m)
#         l = m / k
#     return l
# 2.  Написати функцію, яка повертає абсолютне значення числа
# def modul(x):
#     if x < 0:
#         return -x
#     else:
#         return x
# 3.  Написати функцію, яка знаходить максимальне число з двох чисел, а також в функції використати рядки документації
# DocStrings.
# def max_num(a, b):
#     '''функція знаходить максимальне число'''
#     if a > b:
#         return a
#     else:
#         return b
# 4.  Написати програму, яка обчислює площу прямокутника, трикутника та кола (написати три функції для обчислення
# площі, і викликати їх в головній програмі в залежності від вибору користувача)
# def s_circle():
#     p = 3.14
#     radius = int(input("Enter radius of the circle: "))
#     S = p * radius ** 2
#     print("S of circle =", S)
#
# def s_triangle():
#     a = int(input("Enter side of the triangle: "))
#     h = int(input("Enter height of the triangle: "))
#     S = 0.5 * a * h
#     print("S of the circle =", S)
#
# def s_rectangle():
#     a = int(input("Enter first side of the rectangle: "))
#     b = int(input("Enter second side of the rectangle: "))
#     S = a * b
#     print("S of the rectangle =", S)
#
# print("1 = S circle\n"
#       "2 = S triangle\n"
#       "3 = S rectangle")
# user = int(input("Choice figure:"))
# if user == 1:
#     print(s_circle())
# elif user == 2:
#     print(s_triangle())
# elif user == 3:
#     print(s_rectangle())
# else:
#     print("Input Eror")
# 5.  Написати функцію, яка обчислює суму цифр введеного числа.
# def sum_of_number(number):
#     """This function counts sum of digits of the entered number"""
#     x = 0
#     for i in range(number + 1):
#         x += i
#     return x
#
# print(sum_of_number(5))
# print(sum_of_number.__doc__)
# 6.  Написати програму калькулятор, яка складається з наступних функцій: 
# print("The number 0 closes the program")
#
# while True:
#     x = float(input("Enter the first number, x=  "))
#     symbl = input("Enter one of symbols (+, -, *, /): ")
#     y = float(input("Enter the second number, y=  "))
#
#     if symbl == "0":
#         print("Thank you for choosing our product")
#         break
#     if symbl == "+":
#         print("x + y =", x + y)
#     elif symbl == "-":
#         print("x - y =", x - y)
#     elif symbl == "*":
#         print("x * y =", x * y)
#     elif symbl == "/":
#         if x == 0 or y == 0:
#             print("Division by zero!")
#         else:
#             print("x / y =", x / y)
#     else:
#         print("Input Error")
