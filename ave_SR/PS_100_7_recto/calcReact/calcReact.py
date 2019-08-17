# -*- coding: utf-8 -*-

execfile('../model_gen.py')
execfile('../../PSs/loadStateData.py')

#ordered list of load cases (from those defined in ../loadStateData.py
#or redefined lately) for which we want to obtain results:


execfile('../../PSs/calcReactions.py')

f=open("results.py","w")
f.write('React='+repr(results)+'\n')
f.close()

