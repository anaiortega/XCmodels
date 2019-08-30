# -*- coding: utf-8 -*-
abutment='Y' #if abutment is modelled 'Y'
pile_found='Y'

def redondea(lista,decimales):
    retval=[]
    for i in lista:
        retval.append(round(i,decimales))
    return retval
