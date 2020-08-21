# tren de cargas 3 en vía 1
    cLC= loadCaseManager.setCurrentLoadCase('TC3V1')
        sets{setNodosRVia1TC3{sepMediaNodos= x0TC3*2/getNumNodos}}
        CargaNodosSet("setNodosRVia1TC3",[0,0,-cargaRCarril*sepMediaNodos,0,0,0])
        CargaNodosSet("setNodosPVia1TC3",[0,0,-cargaPCarril,0,0,0])

