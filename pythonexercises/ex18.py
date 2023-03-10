import math
n1 = int(input('Digite um ângulo: '))
sen = math.sin(math.radians(n1))
cos = math.cos(math.radians(n1))
tan = math.tan(math.radians(n1))
print('O seno de {} é: {:.2f}'.format(n1, sen))
print('O coseno de {} é: {:.2f}'.format(n1, cos))
print('A tangente de {} é: {:.2f}'.format(n1, tan))
