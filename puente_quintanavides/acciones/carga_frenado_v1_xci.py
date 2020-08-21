# Frenado en vía 1
    cLC= loadCaseManager.setCurrentLoadCase('FV1')
        frenadoVia= 1.21*20e3*ladoElemento/2
        for n in setNodosVia1.nodes:
            n.newLoad(xc.Vector([frenadoVia,0,0,0,0,0]))

