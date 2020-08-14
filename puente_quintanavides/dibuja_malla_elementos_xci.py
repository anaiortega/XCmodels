# -*- coding: utf-8
nmbSet= "total"

VtkCargaMallaElem("uGridElem",nmbSet)

\vtk
    \define["vtkRenderer","renderer"]
        set_background(.95, .95, .95)
    VtkDefineActorNodo("uGridElem","renderer",0.02)
    VtkDefineActorElementos("uGridElem","renderer","surface")


    \renderer
      { \reset_camera() }
'''
VtkDibujaIdsNodos("uGridElem",nmbSet,"renderer") # Dibuja etiquetas de los nodos.
VtkDibujaIdsElementos("uGridElem","renderer") # Dibuja etiquetas de los elementos.
'''
