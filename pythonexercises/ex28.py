from random import randint
from time import sleep
from emoji import emojize


em = emojize(':disappointed_face:')
print('-=-'*16)
print(f'Tente adivinhar em que número eu vou pensar! {em}')
print('-=-'*16)
n1 = int(input('Digite um número de 0 a 5: '))
n2 = randint(0, 5)
ac = emojize(':thumbs_up:')
er = emojize(':thumbs_down:')
print('ANALISANDO...')
sleep(2.5)

if n1==n2:
    print(f'Parabéns, você acertou! {ac}')

else:
    print(f'Tomastes no cu, tu errou! {er}')  
    
print(f'O numéro é {n2}')
