    cLC= loadCaseManager.setCurrentLoadCase('VTRSV')
        vientoTrsvH= FkHTablero/cantoTablero*2 # Se aplica en los elementos de la mitad superior para simular el momento.
        for e in setElemsVientoTrsvH.elements:
            e.vector3dUniformLoadGlobal(xc.Vector([0,vientoTrsvH,0]))
        vientoTrsvV= FkVTablero/BTablero*2# Se aplica en los elementos de la mitad derecha para simular el momento.
        for e in setElemsVientoTrsvV.elements:
            e.vector3dUniformLoadGlobal(xc.Vector([0,0,vientoTrsvV]))

