print('Você é o rapaz responsável por precificar os produtos, no entanto,\n' 
      'você colocou o preço errado e um clinte o comprou por outro preço.\n' 
      'Ele fez uma reclamação por causa alteração do preço do produto.\n' 
      'Então seu patrão mandou dar um desconto de 5% sobre o preço original.\nQuanto será que vai ficar o valor?\n')

n1 = float(input('Você que o precificou, por quanto estava o valor do produto? R$'))
c = n1*0.95

print('Bem, depois de tudo, vamos dar o desconto. Este é o valor que o cliente vai pagar {:.2f}R$'
      .format(c))
