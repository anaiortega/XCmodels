# Carga de lazo en vía 2
        nP1= 
        setNodosVia2{ nP1= getTagNearestNode(LTablero/2.0,yVia2CI,zVia2CI) }
        def_set["NodosCargaLazoV2"]
          { sel_nod(nP1) }
    cLC= loadCaseManager.setCurrentLoadCase('LZV2')
        CargaNodosSet("NodosCargaLazoV2",[0,-cargaLazo,0,0,0,0])

