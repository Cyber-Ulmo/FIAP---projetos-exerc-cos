palavra_chave = "LIEBRDADE"

numero_em_minutos = int(input("digite os minutos no momento da digitação: "))

resultado = 1
for n in range(1, numero_em_minutos+1):
    resultado *= n
print(f"{palavra_chave}{resultado}")

