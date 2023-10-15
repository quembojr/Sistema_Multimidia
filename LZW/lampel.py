
def lzw_encode(texto):
    compressao = []
    dicionario ={}
    dicionario_inicial = {}
    tamanho =0
    s = texto[0]

    for c in texto:
        if not c in dicionario:
            tamanho += 1
            dicionario[c] = tamanho
    dicionario_inicial = dicionario.copy()

    for i in range(1, len(texto)):
        c = texto[i]
        if s + c in dicionario:
            s = s + c
        else:
            compressao.append(dicionario[s])
            tamanho += 1
            dicionario[s + c] = tamanho
            s = c
    compressao.append(dicionario[s])
    print("Dicionário:")
    for key, value in dicionario.items():
        print(key, value)
    return compressao, dicionario_inicial


def lzw_descompressao(compressao, dicionario_inicial):
    resultado = ""
    dicionario={}

    for k, v in dicionario_inicial.items():
        dicionario[v]=(k)

    tamanho = len(dicionario)
    s = dicionario[compressao[0]]
    resultado += s

    for i in range(1, len(compressao)):
        if compressao[i] in dicionario:
            entrada = dicionario[compressao[i]]
        else:
            entrada = s + s[0]

        resultado += entrada
        tamanho += 1
        dicionario[tamanho] = s + entrada[0]
        s = entrada
    return resultado


def ler_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as file:
        dados = file.read()
    return dados

def escrever_arquivo(nome_arquivo, dados):
    with open(nome_arquivo, 'w') as file:
        file.write(dados)

def ficheiro():
    arquivo = "dados.txt"
    dados = ler_arquivo(arquivo)
    if dados is not None:
        print("Dados a serem comprimidos:", dados)
        compressao, dicionario_inicial = lzw_encode(dados)
        with open("comprimido.txt", 'w') as file:
            file.write(','.join(map(str, compressao)))
        print("Compressão:", compressao)
        print("O dicionario inicial: ", dicionario_inicial)
        descompressao = lzw_descompressao(compressao, dicionario_inicial)
        escrever_arquivo("descomprimido.txt", descompressao)
        print("Descompressão:", descompressao)
ficheiro()
