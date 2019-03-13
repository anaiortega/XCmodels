from materials.ec3 import EC3Beam as ec3b
from materials.ec3 import EC3_limit_state_checking as EC3lsc

lstLines=gridGeom.getLstLinRange(beamY_rg)
#lstPoints=gridGeom.getLstPntRange(beamY_rg)


supCf_beam=EC3lsc.SupportCoefficients(ky=1.0,kw=1.0,k1=1.0,k2=1.0)
beam01=ec3b.EC3Beam(name='beam01',ec3Shape=beamY_mat,sectionClass=1,supportCoefs=supCf_beam,lstLines=lstLines)
#beam=ec3b.EC3Beam(ec3Shape=None,lstPoints=lstPoints)
beam01.setControlPoints()

beam01.installULSControlRecorder(recorderType="element_prop_recorder")
