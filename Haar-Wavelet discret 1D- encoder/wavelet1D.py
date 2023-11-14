def WAVELET(dados):
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

dados = [56, 40, 8, 24, 48, 48, 40, 16]
resultado= WAVELET(dados)
print("O resultado :", resultado)

