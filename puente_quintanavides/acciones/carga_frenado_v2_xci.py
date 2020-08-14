# Frenado en vía 2
\mdlr
    loads(casos(set_current_load_pattern("FV2")))
    \sets
        frenadoVia= 1.21*20e3*ladoElemento/2
        \setNodosVia2{\nodos{\for_each
          {
            load([frenadoVia,0,0,0,0,0])
          }}}

