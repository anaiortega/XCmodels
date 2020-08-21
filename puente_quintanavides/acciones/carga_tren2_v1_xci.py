# tren de cargas 2 en vía 1
    cLC= loadCaseManager.setCurrentLoadCase('TC2V1')
        sets{setNodosRVia1TC2{sepMediaNodos= (LTot-x5TC2+x0TC2)*2/getNumNodos}}
        CargaNodosSet("setNodosRVia1TC2",[0,0,-cargaRCarril*sepMediaNodos,0,0,0])
        CargaNodosSet("setNodosPVia1TC2",[0,0,-cargaPCarril,0,0,0])
