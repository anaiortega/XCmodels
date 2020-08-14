'''Peso propio de la losa superior, se emplea en la
   prueba de carga estática.'''

\mdlr
    \materiales
        hormLosaSup(pesoUnitarioLosaSup= gammaHA*getThickness)
\mdlr
    loads(casos(set_current_load_pattern("G0B")))
    \sets
        \setLosaSup
          {
            \elementos{\for_each{ \vector3d_uniform_load_global{[0.0,0.0,-pesoUnitarioLosaSup]} }}
          }
