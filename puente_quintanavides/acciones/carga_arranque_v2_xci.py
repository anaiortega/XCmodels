# Arranque en vía 2
\mdlr
    loads(casos(set_current_load_pattern("ARRV2")))
    \sets
        arranqueVia= 1.21*33e3*ladoElemento/2*30/38
        \setNodosVia2{\nodos{\for_each
          {
            load([-arranqueVia,0,0,0,0,0])
          }}}

