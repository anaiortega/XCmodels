    cLC= loadCaseManager.setCurrentLoadCase('VLONG')
        vientoLongH= FkHTablero/cantoTablero*0.25/coefReductor
        for e in setElemsVientoLong.elements:
            e.vector3dUniformLoadGlobal(xc.Vector([vientoLongH,0,0]))

