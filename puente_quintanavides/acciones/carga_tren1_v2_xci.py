# tren de cargas 1 en vía 2
\mdlr
    loads(casos(set_current_load_pattern("TC1V2")))
    \sets
        \sets{\setNodosRVia1TC1{sepMediaNodos= (LTot-x5TC1)*2/getNumNodos}}
        \CargaNodosSet("setNodosRVia2TC1",[0,0,-cargaRCarril*sepMediaNodos,0,0,0])
        \CargaNodosSet("setNodosPVia2TC1",[0,0,-cargaPCarril,0,0,0])
