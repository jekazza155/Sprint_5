from random import randint

class Person:
    user_name = 'Евгений'
    email = f'jekazza15@gmail.com'
    password = f'12332Aa'

class RandomData:
    user_name = 'Фрося'
    email = f'test{randint(0, 999)}@gmail.com'
    password = f'{randint(1000, 9999)}Aa'