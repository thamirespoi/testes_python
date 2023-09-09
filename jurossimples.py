## Calculadora de juros simples:

print("=============================================")
print("======= CALCULADORA DE JUROS SIMPLES ========")
print("=============================================")

nome = input("Olá, qual é seu nome?")
valorprincipal = float(input("Digite o valor inicial:"))
taxadejurosanual = float(input("Digite a taxa anual:"))
tempoanual = float(input("Digite o tempo em anos:"))

taxadejurosanualporcentagem = taxadejurosanual / 100
montante = valorprincipal + (valorprincipal * taxadejurosanualporcentagem * tempoanual)
valordojuros = montante - valorprincipal

print("=============================================")
print(f"Olá {nome},")
print(f"Seu valor principal é {valorprincipal}, sua taxa de juros anual é {taxadejurosanual}% e você irá pagar em {tempoanual} anos")
print(f"O valor total pago é {montante}.")
print(f"E o valor apenas do juros pago é {valordojuros}.")

