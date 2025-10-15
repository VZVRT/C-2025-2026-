import matplotlib.pyplot as plt

Leibniz_iter = [9, 100, 1000, 9354, 69957, 227569, 293567, 295861]
Wallis_iter = [8, 78, 787, 2049, 2049, 2049, 2049, 2049]
Nilakantha_iter = [1, 2, 6, 13, 29, 58, 94, 115]
Madhava_iter = [1, 5, 9, 16, 20, 41, 50, 85]
BBP_iter = [1, 1, 1, 2, 3, 4, 5, 12]

Leibniz_pi = [3.2523658, 3.1315925, 3.1405926, 3.1414917, 3.1416109, 3.1416004, 3.1415994, 3.1415994]
Wallis_pi = [3.0386746, 3.1314757, 3.1405919, 3.1413496, 3.1413496, 3.1413496, 3.1413496, 3.1413496]
Nilakantha_pi = [3.0000000, 3.1666667, 3.1427128, 3.1414797, 3.1415827, 3.1415942, 3.1415932, 3.1415930]
Madhava_pi = [3.4641016, 3.1426048, 3.1415997, 3.1415927, 3.1415927, 3.1415927, 3.1415927, 3.1415927]
BBP_pi = [3.1333332, 3.1333332, 3.1333332, 3.1414223, 3.1415873, 3.1415923, 3.1415925, 3.1415925]

true_pi = 3.141592653589793


osc_iter = [1, 10, 50, 100, 500, 1000, 5000, 10000, 50000, 100000]
osc_pi = [3.24159265, 3.13159265, 3.15159265, 3.13159265, 3.24159265, 3.13159265, 3.15159265, 3.13159265, 3.14659265, 3.13659265]

fig, axes = plt.subplots(2, 3, figsize=(18, 10))
axes = axes.flatten()

axes[0].semilogx(Leibniz_iter, Leibniz_pi, color='blue', linewidth=2)
axes[0].axhline(y=true_pi, color='black', linestyle='--',  label='Точное значение')
axes[0].set_xlabel('Количество итераций')
axes[0].set_ylabel('Вычисленное π')
axes[0].set_title('Формула Лейбница')
axes[0].grid()
axes[0].legend()

axes[1].semilogx(Wallis_iter, Wallis_pi, color='green', linewidth=2)
axes[1].axhline(y=true_pi, color='black', linestyle='--',  label='Точное значение')
axes[1].set_xlabel('Количество итераций')
axes[1].set_ylabel('Вычисленное π')
axes[1].set_title('Формула Валлиса')
axes[1].grid()
axes[1].legend()

axes[2].semilogx(Nilakantha_iter, Nilakantha_pi, color='orange', linewidth=2)
axes[2].axhline(y=true_pi, color='black', linestyle='--',  label='Точное значение')
axes[2].set_xlabel('Количество итераций')
axes[2].set_ylabel('Вычисленное π')
axes[2].set_title('Формула Нилаканты')
axes[2].grid()
axes[2].legend()

axes[3].semilogx(Madhava_iter, Madhava_pi, color='yellow', linewidth=2)
axes[3].axhline(y=true_pi, color='black', linestyle='--',  label='Точное значение')
axes[3].set_xlabel('Количество итераций')
axes[3].set_ylabel('Вычисленное π')
axes[3].set_title('Формула Мадхавы')
axes[3].grid()
axes[3].legend()

axes[4].semilogx(BBP_iter, BBP_pi, color='#00CDCD', linewidth=2)
axes[4].axhline(y=true_pi, color='black', linestyle='--',  label='Точное значение')
axes[4].set_xlabel('Количество итераций')
axes[4].set_ylabel('Вычисленное π')
axes[4].set_title('Формула BBP')
axes[4].grid()
axes[4].legend()

axes[5].semilogx(osc_iter, osc_pi, '*-', color='violet', linewidth=2, markersize=6)
axes[5].axhline(y=true_pi, color='black', linestyle='--',  label='Точное значение')
axes[5].set_xlabel('Количество итераций')
axes[5].set_ylabel('Вычисленное π')
axes[5].set_title('Колебательная формула')
axes[5].grid()
axes[5].legend()

plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 8))

plt.semilogx(Leibniz_iter, Leibniz_pi, label='Лейбниц', linewidth=2)
plt.semilogx(Wallis_iter, Wallis_pi, label='Валлис', linewidth=2)
plt.semilogx(Nilakantha_iter, Nilakantha_pi, label='Нилаканта', linewidth=2)
plt.semilogx(Madhava_iter, Madhava_pi,  label='Мадхава', linewidth=2)
plt.semilogx(BBP_iter, BBP_pi,  label='BBP', linewidth=2)
plt.semilogx(osc_iter, osc_pi,  label='Колебательная', linewidth=2)
plt.axhline(y=true_pi, color='black', linestyle='--', label='Точное значение')

plt.xlabel('Количество итераций', fontsize=12)
plt.ylabel('Вычисленное π', fontsize=12)
plt.title('Зависимость вычисленного π от количества итераций для различных формул', fontsize=14)
plt.grid()
plt.legend(fontsize=12)

plt.tight_layout()
plt.show()
