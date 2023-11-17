def encoder(dados):
    if len(dados) % 2 != 0:
        dados.append(0)

    tamanho = len(dados)
    resultado = [0.0] * tamanho

    while tamanho >= 2:
        for i in range(0, tamanho, 2):
            media = (dados[i] + dados[i + 1]) / 2.0
            diferenca = (dados[i] - dados[i + 1]) / 2.0
            resultado[i // 2] = media
            resultado[i // 2 + tamanho // 2] = diferenca

        for i in range(tamanho):
            dados[i] = resultado[i]
        tamanho //= 2

    return resultado


def decoder(dados):
    tamanho = len(dados)
    resultado = [0.0] * tamanho
    nivel=2
    while nivel <= tamanho:
        for i in range(0, nivel, 2):
            media = (dados[i // 2] + dados[i // 2 + nivel // 2])
            diferenca = (dados[i // 2] - dados[i // 2 + nivel // 2])
            resultado[i] = media
            resultado[i + 1] = diferenca
        for i in range(nivel):
            dados[i] = resultado[i]
        nivel *= 2
    return resultado


dados = [56, 40, 8, 24, 48, 48, 40, 16]
resultado= encoder(dados)
print("O resultado :", resultado)
print("A descompressao :", decoder(resultado))

