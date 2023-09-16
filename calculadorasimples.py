## Calculadora Simples

print("===============================")
print("===== CALCULADORA SIMPLES =====")
print("===============================")


numero1 = float(input("Digite um numero: "))
numero2 = float(input("Digite um numero: "))
operacao = input("Digite uma das operações a seguir (+ - * /): ")


resultado = ''
if (operacao == '+'):
    resultado = numero1 + numero2
elif (operacao == '-'):
    resultado = numero1 - numero2
elif (operacao == '*'):
    resultado = numero1 * numero2
elif (operacao == '/'):
    if numero2 == 0:
        print("Não é possivel dividir por zero")
    else:
        resultado = numero1 / numero2
else:
    print("Digite uma operação válida")

if resultado != '':
    print(f"O resultado é: {resultado}")

