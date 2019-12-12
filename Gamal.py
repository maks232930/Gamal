import random

arr = ['&', 'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У',
       'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я', ' ', '1', '2', '3', '4', '5', '6', '7', '8', '9',
       '0']


def generator(m):
    kod = []
    for i in m:
        i = i.title()
        kod.append(arr.index(i))
    print(kod)

    p = 0
    while True:
        p = random.randint(10, 1000)
        a = p - 2
        if ((a ** p) % p) == a % p:
            break
    print(f'p = {p}')

    while True:
        g = random.randint(1, 1000)
        if int(((g ** p - 1) % p)) == 1 and g < p - 1:
            print(f'g = {g}')
            break

    while True:
        x = random.randint(1, 1000)
        if (x > 1) and (x < p - 1):
            print(f'x = {x}')
            break
    y = (g ** x) % p
    print(f'y = {y}')

    # начинается шифровка

    while True:
        k = random.randint(1, 1000)
        t = k - 2
        if k > 1 and k < p - 1 and ((t ** k) % k) == t % k:
            print(f'k = {k}')
            break

    a = (g ** k) % p
    print(f'a = {a}')
    shifr = []
    for i in kod:
        b = int(i * ((y ** k) % p))
        shifr.append(b)

    shifr = str(shifr)
    shifr = shifr.replace(',', '')
    shifr = shifr.replace(']', '')
    shifr = shifr.replace('[', '')
    print(f'b = {shifr}')


def deshifr(a, b, p, x):
    itog = []
    for i in b:
        m = int(i / ((a ** x) % p))
        itog.append(arr[m])
    print(''.join(map(str, itog)))


while True:

    print('1: Шифровка')
    print('2: Расшифровка')
    ok = int(input('Сделайте выбор: '))
    if ok == 1:
        m = input('Введите текст: ')
        generator(m)
    else:
        b = [int(i) for i in input('Введите зашифрованные коды через пробел: ').split()]
        a = int(input('a = '))
        p = int(input('p = '))
        x = int(input('x = '))
        deshifr(a, b, p, x)
