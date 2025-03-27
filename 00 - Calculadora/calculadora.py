print('---' * 5, 'CALCULADORA', '---' * 5)
print()


def opcao():
    opcao = int(input('''Qual opção deseja?

    [1] - Soma
    [2] - Subtração
    [3] - Múltiplicação
    [4] - Divisão
    [5] - Tabuada
    [6] - Sair

    '''))

    if opcao == 1:
        soma()
    elif opcao == 2:
        subtracao()
    elif opcao == 3:
        multiplicacao()
    elif opcao == 4:
        divisao()
    elif opcao == 5:
        tabuada()
    else:
      print()
      print('Desconectando....')


def continuar():
    continuar = input('Deseja realizar outra operação? [S/N] ').strip().lower()
    print()
    if continuar in ['s', 'sim']:
      opcao()
    else:
      print('Encerrando...')


def escolha_numeros():
    print()
    global numero1, numero2
    numero1 = int(input('Digite um número: '))
    numero2 = int(input('Digite outro número: '))


def escolhe_numero_tabuada():
    print()
    global numero1
    numero1 = int(input('Deseja a tabuada de qual número? '))


def soma():
    escolha_numeros()
    soma = numero1 + numero2
    print()
    print(f'{numero1} + {numero2} = {soma}')
    print()
    continuar()


def subtracao():
    escolha_numeros()
    subtracao = numero1 - numero2
    print()
    print(f'{numero1} - {numero2} = {subtracao}')
    print()
    continuar()


def multiplicacao():
    escolha_numeros()
    multiplicacao = numero1 * numero2
    print()
    print(f'{numero1} x {numero2} = {multiplicacao}')
    print()
    continuar()


def divisao():
    escolha_numeros()
    divisao = numero1 / numero2
    print()
    print(f'{numero1} / {numero2} = {divisao}')
    print()
    continuar()


def tabuada():
    escolhe_numero_tabuada()
    print()
    for n in range(0, 11):
      print(f'{numero1} x {n}: {numero1*n}')
    print()
    continuar()



opcao()