# Frenado en vía 1
\mdlr
    loads(casos(set_current_load_pattern("FV1")))
    \sets
        frenadoVia= 1.21*20e3*ladoElemento/2
        \setNodosVia1{\nodos{\for_each
          {
            load([frenadoVia,0,0,0,0,0])
          }}}

