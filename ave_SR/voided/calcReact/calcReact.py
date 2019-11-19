# -*- coding: utf-8 -*-

execfile('../model_gen.py')
execfile('../../generic_bridges/voided_slab_bridge/loadStateData.py')

#ordered list of load cases (from those defined in ../loadStateData.py
#or redefined lately) for which we want to obtain results:


execfile('../../generic_bridges/voided_slab_bridge/calcReactions.py')

f=open("results.py","w")
f.write('React='+repr(results)+'\n')
f.close()

