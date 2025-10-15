import matplotlib.pyplot as plt

Nilakantha_iter = [1, 2, 6, 13, 29, 58, 94, 115]
Madhava_iter = [1, 5, 9, 16, 20, 41, 50, 85]
BBP_iter = [1, 1, 1, 2, 3, 4, 5, 12]


Nilakantha_pi = [3.0000000, 3.1666667, 3.1427128, 3.1414797, 3.1415827, 3.1415942, 3.1415932, 3.1415930]
Madhava_pi = [3.4641016, 3.1426048, 3.1415997, 3.1415927, 3.1415927, 3.1415927, 3.1415927, 3.1415927]
BBP_pi = [3.1333332, 3.1333332, 3.1333332, 3.1414223, 3.1415873, 3.1415923, 3.1415925, 3.1415925]

true_pi = 3.141592653589793

plt.figure(figsize=(12, 8))

plt.semilogx(Nilakantha_iter, Nilakantha_pi, label='Нилаканта', linewidth=2)
plt.semilogx(Madhava_iter, Madhava_pi,  label='Мадхава', linewidth=2)
plt.semilogx(BBP_iter, BBP_pi,  label='BBP', linewidth=2)
plt.axhline(y=true_pi, color='black', linestyle='--', label='Точное значение')

plt.xlabel('Количество итераций', fontsize=12)
plt.ylabel('Вычисленное π', fontsize=12)
plt.title('Зависимость вычисленного π от количества итераций для "быстрых" формул', fontsize=14)
plt.grid()
plt.legend(fontsize=12)
plt.xlim(1e0, 1e3)
plt.tight_layout()
plt.show()
