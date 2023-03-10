### Biblioteca de Encriptação
A biblioteca de encriptação criada é uma coleção de funções em Python que permitem cifrar e decifrar mensagens utilizando duas técnicas diferentes: a cifra de substituição simples e uma cifra semelhante à máquina Enigma.

Funções Disponíveis
para_one_hot(msg: str) -> np.array
Converte uma string em uma matriz one-hot, onde cada linha representa um caracter do alfabeto e cada coluna representa um caracter da mensagem.

para_string(M: np.array) -> str
Converte uma matriz one-hot em uma string.

cifrar(msg: str, P: np.array) -> str
Aplica uma cifra de substituição simples a uma mensagem, consistindo em substituir cada caracter da mensagem por um caracter de um alfabeto cifrador. Essa substituição é feita trocando o elemento n do alfabeto cifrador pelo elemento n do alfabeto original. Essa operação é feita multiplicando a matriz P (matriz permutação) pelo vetor M, onde P é a matriz one-hot do alfabeto cifrador, e M é a matriz one-hot da mensagem.

de_cifrar(msg: str, P: np.array) -> str
Decifra uma mensagem cifrada com a função cifrar. Ou seja, recupera a mensagem original a partir da mensagem cifrada e da matriz P.

enigma(msg: str, seed: int = 40) -> str
Aplica uma cifra semelhante à cifra da máquina Enigma. Consiste em aplicar uma cifra de substituição simples a cada caracter da mensagem, onde cada caracter da mensagem é substituído por um caracter de um alfabeto cifrador que é cifrado por um alfabeto auxiliar, a cada substituição.

de_enigma(msg: str, seed: int = 40) -> str
Decifra uma mensagem cifrada com a função enigma.

Como usar
As funções desta biblioteca podem ser utilizadas em qualquer programa Python, basta importá-las utilizando o comando import seguido do nome do arquivo em que as funções foram salvas.

Dependências
Esta biblioteca de encriptação depende das seguintes bibliotecas Python:

numpy
random
Certifique-se de que essas bibliotecas estejam instaladas em seu sistema antes de usar a biblioteca de encriptação.