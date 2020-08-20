# Arranque en vía 1
\mdlr
    loads(casos(set_current_load_pattern("ARRV1")))
    \sets
        arranqueVia= 1.21*33e3*ladoElemento/2*30/LTot
        \setNodosVia1{\nodos{\for_each
          {
            load([-arranqueVia,0,0,0,0,0])
          }}}

