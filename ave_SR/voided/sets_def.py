# -*- coding: utf-8 -*-
pilas=pilasBarlov+pilasSotav
pilas.description='Pilas'
pilas.color=cfg.colors['brown03']

pilasInf=gridPil.getSetLinOneXYZRegion(((xPil[0],yPil[0],-hTotPilas),(xPil[-1],yPil[-1],zInfPilas)),'pilasInf')
pilasInf.description='Pilas, zona inferior'
pilasInf.color=cfg.colors['brown04']
pilasSup=gridPil.getSetLinOneXYZRegion(((xPil[0],yPil[0],zInfPilas),(xPil[-1],yPil[-1],zLosInf)),'pilasSup')
pilasSup.description='Pilas, zona superior'
pilasSup.color=cfg.colors['brown01']
if abutment.lower()[0]=='y':
    #zapata
    x=[0,xExtrAletaD]
    y=Yzap
    z=Zzap
    setArmZapEstr=gridAbutment.getSetSurfOneXYZRegion(xyzRange=((x[0],y[0],z[0]),(x[-1],y[-1],z[-1])), nameSet='setArmZapEstr')
    #muro estribo
    x=[0,xAletaD]
    y=Ymurestr
    z=[zZapata,zMurEstr]
    setArmMurEstr=gridAbutment.getSetSurfOneXYZRegion(xyzRange=((x[0],y[0],z[0]),(x[-1],y[-1],z[-1])), nameSet='setArmMurEstr')
    setArmadosEstr=setArmZapEstr+setArmMurEstr
    # No se incluye la aleta izquierda en el set de armados al ser simétrica
    # de la derecha
    # if LaletaIzq>0:
    #     setArmadosEstr+=aletIzqSet
    if LaletaDer>0:
        setArmadosEstr+=aletDerSet
    setArmadosEstr.name='setArmadosEstr'
    setArmadosEstr.description='Estribo'
