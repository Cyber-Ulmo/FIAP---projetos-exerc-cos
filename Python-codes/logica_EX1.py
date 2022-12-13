faturamento_anual = 0

for faturamento_mensal in range(1, 13, 1):
    faturamento = float(input(f"Digite o faturamento mensal {faturamento_mensal}: "))
    faturamento_anual = faturamento_anual + faturamento

plano_do_cliente = input("Informe assinatura do cliente: ")
bonus_da_assinatura = 0

if plano_do_cliente == "Basic":
    bonus_da_assinatura = faturamento_anual * 0.30
    print(f"O faturamento anual foi R${faturamento_anual} e o bônus respectivo da assinatura Basic é R${bonus_da_assinatura} ")

elif plano_do_cliente == "Silver":
    bonus_da_assinatura = faturamento_anual * 0.20
    print(f"O faturamento anual foi R${faturamento_anual} e o bônus respectivo da assinatura Silver é R${bonus_da_assinatura} ")

elif plano_do_cliente == "Gold":
    bonus_da_assinatura = faturamento_anual * 0.10
    print(f"O faturamento anual foi R${faturamento_anual} e o bônus respectivo da assinatura Gold é R${bonus_da_assinatura} ")

elif plano_do_cliente == "Platinum":
    bonus_da_assinatura = faturamento_anual * 0.05
    print(f"O faturamento anual foi R${faturamento_anual} e o bônus respectivo da assinatura Platinum é R${bonus_da_assinatura} ")

else: print("Erro na escolha da Assinatura do cliente, por favor recomeçar")