print('Подсчет уравнения по формуле x = 7*b + 2*c - a')
print('Введите число a')
a=input()
print('Введите число b')
b=input()
print('Введите число c')
c=input()
if a.isdigit() and b.isdigit() and c.isdigit():
    a=int(a)
    b=int(b)
    c=int(c)
    x=7*b + 2*c - a
    print(f'Результат: {x}')
else:
    print('Неверно введенные данные, введите простое целое число')