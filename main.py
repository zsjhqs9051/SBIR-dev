#import wx
#import wx.xrc
import os
import sys
import shutil
from Script.Preparation import *
from Script.Support import *
from Script.CFD_executation import *

#CFD Simulation Folder
if os.path.exists('CFD-Model'):
	shutil.rmtree('CFD-Model')
os.mkdir('CFD-Model')

#Geometry Folder
'''
if os.path.exists('Geometry'):
	shutil.rmtree('Geometry')
os.mkdir('Geometry')
'''

#Geometry and CFD Information Folder
'''
if os.path.exists('temp'):
	shutil.rmtree('temp')
os.mkdir('temp')
'''

#Bathymetry Generation, code needed

#CFD Information Input, GUI code needed

#CFD Model Preparation
mother_route = os.getcwd()
CFD_pre = Preparation()
CFD_pre.constantFolder()
CFD_pre.zeroFolder()
NumberCores = CFD_pre.systemFolder()
Log = SimpleLog ()
#CFD Simulation Executation
RecoveryNumber = 5 #max recovery times
os.chdir('CFD-Model')

RecoveryId = 0
Mech_analysis = MeshAnalysis()
MeshLog = SimpleLog ('Mesh-Analysis')

DimensionAdjust = CFD_pre.DimensionAdjustDict()
SHMParemeter = CFD_pre.SHMParemeterDict()

for RecoveryId in range(4):
	goback = 1
	#controlDict
	TimeControl = CFD_pre.timeControlDicts()
	CFD_pre.controlDict(TimeControl)

	#blockMeshDict
	CFD_pre.blockMeshDict(DimensionAdjust)

	RunOpenFOAMTool('paraFoam', Options = '-touch')
	RunOpenFOAMTool('surfaceFeatures' )

	RunOpenFOAMTool('blockMesh' )
	#SHM and Check
	PMCode = 1
	for PMID in range(3) :
		if PMCode > 0:
			DeleteProcessors()
			#SHMDict
			CFD_pre.SHMDict(DimensionAdjust,SHMParemeter)
			RunOpenFOAMTool('decomposePar' )
			RunOpenFOAMTool('snappyHexMesh',Options = '-overwrite',NumberCores = NumberCores,TimeControl = TimeControl )
			B,PMCode1,LayCoverInfo = Mech_analysis.PrismLayerModification(PMID,DimensionAdjust,SHMParemeter)
			SHMParemeter = B
			print(PMCode1)
			PMCode = PMCode1
			for i in range(len(LayCoverInfo)):
				MeshLog.Log(LayCoverInfo[i])
		else:
			break
	if PMID >=2 and PMCode >0:
		continue
	RunOpenFOAMTool('reconstructParMesh',Options = '-constant' )
	RunOpenFOAMTool('checkMesh' )
	DeleteProcessors()
	#Mesh Analysis
	MeshCode,MeshErrorInfo = Mech_analysis.MeshCheckLog()
	for i in range(len(MeshErrorInfo)):
		MeshLog.Log(MeshErrorInfo[i])
	if MeshCode > 0:
		DimensionAdjust = RecoverOpenFoam(RecoveryId,'snappyHexMesh',Log,DimensionAdjust,SHMParemeter)
		continue

	if os.path.exists('system/setFieldsDict'):
		CFDTool = 'interFoam'
		RunOpenFOAMTool('setFields' )
	else:
		CFDTool = 'pimpleFoam'
	#Openfoam single-phase execute
	RunOpenFOAMTool('decomposePar' )
	RetCode = RunOpenFOAMTool(CFDTool,NumberCores = NumberCores,TimeControl = TimeControl)
	if RetCode != 0:
		A = RecoverOpenFoam(RecoveryId,CFDTool,Log,DimensionAdjust)
		DimensionAdjust = A
		continue
	RunOpenFOAMTool('reconstructPar')
	DeleteProcessors()
	break
os.chdir(mother_route)
