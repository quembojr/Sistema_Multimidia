
def implent_encoder(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    if rows < cols:
        for i in range(cols - rows):
            matrix.append([0] * cols)
        rows = len(matrix)

    elif rows > cols:
        for coluna in matrix:
            coluna.extend([0] * (rows - cols))
        cols = len(matrix[0])

    #Wavelet nas colunas
    for i in range(cols):
        coluna = [matrix[j][i] for j in range(rows)]
        coluna = compressao(coluna)
        for j in range(rows):
            matrix[j][i] = coluna[j]
    #Wavelet nas linhas
    for i in range(rows):
        matrix[i] = compressao(matrix[i])

    return matrix

def compressao(dados):
    tamanho = len(dados)
    resultado = [0] * tamanho

    while tamanho > 2:
        for i in range(0, tamanho, 2):
            media = (dados[i] + dados[i + 1]) / 2.0
            diferenca = (dados[i] - dados[i + 1]) / 2.0
            resultado[i // 2] = media
            resultado[i // 2 + tamanho // 2] = diferenca

        for i in range(tamanho):
            dados[i] = resultado[i]
        tamanho //= 2
    return resultado


def implent_decode(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(rows):
        matrix[i] = descompressao(matrix[i])

    for i in range(cols):
        coluna = [matrix[j][i] for j in range(rows)]
        coluna = descompressao(coluna)
        for j in range(rows):
            matrix[j][i] = coluna[j]

    return matrix

def descompressao(dados):
    tamanho = len(dados)
    resultado = [0] * tamanho

    while tamanho > 2:
        for i in range(0, tamanho, 2):
            media = dados[i // 2]
            diferenca = dados[i // 2 + tamanho // 2]
            resultado[i] = media + diferenca
            resultado[i + 1] = media - diferenca
        for i in range(tamanho):
            dados[i] = resultado[i]
        tamanho //= 2

    return resultado





dados2D = [[63, 127, 127, 63],
           [127, 255, 255, 127],
           [127, 255, 255, 127],
           [63, 127, 127, 63]]

resultado2D = implent_encoder(dados2D)
for linha in resultado2D:
    print(linha)

print()

result = implent_decode(resultado2D)
for linha in resultado2D:
    print(linha)

