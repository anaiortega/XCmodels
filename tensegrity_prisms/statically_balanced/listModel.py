
import pandas as pd
def listModelSet(XCset):
    nodes_param=pd.DataFrame(columns=('X','Y','Z'))
    nod_set=XCset.nodes
    for n in nod_set:
        nodes_param.loc[n.tag]=n.getCoo[0],n.getCoo[1],n.getCoo[2]
    print '\n set: ', XCset.name,' Nodes: '
    print nodes_param
    elem_param=pd.DataFrame(columns=('node i','node j'))
    el_set=XCset.elements
    for e in el_set:
        elem_param.loc[e.tag]=str(e.getNodes[0].tag),str(e.getNodes[1].tag)
    print '\n set: ', XCset.name,' Elements: '
    print elem_param
