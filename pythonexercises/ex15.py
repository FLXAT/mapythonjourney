n1 = float(input('Por quantos dias o alugou? '))
n2 = float(input('Desde que o alugou, quantos km percorreu? '))
c1 = 60*n1
c2 = 0.15*n2
r = c1+c2
print('Este é o valor que tem a pagar pelos dias e kms rodados: R${:.2f}'.format(r))
