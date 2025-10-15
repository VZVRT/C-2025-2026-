import matplotlib.pyplot as plt

Leibniz_iter = [9, 100, 1000, 9354, 69957, 227569, 293567, 295861]
Wallis_iter = [8, 78, 787, 2049, 2049, 2049, 2049, 2049]


Leibniz_pi = [3.2523658, 3.1315925, 3.1405926, 3.1414917, 3.1416109, 3.1416004, 3.1415994, 3.1415994]
Wallis_pi = [3.0386746, 3.1314757, 3.1405919, 3.1413496, 3.1413496, 3.1413496, 3.1413496, 3.1413496]


true_pi = 3.141592653589793


osc_iter = [1, 10, 50, 100, 500, 1000, 5000, 10000, 50000, 100000]
osc_pi = [
    3.24159265,
    3.13159265,
    3.15159265,
    3.13159265,
    3.24159265,
    3.13159265,
    3.15159265,
    3.13159265,
    3.14659265,
    3.13659265,

]
plt.figure(figsize=(12, 8))

plt.semilogx(Leibniz_iter, Leibniz_pi, label='Лейбниц', linewidth=2)
plt.semilogx(Wallis_iter, Wallis_pi, label='Валлис', linewidth=2)
plt.semilogx(osc_iter, osc_pi,  label='Колебательная', linewidth=2)
plt.axhline(y=true_pi, color='black', linestyle='--', label='Точное значение')

plt.xlabel('Количество итераций', fontsize=12)
plt.ylabel('Вычисленное π', fontsize=12)
plt.title('Зависимость вычисленного π от количества итераций для "медленных" и "колебательной" формул', fontsize=14)
plt.grid()
plt.legend(fontsize=12)

plt.tight_layout()
plt.show()
