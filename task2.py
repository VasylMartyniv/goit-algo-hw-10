import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi


def f(x):
    return x ** 2


a = 0
b = 2

N = 10000

x_random = np.random.uniform(a, b, N)
y_random = np.random.uniform(0, f(b), N)

points_under_curve = y_random < f(x_random)
integral_approximation = (b - a) * f(b) * np.sum(points_under_curve) / N

result, error = spi.quad(f, a, b)

print(f"Оцінка інтеграла методом Монте-Карло: {integral_approximation}")
print("Точне значення інтеграла (quad):", result)
print("Абсолютна похибка:", error)
print(f"Різниця між оцінкою Монте-Карло та точним значенням: {abs(integral_approximation - result)}")

x = np.linspace(-0.5, 2.5, 400)
y = f(x)

fig, ax = plt.subplots()

ax.plot(x, y, 'r', linewidth=2)

ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

ax.scatter(x_random[points_under_curve], y_random[points_under_curve], color='blue', s=1, label='Точки під кривою')
ax.scatter(x_random[~points_under_curve], y_random[~points_under_curve], color='red', s=1, label='Точки над кривою')

ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.5])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Метод Монте-Карло для обчислення інтеграла')
plt.legend()
plt.grid()
plt.show()
