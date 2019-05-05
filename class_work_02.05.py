# task_1.1
i = 0
for i in range(100):
    if i % 2 != 0:
        continue
    print(i, end=" ")
# task_1.2
i = 0
while i < 100:
    print(i, end=" ")
    i += 2
# task_2.1
i = 1
while i < 100:
    print(i, end=" ")
    i += 2
# task_2.2
i = 0
while i < 100:
    i += 1
    if i % 2 == 0:
        continue
    print(i, end=" ")
# task_3
list = [1, 2, 4, 6]
for i in list:
    if i % 2 != 0:
        break
else:
    print("vsi chusla parni")
# task_4
a = [1, 2, 3, 4, 5, 6]
for i in a:
    print(float(i))
# task_5
n = int(input())
first_max = 0
two_max = 1
while two_max < n:
    print(first_max, end=" ")
    print(two_max, end=" ")
    first_max += two_max
    two_max += first_max
# task_6
a = [1, 2, 3, 4]
for i in a:
    print(i)
# task_7
a = [6, 2, 3, 4]
for i in a:
    print(i, end="# ")
