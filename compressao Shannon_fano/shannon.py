class Node:
    def __init__(self, caractere, probabilidade):
        self.caractere = caractere
        self.probabilidade = probabilidade
        self.codigo = ""

def calcular_probabilidades(texto):
    total_caracteres = len(texto)
    probabilidades = {}

    for caractere in texto:
        if caractere in probabilidades:
            probabilidades[caractere] += 1
        else:
            probabilidades[caractere] = 1
    for caractere, contagem in probabilidades.items():
        probabilidades[caractere] = contagem / total_caracteres

    return probabilidades

def criar_simbolos(probabilidades):
    simbolos = [Node(caractere, prob) for caractere, prob in probabilidades.items()]
    return simbolos

def codificacao_fano_shannon(simbolos):
    simbolos.sort(key=lambda x: x.probabilidade, reverse=True)
    fano_shannon(simbolos, 0, len(simbolos) - 1)

def fano_shannon(simbolos, inicio, fim):
    if inicio == fim:
        return

    y = inicio
    z = fim
    soma_esquerda = 0.0
    soma_direita = 0.0

    while y <= z:
        if soma_esquerda <= soma_direita:
            soma_esquerda += simbolos[y].probabilidade
            y += 1
        else:
            soma_direita += simbolos[z].probabilidade
            z -= 1

    for h in range(inicio, y):
        simbolos[h].codigo += "0"
    for h in range(y, fim + 1):
        simbolos[h].codigo += "1"

    fano_shannon(simbolos, inicio, y - 1)
    fano_shannon(simbolos, y, fim)

def gerar_palavra_comprimida(texto, simbolos):
    palavra_comprimida = ""
    for caractere in texto:
        for simbolo in simbolos:
            if simbolo.caractere == caractere:
                palavra_comprimida += simbolo.codigo
                break
    return palavra_comprimida

def descomprimir_palavra(palavra_comprimida, simbolos):
    texto_descomprimido = ""
    codigo_atual = ""

    for bit in palavra_comprimida:
        codigo_atual += bit
        for simbolo in simbolos:
            if simbolo.codigo == codigo_atual:
                texto_descomprimido += simbolo.caractere
                codigo_atual = ""
                break
    return texto_descomprimido

def exibir_resultados(simbolos):
    for simbolo in simbolos:
        print(f"Caractere: {simbolo.caractere}, Probabilidade: {simbolo.probabilidade}, Código: {simbolo.codigo}")

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
        print("Dados lidos do arquivo:", "dados.txt")
        print()
        print("Dados a Ser comprimidos:", dados)
        probabilidades = calcular_probabilidades(dados)
        simbolos = criar_simbolos(probabilidades)
        codificacao_fano_shannon(simbolos)
        exibir_resultados(simbolos)
        print()
        compressao = gerar_palavra_comprimida(dados, simbolos)
        escrever_arquivo("comprimido.txt", compressao)
        print("Compressao: ",compressao)
        descompressao = descomprimir_palavra(compressao, simbolos)
        escrever_arquivo("descomprimido.txt", descompressao)
        print("A descompressao: ", descompressao)
ficheiro()
