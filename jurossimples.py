## Calculadora de juros simples:

print("=============================================")
print("======= CALCULADORA DE JUROS SIMPLES ========")
print("=============================================")

valorprincipal = float(input("Qual é o valor principal?"))
taxadejurosanual = float(input("Qual a taxa de juros anual?"))
tempoanual = int(input("Qual o período de tempo em anos?"))

montante = valorprincipal + (valorprincipal + taxadejurosanual + tempoanual)

print("=============================================")
print(f"O valor do montante final é {montante}.")