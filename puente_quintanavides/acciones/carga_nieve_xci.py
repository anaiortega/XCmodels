\mdlr
    loads(casos(set_current_load_pattern("NV")))
    \sets
        cargaNieve= 1e3
        \setElemsNieve{\elementos{\for_each{\vector3d_uniform_load_global{[0.0,0.0,-cargaNieve]}}}}

