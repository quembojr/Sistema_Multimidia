

def dpcm(dados):
    preditor = [0]
    resultado = []
    for i in range(0, len(dados)):
        fn = preditor[-1]
        en = dados[i] - fn
        quantizer = round(en)
        resultado.append(quantizer)
        preditor.append(quantizer+fn)
    return resultado

def decoder(dados):
    preditor = [0]
    resultado = []
    for i in range(0, len(dados)):
        fn = preditor[-1]
        en = dados[i] + fn
        resultado.append(en)
        preditor.append(fn + dados[i])
    return resultado

entrada = [3.1,3.2,3.3,3.6,3.7,3.8]
resultado = dpcm(entrada)

print("A sequencia original: ", entrada)
print("O resultado da compresssao : ", resultado)
print("A descompressao e: ", decoder(resultado))


