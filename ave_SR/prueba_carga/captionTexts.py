# -*- coding: utf-8 -*-

#Texts for captions (without punctuation marks)
#prefix 'fatg_' corresponds to fatigue verifications
capTexts={
    'FEmesh': 'FE mesh',
    'ULS_normalStressesResistance': 'ULS normal stresses check',
    'ULS_shearResistance': 'ULS shear check',
    'getMaxSteelStress': 'steel maximum stress',
    'SLS_frequentLoadsCrackControl': 'SLS cracking, frequent actions',
    'SLS_quasiPermanentLoadsLoadsCrackControl': 'SLS cracking, quasi-permanent actions',
}

#captions for reults of simple load cases (English version)
enCapTextsSimplLC={
    'uX':'displacement in global X direction',
    'uY':'displacement in global Y direction',
    'uZ':'displacement in global Z direction',
    'rotX':"rotation around global X axis",
    'rotY':"rotation around global Y axis",
    'rotZ':"rotation around global Z axis",
    'N1':'internal axial force in local direction 1',
    'N2':'internal axial force in local direction 2',
    'M1':'bending moment around local axis 1',
    'M2':'bending moment around local axis 2',
    'Q1':'internal shear force in local direction 1',
    'Q2':'internal shear force in local direction 2',
    'N':'internal axial force',
    'Qy':'internal shear force in local direction y',
    'Qz':'internal shear force in local direction z',
    'My':'bending moment around local axis y',
    'Mz':'bending moment around local axis z',
    'T':'internal torsional moment'
}

capTexts={
    'uX':'déplacement en direction X',
    'uY':'déplacement en direction Y',
    'uZ':'déplacement en direction Z',
    'rotX':"rotation autour de l'axe X",
    'rotY':"rotation autour de l'axe Y",
    'rotZ':"rotation autour de l'axe Z",
    'CF':'facteur de capacité',
    'getCF':'facteur de capacité',
    'N':'effort normal associé au facteur de capacité',
    'N1':'effort normal direction 1',
    'N2':'effort normal direction 2',
    'M1':'moment de flexion direction 1',
    'M2':'moment de flexion adirection 2',
    'Q1':'effort tranchant direction 1',
    'Q2':'effort tranchant direction 2',
    'Qy':'effort tranchant direction y',
    'Qz':'effort tranchant direction z',
    'My':'moment de flexion associé au facteur de capacité',
    'Mz':'moment de flexion associé au facteur de capacité',
    'Mu':'valeur ultime du moment de flexion',
    'theta':'',
    'Vy':'effort tranchant associé au facteur de capacité',
    'Vz':'effort tranchant associé au facteur de capacité',
    'Vcu':'',
    'Vsu':'',
    'Vu':"valeur ultime de l'effort tranchant",
    'LocalAxes': 'axes locaux',
    'FEmesh': 'maillage',
    'ULS_normalStressesResistance': 'Vérification ELU contraintes normales',
    'normalStressCheck': 'Vérification ELU contraintes normales',
    'ULS_shearResistance': 'Vérification ELU effort tranchant',
    'getMaxSteelStress': "contrainte maximale dans l'armature",
    'SLS_frequentLoadsCrackControl': 'Vérification ELS fissuration, cas de charge fréquents',
    'SLS_quasiPermanentLoadsLoadsCrackControl': 'Vérification ELS fissuration, cas de charge quasi-permanents',
    
}

fatg_capTexts={
    'ULS_fatigueResistance': 'Vérification ELU fatigue',
    'getAbsSteelStressIncrement': "vérification de l'armature. Différence de contrainte $\delta_{sd}(Q_{fat})$ sous les actions de fatigue",
    'concreteBendingCF':'vérification du béton. Facteur de capacité contraintes de compression',
    'concreteLimitStress':'vérification du béton. Limites contraintes de compression',
    'concreteShearCF':'vérification du béton. Facteur de capacité effort tranchant',
    'shearLimit': 'vérification du béton. Limites effort tranchant',
    'Mu': 'moment de flexion ultime',
    'Vu': 'effort tranchant ltime',

}

#Español
capTexts={
    'uX':'desplazamiento en dirección X',
    'uY':'desplazamiento en dirección Y',
    'uZ':'desplazamiento en dirección Z',
    'rotX':"rotación en torno al eje X",
    'rotY':"rotación en torno al eje Y",
    'rotZ':"rotación en torno al eje Z",
    'CF':'factor de capacidad',
    'getCF':'factor de capacidad',
    'N':'esfuerzo normal asociado al factor de capacidad',
    'N1':'esfuerzo normal dirección 1',
    'N2':'esfuerzo normal dirección 2',
    'M1':'momento flector dirección 1',
    'M2':'momento flector dirección 2',
    'Q1':'esfuerzo cortante dirección 1',
    'Q2':'esfuerzo cortante dirección 2',
    'Qy':'esfuerzo cortante dirección y',
    'Qz':'esfuerzo cortante dirección z',
    'My':'momento flector asociado al factor de capacidad',
    'Mz':'momento flector asociado al factor de capacidad',
    'Mu':'valor último del momento flector',
    'theta':'',
    'Vy':'esfuerzo cortante asociado al factor de capacidad',
    'Vz':'esfuerzo cortante asociado al factor de capacidad',
    'Vcu':'',
    'Vsu':'',
    'Vu':"valor último del esfuerzo cortante",
    'LocalAxes': 'ejes locales',
    'FEmesh': 'malla de elementos',
    'ULS_normalStressesResistance': 'Comprobación ELU tensiones normales',
    'normalStressCheck': 'Comprobación ELU tensiones normales',
    'ULS_shearResistance': 'Comprobación ELU esfuerzo cortante',
    'getMaxSteelStress': "tensión máxima en la armadura",
    'SLS_frequentLoadsCrackControl': 'Comprobación ELS fisuración, casos de carga frecuentes',
    'SLS_quasiPermanentLoadsLoadsCrackControl': 'Comprobación ELS fisuración, casos de carga quasi-permanentes',
    
}
