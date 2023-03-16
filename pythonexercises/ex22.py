n1 =  str(input('Digite seu nome completo: ')).strip(' ')
sp = n1.split()
print(f'Seu nome completo em maiúsculo {n1.upper()}')
print(f'Em minúsculo {n1.lower()}')
print(f'Quantidade de letras {len(n1) - n1.count(" ")}')
print(f'Quantidade de letras do seu primeiro nome {len(sp[0])}')
    