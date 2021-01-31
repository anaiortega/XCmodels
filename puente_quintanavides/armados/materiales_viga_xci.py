nmbHorm= "HP50"
exec(open('ehe/hormigonesEHE_xcm.py').read()))
exec(open('ehe/acerosEHE_xcm.py').read()))

# Coeficientes de seguridad de los materiales.
gammac= 1.5 # Coeficiente de minoración de la resistencia del hormigón.
gammas= 1.15 # Coeficiente de minoración de la resistencia del acero.

\setupHormigon("HP50",gammac)
\setupAcero("B500S",gammas)
tagHA= 0.0
tagB500S= 0.0

\mdlr
\materiales
    tagHA= defDiagDHormigon("HP50")
    \dgDHP50
        Ec= getTangent

    tagB500S= defDiagDAcero("B500S")
    \dgDB500S
        Es= getTangent
  }}
