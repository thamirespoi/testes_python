## ATIVIDADE LOJA DE ROUPAS

print("======================================")
print("======= LOJA DE ROUPAS PYTHON ========")
print("======================================")

print("Seja bem-vindo e boas compras!")

nome = input("Olá, qual é seu nome? ")
valorcompra = float(input("Digite o valor total das suas compras: "))
formadepagamento = int(input("Qual é a forma de pagamento? (Digite 1 se for à vista ou 2 se for parcelado)"))

## FORMA DE PAGAMENTO - A VISTA

if (formadepagamento == 1):
    if (valorcompra >= 1 and valorcompra < 500):
        desconto = 10
    elif (valorcompra >= 500 and valorcompra < 1000):
        desconto = 15
    elif (valorcompra >= 1000):
        desconto = 20
    else:
        print("Digite um valor válido")

## FORMA DE PAGAMENTO - A PRAZO 
# ATÉ R$799,00

elif (formadepagamento == 2):
    if (valorcompra >= 1 and valorcompra < 800): 
        print("A compra pode ser dividida até em 5x sem juros")
        parcelavezes = int(input("Digite o número de vezes que você quer dividir:")) 
        if(parcelavezes > 5 and parcelavezes >= 0):
            print("Valor de parcelamento indisponível.")  
    else:
        print("Digite um valor válido")         

## FORMA DE PAGAMENTO - A PRAZO 
# ACIMA DE R$800,00

    if (valorcompra >= 800):
        print("Com esse valor há mais formas de parcelamento, em até 10x sem juros e até em 18x com juros")
        parcelavezes = int(input("Digite o número de vezes que você quer dividir:"))
        if (parcelavezes == 11):
            digitojuros = 5
        elif (parcelavezes == 12):
            digitojuros = 6.5          
        elif (parcelavezes == 13):
            digitojuros = 7
        elif (parcelavezes == 14):
            digitojuros = 9
        elif (parcelavezes == 15):
            digitojuros = 9.5
        elif (parcelavezes == 16):
            digitojuros = 10
        elif (parcelavezes == 17):
            digitojuros = 11.3
        elif (parcelavezes == 18):
            digitojuros = 12     
        else:
            print("Essa quantidade de vezes não esta disponível para parcelamento, escolha uma quantidade disponível.")
else:
    print("Essa forma de pagamento não está disponível, tente novamente escolhendo uma das opções À Vista ou Parcelado")

## PÓS VENDA

if (formadepagamento == 1):
    print(f"O valor total da compra sem desconto é R${valorcompra} e com desconto de {desconto}% do pagamento a vista fica um total de R${valorcompra - valorcompra * (desconto / 100)}.") 
elif (formadepagamento == 2):
        if(valorcompra >= 1 and valorcompra < 800):
            if(parcelavezes >=1 and parcelavezes <= 5):
                print(f"O valor total da compra é R${valorcompra} e o valor da parcela fica R${valorcompra / parcelavezes} em {parcelavezes} parcelas.") 
        elif(valorcompra >= 800):
            if(parcelavezes >=1 and parcelavezes <= 10):
               print(f"O valor total da compra é R${valorcompra} e o valor da parcela fica R${valorcompra / parcelavezes} em {parcelavezes} parcelas.")   
            if(parcelavezes >=11 and parcelavezes <= 18):
                print(f"O valor total da compra é R${valorcompra}, o valor da parcela fica R${valorcompra + (valorcompra * (parcelavezes*(digitojuros / 100))) / parcelavezes} em {parcelavezes} parcelas e o valor final com juros de {digitojuros}% ao mês fica R${valorcompra + (valorcompra * (parcelavezes*(digitojuros / 100)))}.") 

print(f"Obrigada pela compra {nome}, volte sempre!")