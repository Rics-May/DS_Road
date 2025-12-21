import numpy as np

# 1. Умножение матриц
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Стандартный оператор (Python 3.5+) для умножения матриц
C = A @ B
# Или np.dot(A, B)
print(f"A * B =\n{C}")

# 2. Обратная матрица
# Проверка на вырожденность (определитель не 0)
if np.linalg.det(A) != 0:
    A_inv = np.linalg.inv(A)
    print(f"Inverse of A =\n{A_inv}")

    # Проверка: A * A_inv должно быть близко к I
    Identity_check = A @ A_inv
    print(f"Check (should be I) =\n{Identity_check}")
else:
    print("Матрица сингулярна")

# 3. Пример сингулярной матрицы (строки зависимы)
Singular_A = np.array([[1, 3], [2, 6]])
# np.linalg.inv(Singular_A) # Вызовет ошибку LinAlgError