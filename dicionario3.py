#Dicionário dentro de dicionário

contatos = {
    "Clark Kent":
        {"Celular":"12345678",
         "Email":"clark@planetadiario.com"},
    "Bruce Wayne":
        {"Celular":"70707070",
         "Email":"bruce@wayneenterprise.com"}
}

# para cada item do dicionário anterior vamos recuperar a chave "forma" e o valor "valor"
celular = ""
email = ""

for contato, valor in contatos.item():
    if "Celular" in contato:
        celular = valor
    elif "Email" in contato:
        email = valor

if email and celular:
    print("O contato {} pode ser encontrado no celular {} e no email {}".format(contato, celular, email))
elif email:
    print("O contato {} pode ser encontrado no email {}".format(contato,email))
elif celular:
    print("O contato {} pode ser encontrado no celular {}".format(contato,celular))