# Carga de lazo en vía 1
cargaLazo= 1.21*100e3
        nP1= 
        setNodosVia1{
            nP1= getTagNearestNode(LTablero/2.0,yVia1CD,zVia1CD)
          }
        def_set["NodosCargaLazoV1"]
          { sel_nod(nP1) }
    cLC= loadCaseManager.setCurrentLoadCase('LZV1')
        CargaNodosSet("NodosCargaLazoV1",[0,cargaLazo,0,0,0,0])

