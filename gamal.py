import random
import math

arr = ['&', 'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У',
       'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я', ' ', '1', '2', '3', '4', '5', '6', '7', '8', '9',
       '0']


def generator(text):
    kod = [arr.index(i.title()) for i in text]
    print(kod)

    while True:
        p = random.randint(50, 1000)
        if (math.factorial(p - 1) + 1) % p != 0:  # простота по теореме Вильсона
            pass
        else:
            print(f'p = {p}')
            break

    while True:
        g = random.randint(10, 1000)
        if g < p:
            print(f'g = {g}')
            break

    while True:
        x = random.randint(1, 1000)
        if x < (p - 1):
            print(f'x = {x}')
            break

    y = (g ** x) % p
    print(f'y = {y}')

    def encryption_gamal(kod, p, g, x):
        while True:
            k = random.randint(2, 1000)
            if k < (p - 1):
                print(f'Сессионный ключ = {k}')
                break

        a = (g ** k) % p
        print(f'a = {a}')

        encryption = str([i * (y ** k % p)for i in kod])
        encryption = encryption.replace(
            ',', '').replace(']', '').replace('[', '')
        print(f'Закртытое сообщение: {encryption}')
    encryption_gamal(kod, p, g, x)


def decryption_gamal(text, a, x, p):
    decryption = [arr[int(i / (a ** x % p))] for i in text]
    print(''.join(map(str, decryption)))


while True:
    print("1: Шифровка\n2: Расшифровать")
    choice = int(input("Сделайте выбор: "))
    if choice == 1:
        text = str(input('Введите текст: '))
        generator(text)
    else:
        text = [int(i) for i in input(
            'Введите закртытое сообщение через пробел: ').split()]
        a = int(input('Введите значение a: '))
        x = int(input('Введите значение x: '))
        p = int(input('Введите значение p: '))
        decryption_gamal(text, a, x, p)
