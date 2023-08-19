from matplotlib import pyplot
class objeto:
    def __init__(self, velocidadeX, velocidadeY, x, y):
        self.velocidadeY = velocidadeY
        self.velocidadeX = velocidadeX
        self.x = x
        self.y = y

#posição do plot
objeto.x = 0
objeto.y = 0
objeto.velocidadeX = 0.3
objeto.velocidadeY = -1
#tamanho dos eixos
Xnegativo = -50
Xpositivo = 55
Ynegativo = -50
Ypositivo = 50

def mostrarPosicao():
    pyplot.axis([Xnegativo,Xpositivo,Ynegativo,Ypositivo])
    pyplot.plot(objeto.x, objeto.y, 'bo')
    pyplot.draw()
    pyplot.pause(0.00001)
    pyplot.clf()

pyplot.ion()
while True:
    mostrarPosicao()
    objeto.y += objeto.velocidadeY
    objeto.x += objeto.velocidadeX
    if objeto.y <= Ynegativo or objeto.y >= Ypositivo:
        objeto.velocidadeY *= -1
    if objeto.x <= Xnegativo or objeto.x >= Xpositivo:
        objeto.velocidadeX *= -1