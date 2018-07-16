# -*- coding: utf-8 -*-
import os
import glob

#This function is intended to generate a tex file where to include an ordered
#sequence of figures from graphics contained in a directory

def putGrphAsFig(texFile,pathGrph,lstGrPrefix,grWdt):
    '''This function is intended to generate a tex file where to include an 
    ordered sequence of figures from graphics contained in a directory

    :param texFile:     name of the Latex file to be generated
    :param pathGrph:    directory where the graphic files are placed
    :param lstGrPrefix: ordered list with the prefix of the graphic files that 
                        are going to be included
    :param grWdt:       width of the figures 
    '''
    texfl=open(texFile,'w')
    for prf in lstGrPrefix:
        fGrph=glob.glob(pathGrph+prf+'*.jpg')
        fGrph.sort()
        for f in fGrph:
            texfl.write('\\begin{center}\n')
            texfl.write('\includegraphics[width='+grWdt+']{'+f[:-4]+'}\n')
            texfl.write('\end{center}\n')

    texfl.close()
    return

#  Simple load cases results
texFile='./simpleLCresForAnnex.tex'   #name of the Latex file to be generated
pathGrph='./graphics/simplLoadCases/' #directory where the graphic files are
                                      #placed
lstGrPrefix=['GselfWeight','GdeadLoad','GearthPress','QtrafSit1a','QtrafSit1b','QtrafSit2a','QtrafSit2b']
                                      #ordered list with the prefix of the
                                      #graphic files that are going to be
                                      #included
grWdt='120mm'   #width of the graphics for the tex file

putGrphAsFig(texFile,pathGrph,lstGrPrefix,grWdt)


#  ULS normal stresses results
texFile='./normStrsULSForAnnex.tex'   #name of the Latex file to be generated
pathGrph='./graphics/normStrsULS/'     #directory where the graphic files are
                                      #placed
lstGrPrefix=['CF']
                                      #ordered list with the prefix of the
                                      #graphic files that are going to be
                                      #included
grWdt='120mm'   #width of the graphics for the tex file

putGrphAsFig(texFile,pathGrph,lstGrPrefix,grWdt)

#  ULS shear results
texFile='./shearULSForAnnex.tex'   #name of the Latex file to be generated
pathGrph='./graphics/shearULS/'     #directory where the graphic files are
                                      #placed
lstGrPrefix=['CF']
                                      #ordered list with the prefix of the
                                      #graphic files that are going to be
                                      #included
grWdt='120mm'   #width of the graphics for the tex file

putGrphAsFig(texFile,pathGrph,lstGrPrefix,grWdt)

#  SLS cracking (freq) results
texFile='./crackingSLS_freqForAnnex.tex'   #name of the Latex file to be generated
pathGrph='./graphics/crackingSLS_freq/'     #directory where the graphic files are
                                      #placed
lstGrPrefix=['getMaxSteelStress']
                                      #ordered list with the prefix of the
                                      #graphic files that are going to be
                                      #included
grWdt='120mm'   #width of the graphics for the tex file

putGrphAsFig(texFile,pathGrph,lstGrPrefix,grWdt)

#  SLS cracking (qperm) results
texFile='./crackingSLS_qpermForAnnex.tex'   #name of the Latex file to be generated
pathGrph='./graphics/crackingSLS_qperm/'     #directory where the graphic files are
                                      #placed
lstGrPrefix=['getMaxSteelStress']
                                      #ordered list with the prefix of the
                                      #graphic files that are going to be
                                      #included
grWdt='120mm'   #width of the graphics for the tex file

putGrphAsFig(texFile,pathGrph,lstGrPrefix,grWdt)

