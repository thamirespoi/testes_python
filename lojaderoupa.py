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
    if (valorcompra >= 1 and valorcompra <= 499):
        valorfinal = valorcompra - valorcompra * 0.10
    elif (valorcompra >= 500):
        valorfinal = valorcompra - valorcompra * 0.15
    elif (valorcompra >= 1000):
        valorfinal = valorcompra - valorcompra * 0.20
    else:
        print("Digite uma operação válida")

## FORMA DE PAGAMENTO - A PRAZO 
# ATÉ R$799,00

if (formadepagamento == 2):
    if (valorcompra >= 1 and valorcompra < 800): 
        print("A compra pode ser dividida até em 5x sem juros")
        parcelavezes = int(input("Digite o número de vezes que você quer dividir:")) 
        if(parcelavezes > 5 and parcelavezes >= 0):
            print("Valor de parcelamento indisponível.")   

## FORMA DE PAGAMENTO - A PRAZO 
# ACIMA DE R$800,00

    if (valorcompra >= 800):
        print("Com esse valor há mais formas de parcelamento, em até 10x sem juros e até em 18x com juros")
        parcelavezes = int(input("Digite o número de vezes que você quer dividir:"))
        if (parcelavezes >= 1 and parcelavezes <= 10):
            valorfinal = valorcompra
        elif (parcelavezes == 11):
            juros = valorcompra * (parcelavezes*0.05)
        elif (parcelavezes == 12):
            juros = valorcompra * (parcelavezes*0.065)           
        elif (parcelavezes == 13):
            juros = valorcompra * (parcelavezes*0.07)
        elif (parcelavezes == 14):
            juros = valorcompra * (parcelavezes*0.09)
        elif (parcelavezes == 15):
            juros = valorcompra * (parcelavezes*0.095)
        elif (parcelavezes == 16):
            juros = valorcompra * (parcelavezes*0.010)
        elif (parcelavezes == 17):
            juros = valorcompra * (parcelavezes*0.0113)
        elif (parcelavezes == 18):
            juros = valorcompra * (parcelavezes*0.012)      
        else:
            print("Essa quantidade de vezes não esta disponível para parcelamento, escolha uma quantidade disponível.")
else:
    print("Essa forma de pagamento não está disponível, tente novamente escolhendo uma das opções À Vista ou Parcelado")

## PÓS VENDA

if (formadepagamento == 1):
    print(f"O valor total da compra fica {valorcompra} e o valor com desconto {valorfinal}.") 
elif (formadepagamento == 2):
        if(valorcompra >= 1 and valorcompra <= 799):
            if(parcelavezes >=1 and parcelavezes <= 5):
                print(f"O valor total da compra fica {valorcompra} e o valor da parcela fica {valorcompra / parcelavezes} em {parcelavezes} parcelas.") 
        elif(valorcompra >= 800):
            if(parcelavezes >=1 and parcelavezes <= 10):
                print(f"O valor total da compra fica {valorcompra} e o valor da parcela fica {valorcompra + juros / parcelavezes} em {parcelavezes} parcelas e o valor final com juros fica {valorcompra + juros}.")   
            if(parcelavezes >=11 and parcelavezes <= 18):
                print(f"O valor total da compra fica {valorcompra} e o valor da parcela fica {valorcompra + juros / parcelavezes} em {parcelavezes} parcelas e o valor final com juros fica {valorcompra + juros}.") 

print(f"{nome}, obrigada pela compra, volte sempre!")