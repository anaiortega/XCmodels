# Arranque en vía 2
    cLC= loadCaseManager.setCurrentLoadCase('ARRV2')
        arranqueVia= 1.21*33e3*ladoElemento/2*30/38
        for n in setNodosVia2.nodes:
            n.newLoad(xc.Vector([-arranqueVia,0,0,0,0,0]))

