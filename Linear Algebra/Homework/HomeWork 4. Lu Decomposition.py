import numpy as np
import scipy.linalg
from scipy.linalg import lu
# Данные матрицы
A = np.array([
    [2,4,-2],
    [4,9,-3],
    [-2,-3,7]
], dtype=np.float64)

b = np.array([2,8,10])
# Задаем единичную матрицу как заготовку для L
L = np.eye(3)
# Алгоритм в ручную
l21 = A[1]-2*A[0]
L[1,0] = 2
l31 = A[0] + A[2]
L[2,0] = -1
U = A.copy()
U[1]=U[1]-2*U[0]
U[2] = U[2]--(1)*U[0]
print(U)

l32 = A[1] - A[2]
L[2,1] = 1
print(L)
U[2] = U[2] - 1* U[1]
print(L@U)
# 2. Использование SciPy
P,L_scipy,U_scipy = lu(A)
print (f'Матрица L через Scipy,{L_scipy}')
print(f'Матрица U через scipy,{U_scipy}')
print(P@L_scipy@U_scipy)

#3 Решение системы через LU
print('Решение системы')
y = scipy.linalg.solve_triangular(L,b,lower=True)
x = scipy.linalg.solve_triangular(U,y,lower=False)
print(x)
print(np.linalg.solve(A,b))