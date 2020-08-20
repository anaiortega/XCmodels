# tren de cargas 2 en vía 2
\mdlr
    loads(casos(set_current_load_pattern("TC2V2")))
    \sets
        \sets{\setNodosRVia2TC2{sepMediaNodos= (LTot-x5TC2+x0TC2)*2/getNumNodos}}
        \CargaNodosSet("setNodosRVia2TC2",[0,0,-cargaRCarril*sepMediaNodos,0,0,0])
        \CargaNodosSet("setNodosPVia2TC2",[0,0,-cargaPCarril,0,0,0])

