# Домашнє завдання: Обчислення інтегралу методом Монте-Карло

## Опис завдання

Метою даного завдання було обчислити визначений інтеграл функції за допомогою методу Монте-Карло та порівняти отриманий
результат з аналітичним рішенням, знайденим за допомогою функції `quad` з бібліотеки SciPy.

## Опис алгоритму

- Функція для інтегрування: \( f(x) = x^2 \)
- Інтервал інтегрування: [0, 2]
- Використовуваний метод: метод Монте-Карло
- Порівняння результатів з функцією `quad` для перевірки точності.

## Результати

1. Оцінка інтеграла методом Монте-Карло: 2.6456
2. Точне значення інтеграла (quad): 2.6666666666666665
3. Різниця між оцінкою Монте-Карло та точним значенням: 0.021066666666666567

## Висновки

Метод Монте-Карло забезпечує наближення до точного значення інтеграла, і його точність залежить від кількості випадкових
точок. Використання методу Монте-Карло є доцільним у випадках, коли аналітичне обчислення інтегралу є складним або
неможливим.