import matplotlib.pyplot as plt

err_Leibniz = [0.1107731, 0.0100002, 0.0010002, 0.0001011, 0.0000181, 0.0000076, 0.0000067, 0.0000067]
err_Wallis = [0.1029181, 0.0101171, 0.0010009, 0.0002432, 0.0002432, 0.0002432, 0.0002432, 0.0002432]
err_Nilakantha = [0.1415927, 0.0250740, 0.0011201, 0.0001130, 0.0000100, 0.0000014, 0.0000005, 0.0000002]
err_Madhava = [0.3225088, 0.0010121 , 0.0000069, 0.0000000, 0.0000000, 0.0000000, 0.0000000, 0.0000000]
err_BBP = [0.0082595, 0.0082595, 0.0082595, 0.0001705, 0.0000055, 0.0000005, 0.0000002, 0.0000002]

Leibniz_time = [5e-07, 8e-07, 7.2e-06, 6.74e-05, 5.04e-04, 1.7774e-03, 2.9837e-03, 2.1446e-03]
Wallis_time = [2e-07, 9e-07, 9e-06, 2.34e-05, 2.35e-05, 2.35e-05, 2.55e-05, 2.36e-05]
Nilakantha_time = [1e-07, 1e-07, 2e-07, 2e-07, 2e-07, 5e-07, 9e-07, 8e-07]
Madhava_time = [6.7e-06, 4.7e-06, 7e-07, 8e-07, 8e-07, 2.3e-06, 4.6e-06, 3.4e-06]
BBP_time = [2e-07, 1e-07, 1e-07, 2e-07, 2e-07, 3e-07, 5e-07, 7e-07]
# tolerances = [0.1, 0.01, 0.001, 0.0001, 0.00001, 0.000001, 0.0000001, 0.00000001]
min_error = 1e-20
errors_Madhava = [max(err, min_error) for err in err_Madhava]

plt.figure(figsize=(12, 8))

plt.loglog(err_Leibniz, Leibniz_time, 'o-', label='Лейбниц', linewidth=2, markersize=8)
plt.loglog(err_Wallis, Wallis_time, '^-', label='Валлис', linewidth=2, markersize=8)
plt.loglog(err_Nilakantha, Nilakantha_time, 'v-', label='Нилаканта', linewidth=2, markersize=8)
plt.loglog(errors_Madhava, Madhava_time, 's-', label='Мадхава', linewidth=2, markersize=8)
plt.loglog(err_BBP, BBP_time, 'd-', label='BBP', linewidth=2, markersize=10)

plt.xlabel('Ошибка вычисления π', fontsize=14)
plt.ylabel('Количество итераций', fontsize=14)
plt.title('Зависимость времени сходимости к точному значению от ошибки для разных формул π \n (двойной логарифмический масштаб)', fontsize=15,fontweight='bold')
plt.grid()
plt.legend(fontsize=12)

plt.xlim(1e0, 1e-7)

plt.gca().invert_xaxis()
plt.tight_layout()
plt.show()