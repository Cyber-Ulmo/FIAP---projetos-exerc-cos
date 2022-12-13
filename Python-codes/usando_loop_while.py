#Crie um programa onde o usuário veja um menu e possa escolher entre as seguintes opções: 1- Elogio, 2 - Frase motivacional ou 3 - Sair
#O menu deve continuar a ser exibido até que o usuário escolha a opção 3.

opcao = 0

while opcao != 3:
    print("MENU FIRMEZA!")
    print("1 - Receber um elogio!")
    print("2 - Frase motivacional :)")
    print("3 - Sair do sistema")
    opcao = int(input("Informe a sua opção: "))
    if opcao == 1:
        print("Você tem uma bela densidade óssea!")
    elif opcao == 2:
        print("Que você destrua com seus dentes todos os sucrilhos!")
    elif opcao == 3:
        print("Saindo do sistema...")
    else:
        print("Opção inválida!")