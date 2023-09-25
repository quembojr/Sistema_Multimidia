# Definicao da classe Node para representar os nos da arvore de Huffman.
class Node:
    def __init__(self, probabilidade, simbolo, esquerda=None, direita=None):
        self.probabilidade = probabilidade
        self.simbolo = simbolo
        self.esquerda = esquerda
        self.direita = direita
        self.codigo = ''

# Dicionario para armazenar os codigos Huffman de cada simbolo.
codigos = {}

# Funcao para calcular os codigos Huffman para os nos da arvore.
def calcular_codigos(no, valor=''):
    novo_valor = valor + str(no.codigo)
    if no.esquerda:
        calcular_codigos(no.esquerda, novo_valor)
    if no.direita:
        calcular_codigos(no.direita, novo_valor)
    if not no.esquerda and not no.direita:
        # armazena o codigo no dicionário usando o simbolo como chave.
        codigos[no.simbolo] = novo_valor
    return codigos

# Funcao para calcular a probabilidade de ocorrencia de cada simbolo nos dados de entrada.
def calcular_frequencia(dados):
    simbolos = {}
    for elemento in dados:
        if simbolos.get(elemento) is None:
            simbolos[elemento] = 1
        else:
            simbolos[elemento] += 1
    return simbolos

# Funcao para gerar a saida codificada usando os codigos Huffman.
def saida(dados, codigo):
    saida = ""
    for c in dados:
        saida += codigo[c]
    return saida

# Funcao principal para realizar a compressao de Huffman.
def compressao_huffman(dados):
    simbolo_probabilidade = calcular_frequencia(dados)
    simbolos = simbolo_probabilidade.keys()
    # Gerar uma lista de contagem de simbolos e suas frequencias.
    contagem_simbolos = [f"{simbolo}: {probabilidade}" for simbolo, probabilidade in simbolo_probabilidade.items()]
    probabilidade = ", ".join(contagem_simbolos)
    print("Ocorrencias: ", probabilidade)

    # Inicializar uma lista de nos (inicialmente, um no para cada símbolo).
    nos = []
    for simbolo in simbolos:
        nos.append(Node(simbolo_probabilidade.get(simbolo), simbolo))

    # Construir a arvore de Huffman combinando os nos ate restar apenas um no raiz.
    while len(nos) > 1:
        nos = sorted(nos, key=lambda x: x.probabilidade)
        direita = nos[0]
        esquerda = nos[1]

        # Atribuir códigos 0 e 1 para os nos filhos.
        esquerda.codigo = 0
        direita.codigo = 1

        # Criar um novo no combinando os dois nos filhos.
        novo_no = Node(esquerda.probabilidade + direita.probabilidade, esquerda.simbolo + direita.simbolo, esquerda, direita)
        nos.remove(esquerda)
        nos.remove(direita)
        nos.append(novo_no)

    # Calcular os codigos Huffman para os simbolos a partir do no raiz.
    codigos_huffman = calcular_codigos(nos[0])
    print("Simbolos com codigos: ", codigos_huffman)

    saida_codificada = saida(dados, codigos_huffman)

    return saida_codificada, nos[0]

# Funcao para realizar a descompressao dos dados codificados.
def descompressao(dados_codificados, arvore_huffman):
    no_raiz = arvore_huffman
    resultado = ""
    no_atual = arvore_huffman

    for i in dados_codificados:
        if i == '1':
            no_atual = no_atual.direita
        elif i == '0':
            no_atual = no_atual.esquerda

        if no_atual.esquerda is None and no_atual.direita is None:
            resultado += str(no_atual.simbolo)
            no_atual = no_raiz
    return resultado



def ler_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as file:
            dados = file.read()
        return dados
    except FileNotFoundError:
        print(f"O arquivo '{nome_arquivo}' não foi encontrado.")
        return None

def escrever_arquivo(nome_arquivo, dados):
    with open(nome_arquivo, 'w') as file:
        file.write(dados)

def ficheiro():
    arquivo="dados.txt"
    dados = ler_arquivo(arquivo)
    if dados is not None:
        print("Dados lidos do arquivo:",  arquivo)
        print("Dados a Ser comprimido: ", dados)

        compressao, arvore = compressao_huffman(dados)
        escrever_arquivo("comprimido", compressao)
        print("A compressao: ", compressao)
        # Descomprimir os dados
        resultado = descompressao(compressao, arvore)

        # Escrever os dados descomprimidos em um arquivo
        escrever_arquivo("descomprimido", resultado)
ficheiro()
