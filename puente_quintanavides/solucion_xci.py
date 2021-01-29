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
    modelSpace.removeAllLoadPatternsFromDomain()
    modelSpace.revertToStart()
    modelSpace.deactivateElements(setLosaSup) # Deactivate bridge deck.

    lc0= modelSpace.addLoadCaseToDomain('G0')
    analOk= solProc.solve()

    modelSpace.activateElements(setLosaSup) # Activate bridge deck.
    lc0= modelSpace.addLoadCaseToDomain(nmbComb)
    analOk= solProc.solve()
    # print("Resuelta combinación: ",nmbComb,"\n")
