\mdlr
    loads(casos(set_current_load_pattern("VTRSV")))
    \sets
        vientoTrsvH= FkHTablero/cantoTablero*2 # Se aplica en los elementos de la mitad superior para simular el momento.
        \setElemsVientoTrsvH{\elementos{\for_each{\vector3d_uniform_load_global{[0,vientoTrsvH,0]}}}}
        vientoTrsvV= FkVTablero/BTablero*2# Se aplica en los elementos de la mitad derecha para simular el momento.
        \setElemsVientoTrsvV{\elementos{\for_each{\vector3d_uniform_load_global{[0,0,vientoTrsvV]}}}}

