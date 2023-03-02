import numpy as np

def para_one_hot(msg: str):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
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
    alphabet = "abcdefghijklmnopqrstuvwxyz"
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
    return C
    

def de_cifrar(C:np.array, P:np.array):
    P_INV = np.linalg.inv(P)
    M_DECIFRADA = np.dot(P_INV, C)
    msg = para_string(M_DECIFRADA)
    return msg

def enigma(msg:str, P:np.array, E:np.array):
    M = para_one_hot(msg)
    C = cifrar(msg, P)
    D = cifrar(C, E)

    return D

def de_enigma(D:np.array, P:np.array, E:np.array):
    P_INV = np.linalg.inv(P)
    E_INV = np.linalg.inv(E)
    C = cifrar(D, E_INV)
    M = cifrar(C, P_INV)
    msg = para_string(M)
    return msg
