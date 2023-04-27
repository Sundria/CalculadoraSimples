print(f'{"Calculadora":=^42}')


def lin():
    print('===' * 14)


def calculo(a, b, c):
    print('O resultado do produto é: ', end='')
    if c == "+":
        soma = a + b
        print(f'{soma:.2f}')
    elif c == "-":
        sub = a - b
        print(f'{sub:.2f}')
    elif c == "/":
        div = a / b
        print(f'{div:.2f}')
    elif c == "*":
        mult = a * b
        print(f'{mult:.2f}')
    lin()


#programa principal
while True:
    a = float(input('Digite o primeiro valor: '))
    b = float(input('Digite o segundo valor: '))
    lin()
    print('''Escolha entre Somar: +
Subtrair: -
Dividir: /
Multiplicar: *''')
    lin()
    while True:
        c = input('O que deseja fazer: ')
        if c not in "+-/*":
            print('Opção inválida, tente de novo.')
        if c in "+-/*":
            break
    calculo(a, b, c)
    while True:
        opção = str(input('Quer continuar as operações?[S/N] ')).upper()[0]
        if opção in "SN":
            break
    lin()
    if opção == "N":
        break