# -*- coding: utf-8
\sol_proc{\control
    \solu_model["sm"]
        transformation_constraint_handler()
        rcm_numberer()
    \solu_method["smt","sm"]
        regula_falsi_line_search()
        newton_line_search_soln_algo()
        norm_unbalance_conv_test( tol(0.5) print_flag(1) max_num_iter(20))
        # \load_control_integrator[dLambda1,<Jd,minLambda,maxLambda>]{}
        load_control_integrator()
        band_gen_lin_soe(band_gen_lin_lapack_solver())
  }}

def resuelveCombEstatLin(nmbComb):
    mdlr(dom(nuevo_caso()))
    execfile('desactiva_losa_sup_xci.py')

    mdlr(loads(add_to_domain("G0")))
    \sol_proc{ \static_analysis["smt"]{ analyze(1) analOk= result } }
    mdlr(sets(setLosaSup(alive_elements()))) # Reactivamos los elementos de la losa superior.
    mdlr(dom(mesh(melt_alive_nodes("congelaLosa")))) # Libera nodos inactivos.
    mdlr(loads(add_to_domain(nmbComb)))
    \sol_proc{ \static_analysis["smt"]{ analyze(1) analOk= result } }
    # print("Resuelta combinación: ",nmbComb,"\n")
