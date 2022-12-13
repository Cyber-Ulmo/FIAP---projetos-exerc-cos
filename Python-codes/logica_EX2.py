status_da_votacao = "sim"
votos = []

while status_da_votacao != "não":
    seu_voto = input("escolha o dia da semana(no padrão: segunda, terça, quarta, quinta ou sexta): ")
    votos.append(seu_voto)
    status_da_votacao = input("há mais eleitores e votos válidos? sim ou não : ")

print(f"O total de votos é de {len(votos)}")
print("o total de votos na Segunda-feira é:", votos.count("segunda"))
print("o total de votos na Terça-feira é:", votos.count("terça"))
print("o total de votos na Quarta-feira é:", votos.count("quarta"))
print("o total de votos na Quinta-feira é:", votos.count("quinta"))
print("o total de votos na Sexta-feira é:", votos.count("sexta"))
print("Todos os votos, válidos e inválidos são: ", votos)
