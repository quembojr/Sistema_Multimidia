import colorsys
import matplotlib.pyplot as plt #importando matplotlib
import cv2

imagem = plt.imread('beach.jpg')  # Lendo o dado da imagem original
plt.imshow(imagem)  # Exibindo a imagem
plt.show()  # Mostrando a imagem na janela


# 1. Escreva um algoritmo que calcula o histograma de uma imagem.

imagem= cv2.imread('beach.jpg')
histograma = cv2.calcHist([imagem], [0], None, [256], [0,256])
plt.plot(histograma) # Exibindo histograma numa imagem colorida
plt.show()

#Calculando Histograma de uma imagem preto-branco
img_gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY) # Convertendo a imagem em tom de cinza
img_gray = cv2.resize(img_gray, (800, 600))
cv2.imshow("imagem P&B", img_gray) # Exibindo a imagem em tons de cinza
plt.show()
histoPB = cv2.calcHist([img_gray], [0], None, [256], [0,256])
cv2.waitKey()
plt.plot(histoPB) # Exibindo histograma numa imagem Tom de cinza
plt.show()

#Equalizando Histograma de uma imagem preto-branco
histo_eq = cv2.equalizeHist(img_gray)
plt.figure()
plt.title("Histograma equalizado")
plt.xlabel("Intensidade")
plt.ylabel("Qtd de Pixels")
plt.hist(histo_eq.ravel(),256,[0, 256])
plt.xlim([0, 256])
plt.show()


#2 Escreva um algoritmo que faz a conversão das cores RGB para HSV.

def RGB_HSV(RGB):

    R, G, B = RGB
    RGB_Max = max(RGB)
    RGB_Min = min(RGB)

    V = RGB_Max;
    S=0
    if V == 0:
        H = S = 0
        return (H,S,V)
    elif V>0:
        S = (V-RGB_Min)/V
        H=0
        return (H,S,V)


    if S == 0:
        H = 0
        return (H, S, V)

    # Compute the Hue
    if ((RGB_Max) == R and (G>=B)):
        H = 60(G - B)/(RGB_Max - RGB_Min)
    if ((RGB_Max) == R and (G<B)):
        H = 60(G - B)/(RGB_Max - RGB_Min) +360
    elif RGB_Max == G:
        H = 60(B - R)/(RGB_Max - RGB_Min)+120
    else: # RGB_MAX == B
        H = 60(R - G)/(RGB_Max - RGB_Min)+240

    return (H, S, V)

#2 Escreva um algoritmo que faz a conversão das cores RGB para YUV.

def rgb_para_yuv(rgb):
    R, G, B = rgb

    Y = 0.299 * R + 0.587 * G + 0.114 * B
    U = 128 + (-0.14713 * R - 0.288862 * G + 0.436 * B)
    V = 128 + (0.615 * R - 0.51498 * G - 0.10001 * B)

    # Garantindo que V e U esteja no intervalo de 0 a 255
    V = max(0, min(V, 255))
    U = max(0, min(U, 255))

    return (round(Y), round(U), round(V))


RGB = (127, 127, 127)
conversao = RGB_HSV(RGB)
verificar_RGB_HSV = colorsys.rgb_to_hsv(RGB[0], RGB[1], RGB[2])
print()
print("Convertido de RGB para HSV: ",conversao)
print("Verificando a coversao apartir do colorsys : ",verificar_RGB_HSV)
print()

#--------------------------------------------------------------------------

rgb_color = (255, 0, 0)  # RGB vermelho puro
yuv_color = rgb_para_yuv(rgb_color)
print("RGB antes da conversao :", rgb_color)
print("A conversao para YUV:", yuv_color)




