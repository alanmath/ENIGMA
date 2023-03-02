from fun import *

#Testar a função para_one_hot

mensagem = "hello hi"
M = para_one_hot(mensagem)
# print(M)


#test enigma
# create a P matrix, a E matrix and a message, then encrypt the message, P and E must have only 0 and 1
alfabeto = 'bcdefghijkl mnopqrstuvwxyza'
alfabeto_ao_contrario = "ijkl mnopqrstuvwxyzabcdefgh"
P = para_one_hot(alfabeto)
E = para_one_hot(alfabeto_ao_contrario)


# x = cifrar("hello", P)
# print(x)

# dec = de_cifrar(x, P)
# print(dec)



x = enigma("o bolo de chocolate fica pronto quatro horas da tarde", P,E)
print(x)

y = de_enigma(x, P, E)
print(y)
