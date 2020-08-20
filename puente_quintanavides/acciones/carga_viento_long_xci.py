\mdlr
    loads(casos(set_current_load_pattern("VLONG")))
    \sets
        vientoLongH= FkHTablero/cantoTablero*0.25/coefReductor
        \setElemsVientoLong{\elementos{\for_each{\vector3d_uniform_load_global{[vientoLongH,0,0]}}}}

