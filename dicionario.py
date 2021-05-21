dicionario = {"Yoda":"Mestre Jedi", "Mace Windu":"Mestre Jedi", "Anakin Skywalker":"Cavaleiro Jedi", "R2-D2":"Dróide", "Dex":"Balconista"}

#Se colocar o dado da chave ele vai printar o valor
print(dicionario["R2-D2"])


#exibir os valores em loop
for valor in dicionario.values():
    print(valor)

print("################################")


#exibir as chaves em loop
for chave in dicionario.keys():
    print(chave)

print("################################")
print("################################")

#remover o item cuja a chave é Mace Windu
#o método pop exclui um item específico
dicionario.pop("Mace Windu")

#o metodo popitem exclui o último item inserido
#dicionario.popitem()

#o método clear exclui todos os itens do dicionário
#dicionario.clear()

#exibir tanto as chaves quanto os valores
for chave, valor in dicionario.items():
    print("O personagem {} é da categoria {}".format(chave, valor))