# Arquivo de IMC

print("===============================")
print("===== CALCULADORA DO IMC ======")
print("===============================")

nome = input("Qual é seu nome?")
idade = int(input("Qual é sua idade?"))
peso = float(input("Qual é seu peso?"))
altura = float(input("Qual é sua altura?"))

imc = peso / (altura * altura)

print("===============================")

print(f"Olá {nome};")
print(f"Sua idade é de {idade} anos.")
print(f"Seu IMC é de {imc};")