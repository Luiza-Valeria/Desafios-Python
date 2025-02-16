print("\n******************* Calculadora em Python *******************")

print('Selecione o número da operação desejada: ')

print('''
         [ 1 ] Adiçao
         [ 2 ] Subtração
         [ 3 ] Multiplicação
         [ 4 ] Divisão

''')

opcao = int(input( 'Digite sua opção: (1/2/3/4): '))

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

def soma_numeros(n1,n2):
    resultado = n1 + n2
    print('{} + {} = {}'.format(n1,n2,resultado))
def multiplicacao(n1,n2):
    resultado = n1 * n2
    print('{} * {} = {}'.format(n1,n2,resultado))
def subtrair_numeros(n1,n2):
    resultado = n1 - n2
    print('{} - {} = {}'.format(n1, n2, resultado))

def divisao(n1,n2):
    resultado = n1 / n2
    print('{} / {} = {}'.format(n1, n2, resultado))

if opcao == 1:
    print(soma_numeros(n1,n2))
elif opcao == 2:
    print(subtrair_numeros(n1,n2))
elif opcao == 3:
    print(multiplicacao(n1,n2))
elif opcao == 4:
    print(divisao(n1,n2))
else:
    print('Opção Inválida. Por Favor, escolha uma opção entre 1 e 4')



