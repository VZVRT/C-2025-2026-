import matplotlib.pyplot as plt

err_Leibniz = [0.1107731, 0.0100002, 0.0010002, 0.0001011, 0.0000181, 0.0000076, 0.0000067, 0.0000067]
err_Wallis = [0.1029181, 0.0101171, 0.0010009, 0.0002432, 0.0002432, 0.0002432, 0.0002432, 0.0002432]
err_Nilakantha = [0.1415927, 0.0250740, 0.0011201, 0.0001130, 0.0000100, 0.0000014, 0.0000005, 0.0000002]
err_Madhava = [0.3225088, 0.0010121 , 0.0000069, 0.0000000, 0.0000000, 0.0000000, 0.0000000, 0.0000000]
err_BBP = [0.0082595, 0.0082595, 0.0082595, 0.0001705, 0.0000055, 0.0000005, 0.0000002, 0.0000002]

Leibniz_iter = [9, 100, 1000, 9354, 69957, 227569, 293567, 295861]
Wallis_iter = [8, 78, 787, 2049, 2049, 2049, 2049, 2049]
Nilakantha_iter = [1, 2, 6, 13, 29, 58, 94, 115]
BBP_iter = [1, 1, 1, 2, 3, 4, 5, 12]
Madhava_iter = [1, 5, 9, 16, 20, 41, 50, 85]
min_error = 1e-20
errors_Madhava = [max(err, min_error) for err in err_Madhava]

plt.figure(figsize=(12, 8))

plt.loglog(err_Leibniz, Leibniz_iter, 'o-', label='Лейбниц', linewidth=2, markersize=8)
plt.loglog(err_Wallis, Wallis_iter, '^-', label='Валлис', linewidth=2, markersize=8)
plt.loglog(err_Nilakantha, Nilakantha_iter, 'v-', label='Нилаканта', linewidth=2, markersize=8)
plt.loglog(errors_Madhava, Madhava_iter, 's-', label='Мадхава', linewidth=2, markersize=8)
plt.loglog(err_BBP, BBP_iter, 'd-', label='BBP', linewidth=2, markersize=10)

plt.xlabel('Ошибка вычисления π', fontsize=14)
plt.ylabel('Количество итераций', fontsize=14)
plt.title('Зависимость количества итераций от ошибки для различных формул π \n (двойной логарифмический масштаб)', fontsize=16,fontweight='bold')
plt.grid()
plt.legend(fontsize=12)

plt.xlim(1e0, 1e-7)

plt.gca().invert_xaxis()
plt.tight_layout()
plt.show()