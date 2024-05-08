from sympy import diff,Symbol,solve
from panelesSolares import validarRectangulos

def areaRectangulo(baseTriangulo,alturaTriangulo):
    X = Symbol('X')
    #pendienteDelaRecta
    #y2-y1/x2-x1
    mitadBase = baseTriangulo/2
    m = (0-alturaTriangulo)/(mitadBase-0) 
    y = m*X+alturaTriangulo
    area = X*y
    ecuacion =diff(area,X)
    #X = m -> y = m*X + alturaTriangulo
    #deribada =  m*X**2+ alturaTriangulo*x
    #maximizada = 2*m*X + alturaTriangulo
    # a1 = X = alturaTriangulo/2m
    valorX = solve(ecuacion,X)
    valorY = m*valorX[0] + alturaTriangulo
    aristas = [int(valorX[0]) , int(valorY)]
    aristas.sort()
    aristas[0] = 2*aristas[0]
    return aristas


def rectanguloEntriango(baseTriangulo,alturaTriangulo,BasePanel,alturaPanel):
    aristas = areaRectangulo(baseTriangulo,alturaTriangulo)
    return validarRectangulos(aristas[0],aristas[1],BasePanel,alturaPanel)