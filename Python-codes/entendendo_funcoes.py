
import teste

def saudacao():
    print("Boa noite")

def elogiar_usuario(nome):
    print(f"{nome}, você é muito firmeza!")

def elogiar_usuario_com_retorno(nome):
    return f"{nome}, você é muito firmeza!"

nomes = ["André", "Weslley", "Dino da Silva Sauro"]
saudacao()
for nome in nomes:
    elogiar_usuario(nome)

print(elogiar_usuario_com_retorno("Batman"))
