import numpy as np
import matplotlib.pyplot as plt

# Столбцы - это влияние различных видов рекламных каналов (на ТВ, в соцсетях, и контекстная реклама)

# Влияние ТВ-рекламы на сегменты: [2, 3, 5]
# Влияние рекламы в соцсетях: [1, 1, 7]
# Влияние контекстной рекламы: [3, 4, 2]

A = np.array([
    [2, 1, 3],
    [3, 1, 4],
    [5, 7, 2]
])

# Целевой охват [10,14,24] - b

b = np.array([10, 14, 24])

result_matrix = np.linalg.solve(A, b)
col1=A[:,0]
col2=A[:,1]
col3=A[:,2]
b_check = result_matrix[0]*col1 + result_matrix[1]*col2 + result_matrix[2]*col3
print(f'Линейная комбинация:{b_check}')
#Результат [3,1,1] -> b = 3*col_1 + col_2 + col_3
#Таким образом, для того, чтобы достичь максимальной эффективности рекламы,
#необходимо 60% всего бюджета, выделенного на рекламную компанию, вложить в ТВ рекламу,
# и по 20% на рекламу в соцсетях и контекстную рекламы

#Визуализация
fig = plt.figure(figsize=(14,10))

ax1 = fig.add_subplot(121, projection='3d')
origin = [0,0,0]
ax1.quiver(origin[0], origin[1], origin[2], b[0], b[1], b[2], color='red', label=f'Целевой охват {b}')
ax1.quiver(origin[0],origin[1],origin[2],col1[0], col1[1],col1[2], color = 'blue', label=f'Тв реклама {col1}')
ax1.quiver(origin[0],origin[1],origin[2],col2[0], col2[1],col2[2], color = 'green', label=f'соцсети {col2}')
ax1.quiver(origin[0],origin[1],origin[2],col3[0], col3[1],col3[2], color = 'orange', label=f'Контекстная {col3}')

ax1.legend()
ax1.grid(True)
plt.show()