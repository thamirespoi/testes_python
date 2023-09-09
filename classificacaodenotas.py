## Classificação de notas

print("===============================")
print("==== CLASSIFICAÇÃO DE NOTA ====")
print("===============================")

nota = float(input("Digite sua nota"))

if (nota >= 90 and nota <= 100):
    print("Nota A")
elif (nota >= 80 and nota <= 89):
    print("Nota B")
elif (nota >= 70 and nota <= 79):
    print("Nota C")
elif (nota >= 60 and nota <= 69):
    print("Nota D")
else:
    print("nota F")