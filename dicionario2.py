#criando um dicionário vazio

dicionario = {}

#incluindo dados no dicionario
dicionario["Felipe Alves"] = "Desenvolvedor"

#pedindo para o usuário incluir dados no dicionário

novaChave = input("Informa o nome do colaborador: ")
novoValor = input("Informa a função do colaborador: ")
dicionario[novaChave] = novoValor

#exibindo o dicionário completo
for chave, valor in dicionario.items():
    print("O colaborador {} desempenha a função de {}".format(chave, valor))