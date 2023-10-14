class Compressao_Aritmetica:
    def __init__(self, dado):
        self.range_probabilidade = self.calcular_probabilidade(dado)

    def calcular_probabilidade(self, dado):
        frequencia = {}
        for simbol in dado:
            if simbol in frequencia:
                frequencia[simbol] += 1
            else:
                frequencia[simbol] = 1
        range_probabilidade = {}
        low = 0.0
        for simbol, count in frequencia.items():
            high = low + (count / len(dado))
            range_probabilidade[simbol] = (low, high)
            low = high
        return range_probabilidade

    def compressao(self, dado):
        low = 0.0
        high = 1.0
        resultado = 0.0
        for simbol in dado:
            intervalo = high - low
            high = low + intervalo * self.range_probabilidade[simbol][1]
            low = low + intervalo * self.range_probabilidade[simbol][0]
        resultado = (low + high) / 2.0
        return resultado

    def probabilidades(self):
        for simbol, (low, high) in self.range_probabilidade.items():
            print(f"Simbol: {simbol}, Intervalo: [{low}, {high}]")

class Descompressao_Aritmetica:
    def __init__(self, range_probabilidade):
        self.range_probabilidade = range_probabilidade

    def descompressao(self, dado_comprimido, tamanho):
        resul =""
        low = 0.0
        high = 1.0
        intervalo = 1.0
        for i in range(tamanho):
            for simbol, (low, high) in self.range_probabilidade.items():
                if dado_comprimido >= low and dado_comprimido < high:
                    carater= simbol
                    intervalo = high - low
                    break
            resul += carater
            dado_comprimido = (dado_comprimido - low) / intervalo
        return resul

dado = 'ATLA'
codigo = Compressao_Aritmetica(dado)
resultado = codigo.compressao(dado)
codigo.probabilidades()
print("Resultado codificado:", resultado)

desco = Descompressao_Aritmetica(codigo.range_probabilidade)
resultado_descomprimido = desco.descompressao(resultado, len(dado))
print("Resultado descomprimido:", resultado_descomprimido)
