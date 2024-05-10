import os

mensagens = []
nome = input("Nome: ")

while True:
    #Limpa terminal
    os.system('cls')

    if len(mensagens) > 0:
        for m in mensagens:
            print(m['nome'], "-", m['texto'])

    print("_________________")

    #obtendo texto
    texto = input("Mensagem: ")
    if texto == "fim":
        break

    #adicionando msg na lista
    mensagens.append({
        "nome": nome,
        "texto": texto
    })