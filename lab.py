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

print("Matrix A : ")
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

print("Matrix B : ")
printList(b)
print("Matrix C : ")
printList(c)
print("Matrix D : ")
printList(d)
print("Matrix E : ")
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

if min_ > sum_:
    print("Minimum is greater than Summary\n")
    for i in range(0, m):
        for j in range(0,m-i):
            e[i][j], e[m-j-1][m-i-1] = e[m-j-1][m-i-1], e[i][j]
else:
    print("Summary is greater than Minimum\n")
    for i in range(m):
        for j in range(m):
            b[i][j], e[i][j] = e[i][j], b[i][j]

f = []
f.extend(d)
f.extend(c)
for i in range(m):
    f[i].extend(e[i])
for i in range(m, n):
    f[i].extend(b[i-m])

print("Matrix F : ")
printList(f)

at = []
for i in range(n):
    at.append([])
    for j in range(n):
        at[i].append(a[j][i])

for i in range(n):
    for j in range(n):
        f[i][j] *= k

print("Matrix F multiplied to K : ")
printList(f)

fa = []

for i in range(n):
    fa.append([])
    for j in range(n):
        s = 0
        for l in range(n):
             s += f[i][l]*at[j][l]
        fa[i].append(s)

print("Matrix F multiplied to Matrix A : ")
printList(fa)

print("Matrix A transposed : ")
printList(at)

for i in range(n):
    for j in range(n):
        at[i][j] *= k

print("Matrix A transposed multiplied to K : ")
printList(at)

for i in range(n):
    for j in range(n):
        fa[i][j] -= at[i][j]

print("(К*F)*А– K*AT : ")
printList(fa)
