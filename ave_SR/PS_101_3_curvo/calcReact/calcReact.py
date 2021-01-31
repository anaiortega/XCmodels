# -*- coding: utf-8 -*-

exec(open('../model_data.py').read()))
exec(open('../../PSs/loadStateData.py').read()))

#ordered list of load cases (from those defined in ../loadStateData.py
#or redefined lately) for which we want to obtain results:


exec(open('../../PSs/calcReactions.py').read()))

f=open("results.py","w")
f.write('React='+repr(results)+'\n')
f.close()

