import numpy as np
import scipy.linalg


A = np.array([
    [2,1,1],
    [4,3,3],
    [8,7,9]
], dtype=float)

b = np.array([2,8,12])

e21 = np.eye(3) # Строим единичную матрицу
e21[1,0] = -2 # Заменяем элемент во второй строке и первый столбец на -2
step1 = e21@A
print(f'Матрица после первого шага:\n {step1}')

e31 = np.eye(3)
e31[2,0]= -4
step2 = e31@(e21@A)
print(f'Матрица после второго шага:\n {step2}')

e32 = np.eye(3)
e32[2,1] = -3
step3 = e32@(e31@(e21@A))
print(f'Матрица после третьего шага:\n'
      f' U = {step3}')
c = e32@(e31@(e21@b))
result = scipy.linalg.solve_triangular(step3, c)
print(f'Итоговое решение:\n {result}')