import matplotlib.pyplot as plt

Leibniz_iter = [9, 100, 1000, 9354, 69957, 227569, 293567, 295861]
Wallis_iter = [8, 78, 787, 2049, 2049, 2049, 2049, 2049]
Nilakantha_iter = [1, 2, 6, 13, 29, 58, 94, 115]
Madhava_iter = [1, 5, 9, 16, 20, 41, 50, 85]
BBP_iter = [1, 1, 1, 2, 3, 4, 5, 12]
err_Leibniz = [0.1107731, 0.0100002, 0.0010002, 0.0001011, 0.0000181, 0.0000076, 0.0000067, 0.0000067]
err_Wallis = [0.1029181, 0.0101171, 0.0010009, 0.0002432, 0.0002432, 0.0002432, 0.0002432, 0.0002432]
err_Nilakantha = [0.1415927, 0.0250740, 0.0011201, 0.0001130, 0.0000100, 0.0000014, 0.0000005, 0.0000002]
err_Madhava = [0.3225088, 0.0010121 , 0.0000069, 0.0000000, 0.0000000, 0.0000000, 0.0000000, 0.0000000]



plt.figure(figsize=(12, 8))

plt.semilogx(Leibniz_iter, err_Leibniz, label='Лейбниц', linewidth=2)
plt.semilogx(Wallis_iter, err_Wallis, label='Валлис', linewidth=2)
plt.semilogx(Nilakantha_iter, err_Nilakantha, label='Нилаканта', linewidth=2)
plt.semilogx(Madhava_iter, err_Madhava,  label='Мадхава', linewidth=2)
plt.semilogx(BBP_iter, err_Nilakantha,  label='BBP', linewidth=2)

plt.xlabel('Количество итераций', fontsize=12)
plt.ylabel('Ошибка', fontsize=12)
plt.title('Зависимость ошибки от количества итераций для различных формул', fontsize=14)
plt.grid()
plt.legend(fontsize=12)

plt.tight_layout()
plt.show()
