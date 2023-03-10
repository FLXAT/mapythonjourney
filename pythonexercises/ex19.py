import random
n1 = input('Nome do primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('Uni duni tê, o escolhido(a) foi você, {}'.format(escolhido))
