print("Bem vindo a calculadora de equação reduzida da reta!")
#Pegando valor de M
print('Digite o valor de m abaixo:')
xa = int(input('Valor de Xa: '))
xb = int(input('Valor de Xb: '))
ya = int(input('Valor de Ya: '))
yb = int(input('Valor de Yb: '))

totalY = yb - ya #-2
totalX = xb - xa #-7
m = totalY / totalX

print(f"O valor do seu M é {m}")

#Pegando o valor de N
print("Agora vamos para o valor de N, para isso você pode escolher o Xa e Ya ou Xb e Yb")
print(f"""Escolha:
1) ({xa} , {ya})
ou
2) ({xb} , {yb})""")
escolhaDoValorPeloUsuario = str(input('Sua escolha: '))

if escolhaDoValorPeloUsuario == '1':
    print(f'Você escolheu o ({xa} , {ya})')
    #Calculando o M e o X
    mx = m * xa
    n = ya - mx
    if n >= 1: 
        print(f'O valor de N é {n}')
        print(f"A equação reduzida da reta é: Y = {m}x + {n}")
    elif n <= -1:
        print(f'O valor de N é {n}')
        print(f"A equação reduzida da reta é: Y = {m}x + ({n})")

elif escolhaDoValorPeloUsuario == '2':
    print(f'Você escolheu o ({xb} , {yb})')
    #Calculando o M e o X
    mx = m * xb
    n = yb - mx
    if n >= 1: 
        print(f'O valor de N é {n}')
        print(f"A equação reduzida da reta é: Y = {m}x + {n}")
    elif n <= -1:
        print(f'O valor de N é {n}')
        print(f"A equação reduzida da reta é: Y = {m}x + ({n})")
