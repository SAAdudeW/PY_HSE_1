# -*- coding: utf-8 -*-
"""Шалагинов_БПМ214_Numpy_hw_к_04_04.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gPUT21CXlJKnrTk2p4naS-JQt7tkk_fq

# `Python` в науке и инженерии

## Домашнее задание 1. `Numpy`

Правила выполнения работы:

- Решение каждой задачи должно располагаться в **ячейке типа "Код" под ячейкой с условием задачи**
- **Результат** каждой задачи должен быть **выведен на экран**
- **Запрещено** изменять ячейки с условиями задач каким-либо образом и перемещать их
- Все задачи должны быть решены с использованием **векторизации**
- Если в условии задачи не сказано иное, **не допускается** применение циклов `for`, `while`, генераторов списков и любых других циклов и их заменителей, не входящих в `numpy`
- **В квадратных скобках** в конце условия задачи указано **количество баллов** за корректное выполнение этой задачи


Полезные документы:

- [Numpy Cheat Sheet](https://s3.amazonaws.com/assets.datacamp.com/blog_assets/Numpy_Python_Cheat_Sheet.pdf)
- [Scientific Python Lectures / Numpy](https://github.com/jrjohansson/scientific-python-lectures/blob/master/Lecture-2-Numpy.ipynb)
- [Matplotlib Cheat Sheet](https://s3.amazonaws.com/assets.datacamp.com/blog_assets/Python_Matplotlib_Cheat_Sheet.pdf)

---

**1. Импортировать модуль `numpy` под именем `np` [1]**
"""

import numpy as np

"""**2. Сгенерировать одномерный целочисленный массив от 5 до 50 включительно с шагом 5 [2]**"""

np.arange(5, 51, 5)

"""**3. Сгенерировать двумерный целочисленный массив от 100 до 1 включительно [2]**"""

np.arange(100, 0, -1).reshape(10, 10)

"""**4. Сгенерировать одномерный массив `x` и найти все `dx[i] = x[i+1] - x[i]` [3]**"""

x = np.arange(20)
x[1:] - x[0:-1]

"""**5. Сгенерировать одномерный массив `x` длины 20 и найти разницу между элементами с четными и нечетными индексами [4]**"""

# разница между соседними четным и нечетным
x = np.arange(20)
x[0::2] - x[1::2]

"""**6. Сгенерировать одномерные массивы `x, y`, содержащие координаты 360 точек, расположенных равномерно на единичной окружности. Объединить их в один двумерный массив размера (360, 2) [5]**"""

x = np.cos(np.radians(np.arange(0, 360, 1)))
y = np.sin(np.radians(np.arange(0, 360, 1)))
np.column_stack((x, y))

"""**7. Сгенерировать массив формы (100, 2), содержащий координаты точек, расположенных на плоскости случайно. Найти точки: ближайшую и самую дальнюю по отношению к началу координат [5]**

Полезные функции для решения задачи:

`np.linalg.norm`, `np.argmin`, `np.argmax`
"""

np.random.seed(0)
a7 = np.random.rand(200).reshape(100, 2)
a7 = np.linalg.norm(a7, axis=1)
np.argmin(a7), np.argmax(a7)

"""**8. Создать двумерный массив размера (n, n) из нулей и единиц, расположенных в шахматном порядке [5]**"""

n =  int(input())
a8 = np.zeros((n, n), dtype=int)
a8[0::2, 0::2] = 1
a8[1::2, 1::2] = 1
a8

"""**9. Создать двумерный массив и выбрать из него элементы согласно рисунку [4]**
![](hw_slice_01.png)
"""

a9 = np.arange(36).reshape(6, 6)
a9[1:-1, 1: -1]

"""**10. Создать двумерный массив и выбрать из него элементы согласно рисунку [4]**
![](hw_slice_02.png)
"""

a10 = np.arange(36).reshape(6, 6)
a10[1::2,0::5]

"""**11. Создать двумерный массив и выбрать из него элементы согласно рисунку [6]**
![](hw_slice_03.png)
"""

# сумма квадратов индексов не больше 256
a11 = np.arange(400).reshape(20, 20)
b = c = np.arange(20)
# первая строка
a11, a11[0, b**2 + c[0]**2 <= 256]

"""**12. Создать трехмерный массив и выбрать из него элементы согласно рисунку [4]**
![](hw_slice_04.png)
"""

a12 = np.arange(125).reshape(5, 5, 5)
a12[::2,1:-1, 1::3]

"""**13. Сгенерировать массив `pts` размера (4, 2) из случайных чисел, равномерно распределенных в полуинтервале [0, 10). Считая, что массив хранит координаты точек на плоскости, провести через первую и вторую пару точек прямые и найти координаты точки их пересечения [5]**

Полезные функции для решения задачи:

`np.linalg.det`, `np.linalg.solve`
"""

rng = np.random.default_rng(0)
pts = rng.uniform(0, 10, (4, 2))
# поиск k1, b1 для первой прямой k1*x+b1=y
S1 = np.linalg.solve([[pts[0, 0], 1], [pts[1, 0], 1]], [pts[0, 1], pts[1, 1]])
# поиск k2, b2 для второй прямой k2*x+b2=y
S2 = np.linalg.solve([[pts[2, 0], 1], [pts[3, 0], 1]], [pts[2, 1], pts[3, 1]])
# система из 2 уравнений для поиска точки пересечения (k1-k2)x+0*y=b2-b1, k1x-y=-b1
S = np.array([[S1[0] - S2[0], 0], [S1[0], -1]])
np.linalg.solve(S, [S2[1] - S1[1], -S1[1]])

