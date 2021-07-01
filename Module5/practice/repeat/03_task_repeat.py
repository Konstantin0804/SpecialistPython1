# Найдите количество чисел являющихся палиндромами в диапазоне от a до b включительно
# Известно, что a и b целые положительные числа.

a = ...
b = ...

def palindrome(number):
    n_str = str(number)
    n_rev = n_str[::-1]
    return n_str == n_rev

a = 145
b = 1690
count = 0
my_list=list(range(a,b))
for i in my_list:
    if palindrome(i) :
        count += 1
print(f"{count} палиндромов между {a} и {b}")
