\mdlr
    \materiales
        hormLosaSup(pesoUnitarioLosaSup= gammaHA*getThickness)
\mdlr
    loads(casos(set_current_load_pattern("PCD")))
    \sets
        \setLosaSup
          {
            \elementos{\for_each{ \vector3d_uniform_load_global{[0.0,0.0,-pesoUnitarioLosaSup]} }}
          }
\CargaNodosLista(tagsNodosRuedas,[0,0,-19500*9.81,0,0,0])