"""---

**14. Загрузить массив из файла `array.txt` и дать ему имя `arr`. В массиве `arr` расположены координаты концов векторов $v_i$, начало которых находится в точке (0, 0). [1]**
"""

arr = np.loadtxt('array.txt')
arr

"""**15. Посчитать углы в градусах между $v_i$ и $v_{i+1}$ векторами для всех $i$ [5]**"""

#  угол = арккосинус частного скалярного произведения и произведения длин векторов
# np.arccos(np.dot(arr[0:-1], arr[1:]) / (np.linalg.norm(arr[0:-1]) * np.linalg.norm(arr[1:])))
np.degrees(np.arccos((arr[0:-1, 0] * arr[1:, 0] + arr[0:-1, 1] * arr[1:, 1]) / (np.linalg.norm(arr[0:-1]) * np.linalg.norm(arr[1:]))))

"""**16. Повернуть векторы $v_i$ на угол 30 градусов против часовой стрелки для всех $i$ [5]**"""

M = np.array([[np.cos(np.pi/6),  -np.sin(np.pi/6)], [np.sin(np.pi/6), np.cos(np.pi/6)]])
a16 = np.matmul(arr[0:], M)
a16

"""---

**17. Загрузить массивы из файлов `nodes.txt` и `triangles.txt` и дать им имена `nodes` и `tris`. Массив `tris` должен содержать целые числа [1]**
"""

nodes = np.loadtxt('nodes.txt')
tris = np.loadtxt('triangles.txt', int)
nodes, tris

"""**18. В массиве `nodes` расположены координаты точек на плоскости, а в массиве `tris` хранятся тройки индексов `(i, j, k)` такие, что точки с индексами $i, j, k$ из массива `nodes` образуют треугольник. Посчитать геометрические центры и площади всех треугольников [7]**

Полезные функции для решения задачи:

`np.mean`, `np.cross`, `'fancy indexing'`
"""

# массив с координатами первой стороны треугольников
i = (nodes[tris][0:, 0] - nodes[tris][0:, 1])
# массив с координатами второй стороны треугольников
j = (nodes[tris][0:, 0] - nodes[tris][0:, 2])
# площадь треугольника = половина модуля векторного произведения пары сторон
s = abs(np.cross(i, j)) * 0.5
s

# геометрический центр = точка пересечения медина

"""---

Для построения графика в следующих задачах можно воспользоваться функцией `plot` из модуля `matplotlib` (см. [Matplotlib Cheat Sheet](https://s3.amazonaws.com/assets.datacamp.com/blog_assets/Python_Matplotlib_Cheat_Sheet.pdf))

---

**19. В файле `stm.npy` хранится трехмерный массив, в который уложены матрицы $S_i$ размером (6, 6). Изобразить график максимального [аргумента](https://ru.wikipedia.org/wiki/Комплексное_число#Аргумент) собственных чисел матрицы $S_i$ в зависимости от $i$ [7]**

Полезные функции для решения задачи:

`np.load`, `np.linalg.eigvals`, `np.max`, `np.angle`, `np.degrees`, `plt.plot`
"""

nodes[tris]

"""**20. В файле `signal.txt` содержится запись зашумленного сигнала. Используя быстрое преобразование Фурье восстановить исходный сигнал. Вывести на экран частоты восстановленного сигнала. Изобразить исходный и восстановленный сигналы на одном графике [7]**

Полезные функции для решения задачи:

`np.loadtxt`, `np.fft.rfft`, `np.fft.irfft`, `np.where`, `plt.plot`
"""



"""**21. Методом интегрирования Монте-Карло оценить площадь под графиком функции $f(x) = \sin(x)$ на отрезке $[0, \pi]$. Оценить зависимость погрешности такой оценки от $N \in [10, 1000]$ и изобразить график этой зависимости (в этой части задачи можно использовать один цикл) [7]**

Согласно методу интегрирования Монте-Карло $\int_a^b{f(x)dx} \approx \frac{b - a}{N} \sum_{i=1}^N{f(u_i)}$, где $u_i$ - $N$ случайных равномерно распределенных на отрезке $[a, b]$ чисел.

Полезные функции для решения задачи:

`np.arange`, `np.linspace`, `np.sin`, `np.sum`, `plt.plot`
"""



"""**22. В файле `lsq.txt` находятся результаты измерений $(t_j, x_j)$, $j=1\ldots n$. Найти коэфициенты $a$ и $b$ прямой, которая наилучшим образом аппроксимирует эти данные, используя метод наименьших квадратов (МНК). Проверить результаты при помощи функции `np.linalg.lstsq`. Изобразить результаты измерений и рассчитанную прямую на одном графике. [10]**

Согласно МНК, коэффициенты $a, b$ можно найти, решив систему уравнений:

$\begin{pmatrix}
\sum_{j=1}^{n}t_j^2 & \sum_{j=1}^nt_j\\
\sum_{j=1}^nt_j & \sum_{j=1}^n 1 
\end{pmatrix}\begin{pmatrix}a\\b\end{pmatrix}=\begin{pmatrix}\sum_{j=1}^{n}t_jx_j\\ \sum_{j=1}^{n}x_j\end{pmatrix}$

Полезные функции для решения задачи:

`np.loadtxt`, `np.ones_like`, `np.dot`, `@`, `np.column_stack`, `np.linalg.leastsq`, `plt.plot`
"""



"""---
---
"""