
execfile('../datos_cordon_pret_xci.py')

\mdlr
    \materiales
        \elastic_membrane_plate_section["hormLosaInf"]{ nu(nu) E(Ec50) h(0.25) rho(rhoHA) }
        \elastic_membrane_plate_section["hormAlmas30"]{ nu(nu) E(Ec50) h(0.30) rho(rhoHA) }
        \elastic_membrane_plate_section["hormAlmas27"]{ nu(nu) E(Ec50) h(0.27) rho(rhoHA) }
        \elastic_membrane_plate_section["hormAlmas22"]{ nu(nu) E(Ec50) h(0.22) rho(rhoHA) }
        \elastic_membrane_plate_section["hormAlmaC50"]{ nu(nu) E(Ec50) h(0.50) rho(rhoHA) }
        \elastic_membrane_plate_section["hormAlmaC40"]{ nu(nu) E(Ec50) h(0.40) rho(rhoHA) }
        \elastic_membrane_plate_section["hormDiafrag"]{ nu(nu) E(Ec50) h(1.0) rho(rhoHA) }
        \elastic_membrane_plate_section["hormLosaSup"]{ nu(nu) E(Ec30) h(0.30) rho(rhoHA) }

        # Cables pretensado
        \cable_material["cordon"]{E(ECordon) prestress(sigmaFinalTesadoCordon) unitWeightEff(densAcero) }
