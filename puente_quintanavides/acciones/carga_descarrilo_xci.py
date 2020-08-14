
\mdlr
    loads(casos(set_current_load_pattern("AD2")))
    \sets
        sets(setNodosRMureteCI(sepMediaNodos= (20-x5TC1)/getNumNodos))
print("sepMediaNodos= ",sepMediaNodos,"\n")
        \CargaNodosSet("setNodosRMureteCI",[0,0,-2*1.4*cargaRCarril*sepMediaNodos,0,0,0])
        \CargaNodosSet("setNodosPMureteCI",[0,0,-2*1.4*cargaPCarril,0,0,0])

