import os
import sys
import shutil
from Script.Preparation import *
from Script.Support import *



DimensionAdjust = {"Base_Size":0.01,"Xmax":2.5,\
				   "Xmin":-2.5,"Ymax":2.5,"Ymin":0,"WSE":0.028,\
				   "Zmax":0.028,"Zmin":-0.01}
SHMParemeter = {'First_Cell':0.005,\
				'BedLayerN':3,'BridgeLayerN':2,\
				'BedSurface':0.01,'BedSurface':0.01,\
				'BedRegion':0.01,'BridgeRegion':0.01,}
LayCoverInfo = []

mother_route = os.getcwd()
os.chdir('CFD-Model')
Log = SimpleLog ()
Mech_analysis = MeshAnalysis()

#PMID = 2
#SHMParemeter,PMCode,LayCoverInfo = Mech_analysis.PrismLayerModification(PMID,DimensionAdjust,SHMParemeter)

#MeshCode,MeshErrorInfo = Mech_analysis.MeshCheckLog()

#for i in range(len(LayCoverInfo)):
	#print(LayCoverInfo[i])
#print(SHMParemeter)
#for i in range(len(MeshErrorInfo)):
#	print(MeshErrorInfo[i])
for i in range(4):
	for j in range(5):
		if j>2:
			break
		else:
			print(i,j)
