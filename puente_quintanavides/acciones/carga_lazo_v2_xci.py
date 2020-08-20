# Carga de lazo en vía 2
\mdlr
    \sets
        nP1= 
        \setNodosVia2
          { nP1= getTagNearestNode(LTablero/2.0,yVia2CI,zVia2CI) }
        \def_set["NodosCargaLazoV2"]
          { sel_nod(nP1) }
    loads(casos(set_current_load_pattern("LZV2")))
    \sets
        \CargaNodosSet("NodosCargaLazoV2",[0,-cargaLazo,0,0,0,0])

