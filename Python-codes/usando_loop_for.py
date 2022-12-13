#Criar um programa que solicite ao usuário o faturamento médio de sua empresa para cada um dos 12 meses do ano.
#Ao final, o programa deve exibir a média anual de faturamento, o maior faturamento e o menor faturamento do ano.
faturamento_total = 0
maior_faturamento = 0
menor_faturamento = 0
for mes in range(1, 13, 1):
    faturamento = float(input(f"Informe o faturamento do mês {mes}: "))
    faturamento_total = faturamento_total + faturamento
    if mes == 1:
        maior_faturamento = faturamento
        menor_faturamento = faturamento
    else:
        if faturamento > maior_faturamento:
            maior_faturamento = faturamento

        if faturamento < menor_faturamento:
            menor_faturamento = faturamento


media_faturamento = faturamento_total / 12
print(f"Você teve um faturamento médio de R${media_faturamento:.2f} por mês")
print(f"O menor faturamento foi de R${menor_faturamento:.2f}")
print(f"O maior faturamento foi de R${maior_faturamento:.2f}")