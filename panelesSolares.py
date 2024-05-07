
def calcularRectangulos(verticesTecho,verticesPanel):
    cantPaneles = 0
    cantvertice1 = int(verticesTecho[0] / verticesPanel[0])
    cantvertice2 = int(verticesTecho[1] / verticesPanel[1])
    nuevoRectangulo = [(verticesTecho[0]-(verticesPanel[0]*cantvertice1)),(verticesTecho[1]-(cantvertice2*verticesPanel[1]))]
    if verticesPanel[0] <= nuevoRectangulo[0]:
        nuevoRectangulo[1]= verticesTecho[1] 
        nuevoRectangulo.sort()
        cantvertice3 = int(nuevoRectangulo[0] / verticesPanel[0])
        cantvertice4 = int(nuevoRectangulo[1] / verticesPanel[1])
        cantPaneles = (cantvertice1 * cantvertice2) + (cantvertice3 * cantvertice4)
    elif verticesPanel[0] <= nuevoRectangulo[1]:
        nuevoRectangulo[0]= verticesTecho[0] 
        nuevoRectangulo.sort()
        cantvertice3 = int(nuevoRectangulo[0] / verticesPanel[0])
        cantvertice4 = int(nuevoRectangulo[1] / verticesPanel[1])
        cantPaneles = (cantvertice1 * cantvertice2) + (cantvertice3 * cantvertice4)
    else:
        cantPaneles = cantvertice1 * cantvertice2
    
    return cantPaneles

def validarRectangulos(baseTecho,alturaTecho,basePanel,AlturaPanel):
    areaTecho = baseTecho * alturaTecho
    areaPanel = basePanel * AlturaPanel
    techoList = [baseTecho,alturaTecho]
    panelList = [basePanel,AlturaPanel]

    techoList.sort()
    panelList.sort()

    if areaTecho >= areaPanel:
        if techoList[1] >= panelList[1] and techoList[0] >= panelList[0]:
            return calcularRectangulos(techoList,panelList)
        else:
            return "El panel solar es mas grande que el techo" 
    else:
        return "El panel solar es mas grande que el techo"

