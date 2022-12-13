numero_tabuada = int(input("Informe o número do qual deseja a tabuada: "))

for contador in range(1, 11, 1):
    resultado = numero_tabuada * contador
    print(f"{numero_tabuada} x {contador} = {resultado}")
