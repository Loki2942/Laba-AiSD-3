"""
С клавиатуры вводится два числа K и N. Квадратная матрица А(N,N), состоящая из 4-х равных по размерам подматриц,
B,C,D,E заполняется случайным образом целыми числами в интервале [-10,10]. Для тестирования использовать не случайное
заполнение, а целенаправленное.

Для ИСТд-13 вид матрицы А
D	Е
С	В

Каждая из матриц B,C,D,E имеет вид
Для ИСТд-13
     4
  3     1
     2

Вариант №16:
Формируется матрица F следующим образом: если в Е минимальный элемент в нечетных столбцах в области 1 больше,
чем сумма чисел в нечетных строках в области 3, то поменять в В симметрично области 3 и 2 местами, иначе В и Е поменять
местами несимметрично. При этом матрица А не меняется. После чего вычисляется выражение:
(К*F)*А– K*AT(К умножается на транспонированную матрицу А) .
Выводятся по мере формирования А, F и все матричные операции последовательно.
"""

import random
from math import ceil, floor

def printMatrix(matrix): # функция вывода матрицы
   for i in range(len(matrix)):
      for j in range(len(matrix[i])):
          print ("{:5d}".format(matrix[i][j]), end="")
      print ()

n = int(input('Введите число число N, большее или равное 5: '))
while n < 5:  # ошибка в случае введения слишком малого порядка матрицы
    n = int(input("Введите число N, большее или равное 5: "))
k = int(input('Введите число число K: '))

# ниже создание и вывод матрицы А(N,N) c диапазоном значений от -10 до 10
A = [ [ random.randint(-10, 10) for j in range(n)] for i in range(n) ]
print('\nМатрица А:')
printMatrix(A)

F = [[elem for elem in raw] for raw in A]         # создание матрицы F, на данный момент равной матрице A
F_dump = [[elem for elem in raw] for raw in F]        # резервная копия матрицы F для дальнейших операций

submatrix_order = ceil(n/2) # определение порядка подматрицы

# вычленяем матрицу Е через срезы
# проверка n на четность нужна для корректного среза(чтобы матрица А делилась на равные 4 подматрицы)


if n %2 == 0:
    e = [F[i][submatrix_order:n] for i in range(0,submatrix_order)]
else:
    e = [F[i][submatrix_order-1:n] for i in range(0, submatrix_order)]


# ниже ищем минимальный элемент в области 1 в Е
minlist = []
for i in range(submatrix_order):
    for j in range(submatrix_order):
        if (i <= j) and ((i + j + 1) >= submatrix_order) and (j+1) % 2 != 0:
            minlist.append(e[i][j])
minvalue = min(minlist)


# ниже ищем сумму чисел в нечетных строках в области 3
sumvalue = 0
for i in range(submatrix_order):
    for j in range(submatrix_order):
        if (i >= j) and ((i + j + 1) <= submatrix_order) and (i+1) % 2 != 0:
            sumvalue += e[i][j]

# ниже выполнение инструкций по условию
if minvalue > sumvalue:
    for i in range(submatrix_order, n):
        for j in range(submatrix_order, n):
            if i >= j:
                F_dump[i][j] = F[submatrix_order - j - 1][submatrix_order - i - 1]
    print("Матрица F:")
    F = F_dump
    printMatrix(F)
else:
    for i in range(ceil(n/2)):
        for j in range(ceil(n/2),n):
            F[i][j] = F_dump[floor(n / 2) + i][j]
            F[floor(n / 2) + i][j] = F_dump[i][j]
    print("Матрица F:")
    printMatrix(F)


KF = [[0 for i in range(n)] for j in range(n)]      # заготовка под результат умножения матрицы F на коэффициент K
for i in range(n):          # производим умножение матрицы на коэффициент
    for j in range(n):
        KF[i][j] = k * F[i][j]
print("\nРезультат умножения коэффициента K на матрицу F:")
printMatrix(KF)


KFA = [[0 for i in range(n)] for j in range(n)]      # заготовка под результат умножения матрицы KF A на матрицу A
for i in range(n):              # производим умножение двух матриц друг на друга
    for j in range(n):
        for l in range(n):
            KFA[i][j] += KF[i][l] * A[l][j]
print("\nРезультат умножения матрицы KF на матрицу A:")
printMatrix(KFA)


AT = [[0 for i in range(n)] for j in range(n)]          # заготовка под транспонированную матрицу A
for i in range(n):  # произведение транспонирования матрицы A
    for j in range(n):
        AT[i][j] = A[j][i]
print("\nМатрица A транспонированная:")
printMatrix(AT)


KAT = [[0 for i in range(n)] for j in range(n)]
for i in range(n):  # умножегие транспонированной матрицы А на кэфф К
    for j in range(n):
        KAT[i][j] = AT[i][j] * k
print("\nРезультат умножения коэффициента K на матрицу AT:")
printMatrix(KAT)


matrix_result = [[0 for i in range(n)] for j in range(n)]      # заготовка под конечный результат
for i in range(n):              #разность между двух матриц
    for j in range(n):
        matrix_result[i][j] = KFA[i][j] - KAT[i][j]
print("\nКонечный результат KFA - KAT:")
printMatrix(matrix_result)

print("\nThe work of the program is completed")
