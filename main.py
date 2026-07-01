print ("Sistema de verificação de idade")

nome = input(" Digite seu nome: ")

idade = int(input(" Digite sua idade: "))

if idade <= 0:
    print ("Idade Inválida.")
else:
    if idade >= 18:
        print (nome, " é maior de idade. ")
    else:
        print (" é menor de idade. ")