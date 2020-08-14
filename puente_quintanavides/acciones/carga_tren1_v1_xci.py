
\mdlr
    loads(casos(set_current_load_pattern("TC1V1")))
    \sets
        \sets{\setNodosRVia1TC1{sepMediaNodos= (LTot-x5TC1)*2/getNumNodos}}
        \CargaNodosSet("setNodosRVia1TC1",[0,0,-cargaRCarril*sepMediaNodos,0,0,0])
        \CargaNodosSet("setNodosPVia1TC1",[0,0,-cargaPCarril,0,0,0])

