a = input("vvedit chislo ")
# ������ ������� ���� ����� �����.
one = int(a[1])
two = int(a[2])
three = int(a[3])
four = int(a[0])
dobutok = one*two*three*four
print("dobutok zufr chusla =", dobutok)
# �������� ����� � ���������� �������.
a = a[::-1]
print("chuslo v reversomy poryadky =", a)
# ����������� �����, �� ������� � ���� �����
sort = sorted(str(a), reverse=False)
print("chusla po vozrostaniy = ", sort)