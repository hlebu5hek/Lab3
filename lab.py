'''Вариант 16
С клавиатуры вводится два числа K и N. Квадратная матрица А(N,N),
состоящая из 4-х равных по размерам подматриц, B,C,D,E заполняется
случайным образом целыми числами в интервале [-10,10].
Для тестирования использовать не случайное заполнение, а целенаправленное.
d e
c b
 4
3 1
 2
Формируется матрица F следующим образом: если в Е минимальный элемент
в нечетных столбцах в области 1 больше, чем сумма чисел в нечетных строках
в области 3, то поменять в В симметрично области 3 и 2 местами,
иначе В и Е поменять местами несимметрично. При этом матрица А не меняется.
После чего вычисляется выражение: (К*F)*А– K*AT . Выводятся по мере формирования
А, F и все матричные операции последовательно.
'''

from random import randint as rnd

def printList(z):
    for i in z:
        for j in i:
            print("{:4}".format(j), end=' ')
        print()
    print()

k, n = int(input("k = ")), int(input("n = "))
m = n//2
n = m*2
a = []

for i in range(n):
    a.append([])
    for j in range(n):
        a[i].append(rnd(-10,10))

print("List a : ")
printList(a)

b = []
c = []
d = []
e = []
for i in range(m):
    b.append([])
    c.append([])
    d.append([])
    e.append([])
    for j in range(m):
        b[i].append(a[i+m][j+m])
        c[i].append(a[i+m][j])
        d[i].append(a[i][j])
        e[i].append(a[i][j+m])

print("List b : ")
printList(b)
print("List c : ")
printList(c)
print("List d : ")
printList(d)
print("List e : ")
printList(e)

min_ = 11
for i in range(m//2):
    for j in range(m-i-1,m):
        if j % 2 == 0: continue
        min_ = min(min_, e[i][j])
for i in range(m//2, m):
    for j in range(i,m):
        if j % 2 == 0: continue
        min_ = min(min_, e[i][j])

sum_ = 0
for i in range(m//2):
    for j in range(0,i+1):
        if i % 2 == 0: continue
        sum_ += e[i][j]
for i in range(m//2, m):
    for j in range(0, m-i):
        if i % 2 == 0: continue
        sum_ += e[i][j]

en = []
for i in range(m):
    en.append(e[i])
bn = []
for i in range(m):
    bn.append(b[i])

if min_ > sum_:
    print("Minimum is greater than Summary\n")
    for i in range(0, m):
        for j in range(0,m-i):
            en[i][j], en[m-j-1][m-i-1] = en[m-j-1][m-i-1], en[i][j]
else:
    print("Summary is greater than Minimum\n")
    for i in range(m):
        for j in range(m):
            bn[i][j], en[i][j] = en[i][j], bn[i][j]

f = []
f.extend(d)
f.extend(c)
for i in range(m):
    f[i].extend(en[i])
for i in range(m, n):
    f[i].extend(bn[i-m])

print("List f : ")
printList(f)

at = []
for i in range(n):
    at.append([])
    for j in range(n):
        at[i].append(a[j][i])

for i in range(n):
    for j in range(n):
        f[i][j] *= k

print("List f times k : ")
printList(f)

fa = []

for i in range(n):
    fa.append([])
    for j in range(n):
        s = 0
        for l in range(n):
             s += f[i][l]*at[j][l]
        fa[i].append(s)

print("List f times List a : ")
printList(fa)

print("List a transposed : ")
printList(at)

for i in range(n):
    for j in range(n):
        at[i][j] *= k

print("List a transposed times k : ")
printList(at)

for i in range(n):
    for j in range(n):
        fa[i][j] -= at[i][j]

print("(К*F)*А– K*AT : ")
printList(fa)
