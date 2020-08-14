\mdlr
    \materiales
        hormLosaSup(pesoUnitarioLosaSup= gammaHA*getThickness)
\mdlr
    \loads
        \load_pattern["PCE"] # Prueba de carga estática.
    loads(casos(set_current_load_pattern("PCE")))
    \sets
        \setLosaSup
          {
            \elementos{\for_each{ \vector3d_uniform_load_global{[0.0,0.0,-pesoUnitarioLosaSup]} }}
          }
\CargaNodosLista(tagsNodosRuedasTraseras,[0,0,-10*9810,0,0,0])
\CargaNodosLista(tagsNodosRuedasIntermedias,[0,0,-13*9810,0,0,0])
\CargaNodosLista(tagsNodosRuedasDelanteras,[0,0,-7*9810,0,0,0])
