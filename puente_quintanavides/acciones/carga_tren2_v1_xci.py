# tren de cargas 2 en vía 1
\mdlr
    loads(casos(set_current_load_pattern("TC2V1")))
    \sets
        \sets{\setNodosRVia1TC2{sepMediaNodos= (LTot-x5TC2+x0TC2)*2/getNumNodos}}
        \CargaNodosSet("setNodosRVia1TC2",[0,0,-cargaRCarril*sepMediaNodos,0,0,0])
        \CargaNodosSet("setNodosPVia1TC2",[0,0,-cargaPCarril,0,0,0])
