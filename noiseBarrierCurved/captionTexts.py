# -*- coding: utf-8 -*-

#Texts for captions (without punctuation marks)
#prefix 'fatg_' corresponds to fatigue verifications
#prefix 'shear_' correponds to shear verifications
capTexts={
    'FEmesh': 'FE mesh',
    'ULS_normalStressesResistance': 'ULS normal stresses check',
    'ULS_shearResistance': 'ULS shear check',
    'MaxSteelStress': 'steel maximum stress',
    'SLS_frequentLoadsCrackControl': 'SLS cracking, frequent actions',
    'SLS_quasiPermanentLoadsLoadsCrackControl': 'SLS cracking, quasi-permanent actions',
}

shear_capText={
    'CF': 'capacity factor (efficiency)',
    'N': 'normal force associated with the capacity factor',
    'My':'bending moment about the local Y axis associated with the capacity factor',
    'Mz':'bending moment about the local Z-axis associated with the capacity factor',
    'Mu':'ultimate bending moment',
    'Vy':'shear force in the local Y-axis direction associated with the capacity factor',
    'Vz':'shear force in the local Z-axis direction associated with the capacity factor',
    'theta':'',
    'Vcu': 'contribution of the concrete to the shear capacity in the ULS',
    'Vsu': 'contribution of the steel to the shear capacity in the ULS',
    'Vu': 'ultimate shear force',
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
    'getMaxSteelStress': "contrainte maximale dans l'armature",
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
