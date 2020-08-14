# Cargas de la viga

\mdlr
    \materiales
        hormLosaInf(pesoUnitarioLosaInf= gammaHA*getThickness)
        \hormAlmas30{pesoUnitarioAlmas30= gammaHA*getThickness}
        \hormAlmas27{pesoUnitarioAlmas27= gammaHA*getThickness}
        \hormAlmas22{pesoUnitarioAlmas22= gammaHA*getThickness}
        \hormAlmaC50{pesoUnitarioAlmaC50= gammaHA*getThickness}
        \hormAlmaC40{pesoUnitarioAlmaC40= gammaHA*getThickness}
        hormDiafrag(pesoUnitarioDiafrag= gammaHA*getThickness)
\mdlr
    loads(casos(set_current_load_pattern("G0")))
    \sets
        \setLosaInf
          {
            \elementos{\for_each{ \vector3d_uniform_load_global{[0.0,0.0,-pesoUnitarioLosaInf]} }}
          }
        \setAlmasC50
          {
            \elementos{\for_each{ \vector3d_uniform_load_global{[0.0,0.0,-pesoUnitarioAlmaC50]} }}
          }
        \setAlmasC40
          {
            \elementos{\for_each{ \vector3d_uniform_load_global{[0.0,0.0,-pesoUnitarioAlmaC40]} }}
          }
        \setAlmas30
          {
            \elementos{\for_each{ \vector3d_uniform_load_global{[0.0,0.0,-pesoUnitarioAlmas30]} }}
          }
        \setAlmas27
          {
            \elementos{\for_each{ \vector3d_uniform_load_global{[0.0,0.0,-pesoUnitarioAlmas27]} }}
          }
        \setAlmas22
          {
            \elementos{\for_each{ \vector3d_uniform_load_global{[0.0,0.0,-pesoUnitarioAlmas22]} }}
          }
        \setDiafragmas
          {
            \elementos{\for_each{ \vector3d_uniform_load_global{[0.0,0.0,-pesoUnitarioDiafrag]} }}
          }
