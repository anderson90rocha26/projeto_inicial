while True:
    print()
    n1 = input('Digite um número: ')
    n2 = input('Dige o segundo numero: ')
    operador = input('Informe um sinal operacional: ')
    sair = input('Deseja sair? [s], [n]: ')
    if sair == 's':
         break

    if not n1.isnumeric() or not n2.isnumeric():
        print('Você precisa digitar um número!')
        continue

    n1 = int(n1)
    n2 = int(n2)

    if operador == '+':
        print(n1 + n2)
    elif operador == '-':
        print(n1 - n2)
    elif operador == '*':
        print(n1 * n2)
    elif operador == '/':
        print(n1 / n2)
    else:
        print('Operação inválida.')