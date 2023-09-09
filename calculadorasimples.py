## Calculadora Simples

print("===============================")
print("===== CALCULADORA SIMPLES =====")
print("===============================")


numero1 = float(input("Digite um numero"))
numero2 = float(input("Digite um numero"))
operacao = input("Digite uma das operações a seguir Soma, Subtração, Multiplicação ou Divisão: ")

Calculo1 = numero1 + numero2
Calculo2 = numero1 - numero2
Calculo3 = numero1 * numero2
Calculo4 = numero1 / numero2


if (operacao == 'Soma'):
    print (Calculo1)
elif (operacao == 'Subtração'):
    print (Calculo2)
elif (operacao == 'Multiplicação'):
    print (Calculo3)
elif (operacao == 'Divisão'):
    print (Calculo4)
else:
    print("Digite uma operação válida")