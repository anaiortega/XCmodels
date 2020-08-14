# Carga de lazo en vía 1
cargaLazo= 1.21*100e3
\mdlr
    \sets
        nP1= 
        \setNodosVia1
          {
            nP1= getTagNearestNode(LTablero/2.0,yVia1CD,zVia1CD)
          }
        \def_set["NodosCargaLazoV1"]
          { sel_nod(nP1) }
    loads(casos(set_current_load_pattern("LZV1")))
    \sets
        \CargaNodosSet("NodosCargaLazoV1",[0,cargaLazo,0,0,0,0])

