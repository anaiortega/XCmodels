# Definición del procedimiento de solución.
\sol_proc{\control
    \solu_model["sm"]
        \transformation_constraint_handler
        \rcm_numberer
    \solu_method["smt","sm"]
        \regula_falsi_line_search
        \newton_line_search_soln_algo
        norm_unbalance_conv_test( tol(0.5) print_flag(1) max_num_iter(20))
        # \load_control_integrator[dLambda1,<Jd,minLambda,maxLambda>]
        \load_control_integrator
        band_gen_lin_soe(\band_gen_lin_lapack_solver)
  }}




def resuelveCombEstatLin(nmbComb):
    mdlr(dom(\nuevo_caso()))

    database(restore(tagSaveFase0))
    \mdlr{\loads{\combinaciones
        \nmbComb
          {
            exec(open('solution/database_helper_solve_xci.py').read()))
            \add_to_domain()
            \sol_proc{ \static_analysis["smt"]{ analyze(1) analOk= result } }
            exec(open('solution/database_helper_save_xci.py').read()))
            \remove_from_domain()
          }
      }}}
    # print("Resuelta combinación: ",nmbComb,"\n")
