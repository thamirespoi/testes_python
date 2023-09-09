# Arquivo de IMC

nome = input("Qual é seu nome?")
idade = int(input("Qual é sua idade?"))
peso = float(input("Qual é seu peso?"))
altura = float(input("Qual é sua altura?"))

resultado1 = altura * altura
imc = peso / resultado1

print("Olá", nome)
print("Sua idade é de", idade, "anos.")
print("Seu IMC é de", imc)