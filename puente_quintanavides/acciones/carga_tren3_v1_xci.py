# tren de cargas 3 en vía 1
\mdlr
    loads(casos(set_current_load_pattern("TC3V1")))
    \sets
        \sets{\setNodosRVia1TC3{sepMediaNodos= x0TC3*2/getNumNodos}}
        \CargaNodosSet("setNodosRVia1TC3",[0,0,-cargaRCarril*sepMediaNodos,0,0,0])
        \CargaNodosSet("setNodosPVia1TC3",[0,0,-cargaPCarril,0,0,0])

