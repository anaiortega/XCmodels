# tren de cargas 3 en vía 2
    cLC= loadCaseManager.setCurrentLoadCase('TC3V2')
        sets{setNodosRVia2TC3{sepMediaNodos= x0TC3*2/getNumNodos}}
        CargaNodosSet("setNodosRVia2TC3",[0,0,-cargaRCarril*sepMediaNodos,0,0,0])
        CargaNodosSet("setNodosPVia2TC3",[0,0,-cargaPCarril,0,0,0])

