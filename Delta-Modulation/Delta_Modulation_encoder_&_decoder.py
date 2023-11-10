def encoder(data):
    preditor = [0]
    result= []
    for i in range(0, len(data)):
        en = data[1] - preditor[-1]
        if en > 0:
            quantizer = 1
        else:
            quantizer = 0
        preditor.append(preditor[-1] + quantizer)
        result.append(quantizer)
    return result

def decoder(data):
    preditor = [0]
    result = []
    for i in range(0, len(data)):
        fn = preditor[-1]
        en = data[i] + fn
        result.append(en)
        preditor.append(fn + data[i])
    return result

data = [3.1,3.2,3.3,3.6,3.7,3.8,1.5]
result = encoder(data)
print("compressao: ", result)
print("Descompressao : ", decoder(result))