#Listas em Python

import sys

nome = "Felipe Alves"
idade = 24
peso = 90.5

# o getsizeof verifica o tamanho da memória ram do computador de qualquer objeto

print("A variável nome é do tipo {} e tem {} bytes".format(type(nome), sys.getsizeof(nome)))
print("A variável idade é do tipo {} e tem {} bytes".format(type(idade), sys.getsizeof(idade)))
print("A variável peso é do tipo {} e tem {} bytes".format(type(peso), sys.getsizeof(peso)))

# tupla são parecidos com as listas mas todos os dados armazenados permanecera2o sempre nas mesmas posições
# enquanto listas sa2o criadas com [] as tuplas são criadas com ()

filmes = ("Avengers", "Avatar", "Toy Story", "Interestelar", "Bad Boys")

for filme in filmes:
    print(filmes)
print(filmes[1])
print(filmes[3])




listaVazia = []
tuplaVazia = ()

print("O objeto listaVazia é do tipo {} e ocupa {} bytes de memória".format(type(listaVazia), sys.getsizeof(listaVazia)))
print("O objeto tuplaVazia é do tipo {} e ocupa {} bytes de memória".format(type(tuplaVazia), sys.getsizeof(tuplaVazia)))