a = int(input("input number a"))
b = int(input("input number b"))
print(a if a >= b else b)

a = int(input("print number "))
if a % 2 == 0:
    print("parne")
else:
    print("neparne")

a = int(input())
b = 1
for i in range(1, a+1):
    b *= i
print(b)
