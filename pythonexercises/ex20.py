from random import shuffle
n1 = input('Nome do primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem de apresentação do trabalho será')
print(lista)