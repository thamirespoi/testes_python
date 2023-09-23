# Laços de Exercícios para laços de repetição

## Exercício 1 - Impressão de números (30min)

for numero in range (1, 11):
    print (numero)

# Sem o int não funciona, porque string não soma com inteiro

maximo = int(input("Qual o numero máximo: "))

for numero in range (1, maximo + 1):
    print (numero)

# Primeira forma de fazer e recomendada

maximo = int(input("Qual o numero máximo: "))
ordem = input("Qual a ordem que deseja imprimir o numeros (C/D): ")

if ordem == 'C':
    for numero in range (1, maximo + 1):
        print (numero)
elif ordem == 'D':
    for numero in range(maximo, 0, -1):
        print(numero)
else:
    print("Ordem Inválida!")


# Segunda forma de fazer

if ordem == 'C':
    numero = 1
    while numero <= maximo:
        print(numero)
        numero +=1
elif ordem == 'D':
    while maximo < 0:
        print(numero)
        numero -=1
else:
    print("Ordem Inválida")


## Exercício 2 - Tabuada

tabuada = float(input("Digite o numero da tabuada: "))

for numero in range (1, 11):
    print(f"{tabuada} x {numero} = {numero*tabuada}") 

## Exercício 3 - Jogo de descobrir

from random import randint

numero = randint(1, 100)
tentativa = int(input("Tente adivinhar o número de 0 a 100: "))
contador = 1


while numero != tentativa:
    if (tentativa >=100 and tentativa <= 0):
        tentativa = int(print("Digite número válido: "))
    elif tentativa > numero:
        tentativa = int(input("O valor é menor, digite um número novamente: "))
        contador = contador + 1
    elif tentativa < numero:
        tentativa = int(input("O valor é maior, digite um número novamente: "))
        contador = contador + 1
    else:
        tentativa = int(input("Digite um número novamente: "))

print ("Parabéns, você acertou!")
print(f"Você fez {contador} tentativas.")


## Exercício 4 - Lista de Médias


