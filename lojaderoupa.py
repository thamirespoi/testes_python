## ATIVIDADE LOJA DE ROUPAS

print("======================================")
print("======= LOJA DE ROUPAS PYTHON ========")
print("======================================")

print("Seja bem-vindo e boas compras!")

nome = input("Olá, qual é seu nome? ")
valortotal = float(input("Digite o valor total das suas compras: "))
formadepagamento = input("Qual é a forma de pagamento? (À Vista ou Parcelado)")

if (formadepagamento == "À Vista"):
    if (valortotal >= 1 and valortotal <= 499):
        print(valortotal - valortotal * 0.1)
    elif (valortotal >= 500):
        print(valortotal - valortotal * 0.15)
    elif (valortotal >= 1000):
        print(valortotal - valortotal * 0.20)