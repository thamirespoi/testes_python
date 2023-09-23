alunos = []
notas = []
solicita_notas = True

while solicita_notas:
    aluno = input("Digite o nome do aluno: ")
    alunos.append(aluno)

    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))
    nota4 = float(input("Digite a quarta nota: "))

    notas_aluno = (nota1, nota2, nota3, nota4)
    notas.append(notas_aluno)

    continua = input("Deseja continuar? (S/N) ")
    if continua == "N": solicita_notas = False

for aluno in alunos:
    print(f"Aluno: {aluno}")
    notas_aluno = notas[alunos.index(aluno)]
    quantidade_notas = len(notas_aluno)
    
    for nota in notas_aluno:
        print(f"Nota: {nota}") 

    media = (nota1+nota2+nota3+nota4) / quantidade_notas
    
    print(f"Média: %.2f" % media)

