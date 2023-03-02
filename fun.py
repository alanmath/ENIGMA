import numpy as np
import random

alphabet = "abcdefghijklmnopqrstuvwxyz "

def para_one_hot(msg: str):
    char_to_index = {}

    for i, char in enumerate(alphabet):
        char_to_index[char] = i

    num_chars = len(alphabet)
    num_timesteps = len(msg)
    one_hot = np.zeros((num_chars, num_timesteps))
    for i, char in enumerate(msg):
        if char in char_to_index:
            one_hot[char_to_index[char], i] = 1
    return one_hot


def para_string(M: np.array):
    msg = ""
    for i in range(M.shape[1]):   # iterar através das colunas (caracteres) da matriz
        indices = np.where(M[:,i] == 1)[0]  # encontra os índices dos elementos igual a 1 na coluna atual
        if indices.size > 0:  # se houver um índice válido, adiciona a letra correspondente à mensagem
            msg += alphabet[indices[0]]
        else:  # se não houver um índice válido, adiciona um espaço em branco à mensagem
            msg += " "
    return msg


def cifrar(msg:str, P:np.array):
    M = para_one_hot(msg)
    C = np.dot(P, M)

    return para_string(C)
    

def de_cifrar(msg: str, P:np.array):
    P_INV = np.linalg.inv(P)
    C = para_one_hot(msg)
    M_DECIFRADA = np.dot(P_INV, C)
    msg = para_string(M_DECIFRADA)
    return msg

def enigma(msg:str, seed:int = 40):
    random.seed(seed)
    alfabeto_cifrador = list(alphabet)
    random.shuffle(list(alfabeto_cifrador))
    alfabeto_cifrador = "".join(alfabeto_cifrador)

    cifrador_aux = list(alfabeto_cifrador)
    random.shuffle(cifrador_aux)
    cifrador_aux = "".join(cifrador_aux)
    
    M = para_one_hot(msg)
    P = para_one_hot(alfabeto_cifrador)
    E = para_one_hot(cifrador_aux)

    matriz_zerada = np.zeros((len(alphabet),len(msg)))
    for i in range(len(msg)):
        matriz_zerada[:,i] = (np.linalg.matrix_power(E,i))@P@M[:,i]

    return para_string(matriz_zerada)



def de_enigma(msg:str, seed:int = 40):
    random.seed(seed)
    alfabeto_cifrador = list(alphabet)
    random.shuffle(list(alfabeto_cifrador))
    alfabeto_cifrador = "".join(alfabeto_cifrador)

    cifrador_aux = list(alfabeto_cifrador)
    random.shuffle(cifrador_aux)
    cifrador_aux = "".join(cifrador_aux)

    M = para_one_hot(msg)
    P = para_one_hot(alfabeto_cifrador)
    E = para_one_hot(cifrador_aux)

    matriz_zerada = np.zeros((len(alphabet),len(msg)))
    for i in range(len(msg)):
        matriz_zerada[:,i] = np.linalg.inv(P)@(np.linalg.matrix_power(E,-i))@M[:,i]

    return para_string(matriz_zerada)
