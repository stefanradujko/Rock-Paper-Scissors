from random import choice


def proveri(o):
    broj = (len(opcije) - 1) / 2
    lista_pob = []
    poz = 0
    for opc in opcije:
        if opc == o:
            brojac = 0
            while brojac != broj:
                poz -= 1
                lista_pob.append(opcije[poz])
                brojac += 1
            return lista_pob
        poz += 1


def uporedi_me():
    o = choice(opcije)
    pobeda = proveri(o)
    if o == z:
        print(f'There is a draw ({o})')
        lista[-1] += 50
    elif z in pobeda:
        print(f'Sorry, but the computer chose <{o}>')
    else:
        print(f'Well done. The computer chose <{o}> and failed')
        lista[-1] += 100


def igraj():
    print("Okay, let's start")
    global z
    while True:
        z = input()
        if z in opcije:
            uporedi_me()
        elif z == '!exit':
            print('Bye')
            break
        elif z == '!rating':
            print(f'Your rating: {lista[-1]}')
        else:
            print('Invalid input')


def prijavi_se():
    ime = input('Enter your name:')
    print(f'Hello, {ime}')
    fajl = open('rating.txt', 'r')
    for line in fajl:
        n, r = line.split()
        if n == ime:
            rejting = int(r)
            return [ime, rejting]
    rejting = 0
    return [ime, rejting]


def definisi_opcije():
    unos = input()
    if unos == '':
        return ['rock', 'paper', 'scissors']
    else:
        return unos.split(',')


lista = prijavi_se()
opcije = definisi_opcije()
igraj()
