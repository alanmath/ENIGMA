from criptografia import *

"""
    Programa para demonstrar a utilização da biblioteca enigma
    A biblioteca permite a encriptação e decriptação de mensagens,
    utilizando o algoritmo de encriptação das máquinas enigma e uma seed
    para gerar a chave de encriptação.
    Sendo assim, para encriptar uma mensagem, basta utilizar a função enigma e
    passar a mensagem e a seed como parâmetros (caso a seed não seja passada o valor seed=40 é adotado). Para decriptar, o processo é o mesmo,
    com o detalhe de que é necessario passsar a mesma seed que foi utilizada para encriptar, a fim de recuperar 
    a mensagem original.
"""
## teste da funcao enigma
crip_enig = enigma("O bolo, de chocolate, fica pronto às 16:05. (Esteja em casa ou vai ficar sem!)", 20)
print("Mensagem encriptada com o enigma: " + crip_enig)

## teste da funcao de_enigma
decrip_enigma = de_enigma(crip_enig, 20)
print("Mensagem decriptada com a funcao de_enigma: "+decrip_enigma)

## teste da funcao para one hot
msg = "O bolo, de chocolate, fica pronto às 16:05. (Esteja em casa ou vai ficar sem!)"
print("Mensagem original: " + msg)
print("Mensagem em one hot: ")
one_hot_msg = para_one_hot(msg)
print(one_hot_msg)

## teste da funcao para string
str_vindo_de_one_hot = para_string(one_hot_msg)
print("Mensagem vinda de one hot: " + str_vindo_de_one_hot)

## As funcoes cifrar e decifrar necessitam de uma matriz P, que é a matriz de permutação
## criada dinamicamente a depender da seed, logo, para testar essas funções, é necessário
## criar uma matriz P a partir da seed utilizada na encriptação.
seed  = 20
alphabet = "abcdefghijklmnopqrstuvwxyz0123456789.,;:!?()[]{}-+*/=<>@#$%&'\"áàéíóúâêûôãõ "
random.seed(seed)
alfabeto_cifrador = list(alphabet)
random.shuffle(list(alfabeto_cifrador))
alfabeto_cifrador = "".join(alfabeto_cifrador)
P = para_one_hot(alfabeto_cifrador)
cifrar_msg = cifrar(msg, P)

## teste da funcao cifrar
print(cifrar_msg)

## teste da funcao decifrar
print(de_cifrar(cifrar_msg, P))