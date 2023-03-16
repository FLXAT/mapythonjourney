n1 = int(input('Digite um número: '))
u = n1 // 1 % 10
d = n1 // 10 % 10
c = n1 // 100 % 10
m = n1 // 1000 % 10
print(f'O número é {n1}')
print(f'A unidade deste número é {u}')
print(f'A dezena é {d}')
print(f'A centena {c}')
print(f'A milhar {m}')
