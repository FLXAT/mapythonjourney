print('Vamos calcular a área de uma parede')
n1 = float(input('Largura da parede: '))
n2 = float(input('Altura da parede: '))
a = n1*n2
t = a/2
print('A área da sua parede é de {:.2f}m². \nE quantidade de tinta necessária para pintá-la é de {:.1f}l.'.format(a, t))
