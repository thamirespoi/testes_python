## Calculadora de juros simples:

print("=============================================")
print("======= CALCULADORA DE JUROS SIMPLES ========")
print("=============================================")

nome = input("Olá, qual é seu nome?")
valorprincipal = float(input("Qual é o valor principal?"))
taxadejurosanual = float(input("Qual a taxa de juros anual?"))
tempoanual = float(input("Qual o período de tempo em anos?"))

taxadejurosanualporcentagem = taxadejurosanual / 100
montante = valorprincipal + (valorprincipal * taxadejurosanualporcentagem * tempoanual)
valordojuros = montante - valorprincipal

print("=============================================")
print(f"Olá {nome},")
print(f"Seu valor principal é {valorprincipal}, e sua taxa de juros anual é {taxadejurosanual}% e você irá pagar em {tempoanual} anos")
print(f"O valor do seu montante final é {montante}.")
print(f"E valor apenas do juros pago é {valordojuros}.")