# -*- coding: utf-8

VtkCargaMallaCad("uGridCad","setTramo6","superficies")
\vtk
    \define["vtkRenderer","renderer"]{set_background(.95, .95, .95)}
    VtkDefineActorKPoint("uGridCad","renderer",0.02)
    VtkDefineActorCells("uGridCad","renderer","surface")

    renderer(\reset_camera())


'''
VtkDibujaIdsKPts("uGridCad","total","renderer") # Dibuja etiquetas de los puntos.
VtkDibujaIdsCells("uGridCad","total","lineas","renderer") #Dibuja etiquetas de las líneas.
VtkDibujaIdsCells("uGridCad","total","superficies","renderer") # Dibuja etiquetas de las superficies.
'''
