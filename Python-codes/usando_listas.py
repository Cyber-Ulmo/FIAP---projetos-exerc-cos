#Fazer um programa que permita ao usuário digitar o nome de cada um dos convidados que chegou em uma festa infantil.
#Ao final, o programa deve exibir a quantidade de convidados que compareceram, a lista de convidados na ordem de chegada e a lista de convidados por ordem alfabética

resposta = "sim"
convidados = []
while resposta.upper() != "NÃO":
    nome_convidado = input("Informe o nome do convidado: ")
    convidados.append(nome_convidado)
    resposta = input("Deseja inserir mais um convidado? SIM ou NÃO? ")

print(f"Na festa vieram {len(convidados)}")
print("Convidados em ordem de chegada:")
for convidado in convidados:
    print(convidado)
convidados.sort()
print("Convidados em ordem alfabética:")
for convidado in convidados:
    print(convidado)

