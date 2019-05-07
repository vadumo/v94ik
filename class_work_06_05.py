"""
rices = [int(i) for i in input('Введите значения цен через пробел ').split()]
print(" Max number is:", max(rices))
print(" Min number is:", min(rices))
--------------------------------------------------
for i in range(1, 11):
    if i % 2 == 0:
        print("parni = ", i)
    elif i % 3 == 0:
        print("neparni = ", i)
    else:
        print("ne dilatsa na 2,3 =", i)
-------------------------------------------------
a = int(input())
b = 1
if a < 0:
    print("sorry, factorial doesnt exist negativ numbers")
else:
    for i in range(1, a+1):
        b *= i
    print("factorial number {0} sum {1}".format(a, b))
-------------------------------------------------
user_name = input("username ")
while user_name == "first":
    print('Hello')
    break
else:
    print('eror, try again')
-------------------------------------------------
a = 1
while a != 0:
    if a > 0:
        a = int(input())
        print('You number = ', a)
    else:
        break
-------------------------------------------------
sum_pos = input()
sum_pos = int(sum_pos)
for i in range(sum_pos):
    chusla = int(input())
    if chusla < 0 or chusla == 0:
        break
-------------------------------------------------
for i in range(10, 30):
    if i % 2 == 0:
        print(i, 'equals 2 *', i / 2)
    elif i % 3 == 0:
        print(i, 'equals 3 *', i / 3)
    else:
        print(i, 'is a prime number')
-------------------------------------------------
def sorting(lst):
    lst.sort(key=len)
    return lst


lst = ["rohan", "amy", "sapna", "muhammad",
       "aakash", "raunak", "chinmoy"]
print(sorting(lst))
"""