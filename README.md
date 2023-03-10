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

O código conta com uma aplicação REST simples que permite realizar um POST para os endpoints enigma e de_enigma, com mensagem e seed, em um json, como demonstrado abaixo:

{
    "msg" : "Turing foi incrivel!"
}
ou 
{
    "msg" : "Primeiro computador",
    "seed" : 10
}

Para ativar o servidor, basta entrar no ambiente virtual, realizar o pip install -r requirements.txt e executar o arquivo app.py com o comando python3 app/app.py (pode alterar a depender do diretorio atual e do SO). O servidor estará disponível na porta 5000.

#### Porque funciona?
O processo matématico que explica o funcionamento da cifra de substituição simples é o seguinte: se a mensagem original é M, e a mensagem cifrada é C, então C = P * M, onde P é a matriz permutação. Ou seja, a mensagem cifrada é o resultado da multiplicação da matriz permutação pelo vetor mensagem. Para decifrar, basta aplicar a inversa da matriz permutação, ou seja, P^-1 * C = M. O mesmo processo é feito na função enigma, porém, a cada substituição, o alfabeto cifrador é cifrado por um alfabeto auxiliar, que é gerado a partir de uma semente aleatória. A semente é utilizada para gerar um número aleatório, que é utilizado para gerar um alfabeto auxiliar. O alfabeto auxiliar é gerado a partir de uma lista de caracteres, que é embaralhada a partir da semente. A cada substituição, o alfabeto auxiliar é embaralhado novamente, gerando um novo alfabeto auxiliar. O processo de embaralhamento é feito utilizando o algoritmo Fisher-Yates.
Sendo assim, podemos resumir esse processo como uma série de multiplicações matriciais, em que a cifra simples mantém a matriz permutação constante, enquanto a cifra Enigma altera a matriz permutação, a partir de multiplicações sucessivas de uma matriz auxiliar constante. Valendo MensagemEnigma = E^i * P * M (em que i é o número de iterações e coincide com o tamanho da mensagem), podemos desencriptar a mensagem, utilizando a inversa da matriz permutação, ou seja, M = P^-1 * E^-i * P * M. Como P^-1 * P = I, podemos simplificar a expressão para M = E^i * M. Ou seja, a mensagem encriptada é o resultado da multiplicação da mensagem original pela matriz Enigma elevada ao número de iterações. (OBS: a matriz Enigma é gerada a partir da semente, e é constante para uma mesma semente.)

(Terminar a parte de explicação matemática)

#### Como usar?
Para utilizar a biblioteca, basta importar o arquivo encriptacao.py e utilizar as funções disponíveis. Para utilizar a aplicação REST, basta realizar um POST para o endpoint /enigma ou /de_enigma, com a mensagem e a semente, em um json, como demonstrado acima.

#### Como instalar?
Caso deseje somente utilizar as funções, é possível instalar o pacote utilizando o pip, basta digitar pip install pip install enigma-lib-insper==1.0.0 no terminal com a env ativa. Para mais informações, bastar acessar o repositório no PyPI: https://pypi.org/project/enigma-lib-insper/1.0.0/. 

