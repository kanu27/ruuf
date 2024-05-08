
def calcularRectangulos(aristasTecho,aristasPanel):
    cantPaneles = 0
    cantarista1 = int(aristasTecho[0] / aristasPanel[0])
    cantarista2 = int(aristasTecho[1] / aristasPanel[1])
    nuevoRectangulo = [(aristasTecho[0]-(aristasPanel[0]*cantarista1)),(aristasTecho[1]-(cantarista2*aristasPanel[1]))]
    if aristasPanel[0] <= nuevoRectangulo[0]:
        nuevoRectangulo[1]= aristasTecho[1] 
        nuevoRectangulo.sort()
        cantarista3 = int(nuevoRectangulo[0] / aristasPanel[0])
        cantarista4 = int(nuevoRectangulo[1] / aristasPanel[1])
        cantPaneles = (cantarista1 * cantarista2) + (cantarista3 * cantarista4)
    elif aristasPanel[0] <= nuevoRectangulo[1]:
        nuevoRectangulo[0]= aristasTecho[0] 
        nuevoRectangulo.sort()
        cantarista3 = int(nuevoRectangulo[0] / aristasPanel[0])
        cantarista4 = int(nuevoRectangulo[1] / aristasPanel[1])
        cantPaneles = (cantarista1 * cantarista2) + (cantarista3 * cantarista4)
    else:
        cantPaneles = cantarista1 * cantarista2
    
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

