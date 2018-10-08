#!/usr/bin/env python
import os

from MEDLoader import MEDLoader
import MEDMeshDescription


from jsonpickle._samples import Thing
import jsonpickle
def saveMeshForXC(mesh,fName):
  # with open(fName + '.pkl', 'wb') as f:
  #   pickle.dump(mesh, f, pickle.HIGHEST_PROTOCOL)
  with open(fName + '.pkl', 'wb') as f:
    json_obj= jsonpickle.encode(mesh)
    f.write(json_obj)

