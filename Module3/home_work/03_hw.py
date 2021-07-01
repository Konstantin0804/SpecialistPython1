# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -100 до 100.
# Вывести на экран сумму всех положительных элементов кратных двум.

# TODO: your code here
import random
numbers = []
n = int(input("Введите n:"))
i = 1
sum = 0
while i <= n:
    numbers.append(random.randint(-100,100))
    i += 1
for el in numbers:
    if el > 0:
        if el % 2 ==0:
            sum += el
print(sum)
