def nota_valida(nota):
    if nota >= 0 and nota <= 10:
        return True
    else:
        return False



nota1 = float(input("digite a nota 1: "))
if (nota_valida(nota1)):
    nota2 = float(input("digite a nota 2: "))
    if (nota_valida(nota2)):
        media = nota1 + nota2 / 2
        print(f"A media da nota 01 {nota1} e nota 02 {nota2} é {media}")
    else:
        print(f" a nota 02 {nota2} é inválida")
else:
    print(f"a nota 01 {nota1} é inválida")

