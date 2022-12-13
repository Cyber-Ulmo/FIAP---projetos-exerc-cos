nota_total_aimpar = 0
media_ai = 0
nota_total_apares = 0
media_ap = 0

for alunosi in range(1, 50, 2):
    print("Você está digitando a nota dos alunos ÍMPARES")
    nota_ai = float(input(f"por favor, digite a nota do aluno número {alunosi}: "))
    nota_total_aimpar = nota_total_aimpar + nota_ai

for alunosp in range(2, 51, 2):
    print("Você está digitando a nota dos alunos PARES")
    nota_ap = float(input(f"por favor, digite a nota do aluno número {alunosp}: "))
    nota_total_apares = nota_total_apares + nota_ap

media_ap = nota_total_apares / 25
media_ai = nota_total_aimpar / 25

print("Média Alunos PARES: ", media_ap)
print("Média dos Alunos ÍMPARES: ", media_ai)

if media_ap > media_ai:
    print(f"A média dos alunos PARES é a maior {media_ap}.")

else:
    print(f"média dos alunos ÍMPARES é a maior {media_ai}. ")