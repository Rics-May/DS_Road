import numpy as np

# Пример системы из лекции
A = np.array([[1, 2, 1],
              [3, 8, 1],
              [0, 4, 1]], dtype=float)
b = np.array([2, 12, 2], dtype=float)

# 1. Forward Elimination (Упрощенно, без pivot swapping)
rows, cols = A.shape
for j in range(cols):  # по столбцам
    pivot = A[j, j]
    if pivot == 0: raise ValueError("Zero pivot encountered")

    for i in range(j + 1, rows):  # по строкам ниже
        multiplier = A[i, j] / pivot
        # Элиминация в A и в b одновременно
        A[i, :] = A[i, :] - multiplier * A[j, :]
        b[i] = b[i] - multiplier * b[j]

print("Верхнетреугольная матрица U:\n", A)
print("Преобразованный вектор c:\n", b)

# 2. Back Substitution (встроенная функция делает это эффективно)
x = np.linalg.solve(A, b)  # Решаем уже упрощенную систему, или исходную
print("Решение x:", x)