## Cálculo de Bônus Salarial

print("===============================")
print("======= BÔNUS SALARIAL ========")
print("===============================")

salario = float(input("Digite seu salario:"))
tempodeservico = float(input("Digite seu tempo de serviço em anos:"))

if (tempodeservico >= 5):
    salariobonus = salario + salario * 0.05
    print(salariobonus)
else:
    print("Sem bônus disponível")