# 1 задача

# import math
# n = 700
# m = 400
# print (math.ceil(m/n))

# import os
# os.system('cls')
# n = int(input('Input number n = '))
# m = int(input('Input number m = '))

# print(f"Дней чтобы проехать километров = ", ((m+n+1)//n))

# 2 задача

# a = int(input('Введите число учеников в 1 классе: '))
# b = int(input('Введите число учеников в 2 классе: '))
# c = int(input('Введите число учеников в 3 классе: '))
# print(f"Наименьшее число парт = ",int((a+a%2+b+b%2+c+c%2)/2))


# 3 задача
# Дано натуральное число. Требуется определить, является ли год с данным номером високосным. 
# Если год является високосным, то выведите YES, иначе выведите NO. Напомним, что в соответствии 
# с григорианским календарем, год является високосным, если его номер кратен 4, но не кратен 100, а также если он кратен 400.
# Input: 2016
# Output: YES

# n = int(input('Введите год: '))
# if ((n%4 == 0) and (n%100 != 0)) or (n%400 == 0)):
#     print ('Yes')
# else:
#     print ('No')



num =10
res = 'yes' if num > 50 else 'no'
print(res)