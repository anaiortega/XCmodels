

\mdlr{\constraints
    # PL
    \fix[tagNodoApoyoDorsalDerecho,2] { valor(0.0) }

    # PU
    \fix[tagNodoApoyoDorsalIzquierdo,1] { valor(0.0) }
    \fix[tagNodoApoyoDorsalIzquierdo,2] { valor(0.0) }

    # PF
    \fix[tagNodoApoyoFrontalDerecho,0] { valor(0.0) }
    \fix[tagNodoApoyoFrontalDerecho,1] { valor(0.0) }
    \fix[tagNodoApoyoFrontalDerecho,2] { valor(0.0) }

    # PU
    \fix[tagNodoApoyoFrontalIzquierdo,0] { valor(0.0) }
    \fix[tagNodoApoyoFrontalIzquierdo,2] { valor(0.0) }
  }}

tagsNodosCoartados= tagNodoApoyoDorsalDerecho,tagNodoApoyoDorsalIzquierdo,tagNodoApoyoFrontalDerecho,tagNodoApoyoFrontalIzquierdo
