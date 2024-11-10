def dec_to_thirteen(n):
 
 digits = '0123456789ABCDEF'
 thirteen_digits = ''
 
 while n > 0:
  remainder = n % 13
  thirteen_digits = digits[remainder] + thirteen_digits 
  n //= 13
 return thirteen_digits
print("Введите положитнел")
x=input()
if x.isdigit():
    
    thirteen_num = dec_to_thirteen(x)
    print(f'Тринадцатеричное представление числа {x}: {thirteen_num}')
else:
    print('Неверно введенные данные, введите простое целое число')