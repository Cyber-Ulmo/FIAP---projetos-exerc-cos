numero_tabuada = int(input("Informe o número do qual deseja a tabuada "))

contadora = 1

while contadora <= 10:
    resultado = numero_tabuada * contadora
    print(f"{numero_tabuada} x {contadora} = {resultado}")
    contadora = contadora + 1
