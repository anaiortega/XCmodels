    materiales
        hormLosaSup(pesoUnitarioLosaSup= gammaHA*getThickness)
    loads
        load_pattern["PCE"] # Prueba de carga estática.
    cLC= loadCaseManager.setCurrentLoadCase('PCE')
        for e in setLosaSup.elements: e.vector3dUniformLoadGlobal(xc.Vector([0.0,0.0,-pesoUnitarioLosaSup]))
          }
CargaNodosLista(tagsNodosRuedasTraseras,[0,0,-10*9810,0,0,0])
CargaNodosLista(tagsNodosRuedasIntermedias,[0,0,-13*9810,0,0,0])
CargaNodosLista(tagsNodosRuedasDelanteras,[0,0,-7*9810,0,0,0])
