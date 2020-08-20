\mdlr
    \materiales
        hormLosaSup(pesoUnitarioLosaSup= gammaHA*getThickness)
\mdlr
    loads(casos(set_current_load_pattern("G1")))
    \sets
        \setLosaSup
          {
            \elementos{\for_each{ \vector3d_uniform_load_global{[0.0,0.0,-pesoUnitarioLosaSup-cargaUnitariaLosaSup]} }}
          }
