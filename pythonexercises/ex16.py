from math import sqrt, trunc
import random
n1 = random.randint(1, 100)
cal = sqrt(n1)
print('A raiz quadrada de {} é {} juntamente com sua porção inteira.'.format(n1, trunc(cal)))
