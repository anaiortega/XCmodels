    cLC= loadCaseManager.setCurrentLoadCase('NV')
        cargaNieve= 1e3
        for e in setElemsNieve.elements:
            e.vector3dUniformLoadGlobal(xc.Vector([0.0,0.0,-cargaNieve]))

