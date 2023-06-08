#Importando o script de raiz quadrada
from math import sqrt

print("Bem vindo a Calculadora de Equação de Segundo Grau!")

print("Primeiro vou pegar os valores")

#pegando os valores

valorDeA = int(input("Digite o valor de a: "))
valorDeB = int(input("Digite o valor de b: "))
valorDeC = int(input("Digite o valor de c: "))

#Calculando o valor do Delta

delta = ((valorDeB ** 2)) - (4 * valorDeA * valorDeC)

#Condições if
if delta > 0:
    bhaskaraX1 = float(((-valorDeB + sqrt(delta))) / (2 * valorDeA))
    bhaskaraX2 = float(((-valorDeB - sqrt(delta))) / (2 * valorDeA))
    print(f"A equação de segundo grau é: \033[32mX1 ={bhaskaraX1} e X2 = {bhaskaraX2}\033[m")
elif delta == 0:
    bhaskara = float(((-valorDeB + delta)) / (2 * valorDeA))
    print(f"A equação de segundo grau é: \033[32mX1 {bhaskara} e X2 {bhaskara}\033[m")

else:
    print(f"\033[33mO valor do delta é\033[m \033[31m{delta}\033[m \033[33mnegativo, sendo assim a equação é sem solução real.\033[m")

