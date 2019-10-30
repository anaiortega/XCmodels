# -*- coding: utf-8 -*-
import sys
arg1= str(sys.argv[1])
execfile(arg1)

from postprocess.xcVtk.FE_model import vtk_FE_graphic


defDisplay= vtk_FE_graphic.RecordDefDisplayEF()
defDisplay.cameraParameters= modelSpace.cameraParameters
setToDisplay= trussF.lowerChordSet+trussF.upperChordSet+trussF.postsSet

defDisplay.displayStrongWeakAxis(xcSet= setToDisplay)

