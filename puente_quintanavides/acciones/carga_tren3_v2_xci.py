# tren de cargas 3 en vía 2
\mdlr
    loads(casos(set_current_load_pattern("TC3V2")))
    \sets
        \sets{\setNodosRVia2TC3{sepMediaNodos= x0TC3*2/getNumNodos}}
        \CargaNodosSet("setNodosRVia2TC3",[0,0,-cargaRCarril*sepMediaNodos,0,0,0])
        \CargaNodosSet("setNodosPVia2TC3",[0,0,-cargaPCarril,0,0,0])

