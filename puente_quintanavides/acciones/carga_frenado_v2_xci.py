# Frenado en vía 2
    cLC= loadCaseManager.setCurrentLoadCase('FV2')
        frenadoVia= 1.21*20e3*ladoElemento/2
        for n in setNodosVia2.nodes:
            n.newLoad(xc.Vector([frenadoVia,0,0,0,0,0]))

