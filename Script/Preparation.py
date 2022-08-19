import pandas as pd
import numpy as np
import shutil
import os
import sys
from Script.Support import *

tolerance = 1e-6

class Preparation():
	#load the input geometry dimension and CFD information
	'''######<<<<<<   CFDdata   >>>>>>######
	CFD Model: 1 - single phase; 2 - VOF, 1 is the default value
	WSE: water surface elevation;
	d50: d50 of sand
	Q: flow rate; Ux: approach velocity. Only one of these two items is allowed to be input
	Base_Size: base size of mesh
	First_Cell: cell size of the first prism layer
	BedLayerN, BridgeLayerN: Prism layer number on riverbed and bridge
	BedSurface, BridgeSurface: Cell size on the surface of riverbed and bridge
	BedRegion,BridgeRegion: Cell size in the region around the riverbed and bridge
	Ratio: ratio of cell sizes between different prism layers, default value is 1.5
	dt: max allowable time step
	physicalTime: physical time
	Processor_Number: number of processors to parallel conduct the simulation
	'''
	'''######<<<<<<   GEOdata   >>>>>>######
	Xmin, Xmax
	Ymin, Ymax
	Zmin
	'''
	def __init__(self):
		#CFD and Geometry Info
		self.CFDdata = {}
		self.GEOdata = {}
		with open('temp/CFD_Info.txt') as f:
			for line in f.readlines():
				self.CFDdata.update({line.split('\t')[0]:float(line.split('\t')[1])})
		with open('temp/Geo_Info.txt') as f:
			for line in f.readlines():
				self.GEOdata.update({line.split('\t')[0]:float(line.split('\t')[1])})

	#CFD Template Source, CFD simulation model: single-phase or VOF
	def __srcroute(self):
		CFDModelTemplateRoute = ''
		#single phase
		if abs(self.CFDdata['CFDMode'] - 1.0 ) <= tolerance :
			CFDModelTemplateRoute = 'Configure/SF_Model/'

		#VOF
		if abs(self.CFDdata['CFDMode'] - 2.0 ) <= tolerance :
			CFDModelTemplateRoute = 'Configure/VOF_Model/'
		return CFDModelTemplateRoute

	#estimated initial k epsilon nut Q and Ux
	def __initialValue(self):
		Viscosity = 8.90883E-07
		C_nu = 0.09
		Width = self.GEOdata['Ymax'] - self.GEOdata['Ymin']
		Depth = self.CFDdata['WSE'] - self.GEOdata['Zmin']
		Area = 0.5 * Width * Depth
		flowrate = self.CFDdata['Q']
		#velocity
		if self.CFDdata['Q'] > 0 :
			U = self.CFDdata['Q'] / Area
		else:
			U = self.CFDdata['Ux']
		Pw = Depth
		Rh = Area/Pw
		Dh = 4 * Rh
		Re = U * Dh / Viscosity
		I = 0.16 * Re ** (-1/8)
		k = 1.5 * (I*U)**2
		l = 0.07 * Dh
		epsilon = (C_nu ** 0.75) * (k**1.5) / l
		nut = C_nu * k **2 / epsilon
		return flowrate,U,k,epsilon,nut

	#prepare constant folder for openfoam model
	def constantFolder(self):
		CFDModelTemplateRoute = self.__srcroute()
		constant_scr = CFDModelTemplateRoute + 'constant'
		constant_dst = 'CFD-Model/constant'
		shutil.copytree(constant_scr,constant_dst)
		#geometry model
		models = ['Bathymetry.stl','BridgeStructure.stl']
		model_scr = 'Geometry/'
		model_dst = constant_dst + '/triSurface/'
		for model in models:
			src = model_scr + model
			dst = model_dst + model
			shutil.copyfile(src, dst)

	#prepare 0 folder for openfoam model
	def zeroFolder(self):
		CFDModelTemplateRoute = self.__srcroute()
		zero_scr = CFDModelTemplateRoute + '0'
		zero_dst = 'CFD-Model/0'
		shutil.copytree(zero_scr,zero_dst)

		#flow condition file
		ks = 2 * self.CFDdata['d50']
		Q,Ux,k,epsilon,nut = self.__initialValue()
		replacedict = {'Ux':str(Ux),'Q':str(Q),'k':str(k),'epsilon':str(epsilon),'nut':str(nut),'d50':str(ks)}
		route = zero_dst + '/flowCondition'
		replacement(route,replacedict)
		#velocity file
		U_dst = zero_dst + '/U'
		if Q > 0:
			U_src = zero_dst + '/U_velcoity'
		else:
			U_src = zero_dst + '/U_flowrate'
		shutil.copyfile(U_src,U_dst)

	#prepare system folder for openfoam model and return processor number
	def systemFolder(self):
		CFDModelTemplateRoute = self.__srcroute()
		system_scr = CFDModelTemplateRoute + 'system'
		system_dst = 'CFD-Model/system'
		shutil.copytree(system_scr,system_dst)
		route = system_dst + '/decomposeParDict'
		NumCore = int(self.CFDdata['Processor_Number'])
		replacedict = {'Processor_Number':str(int(self.CFDdata['Processor_Number']))}
		replacement(route,replacedict)
		return NumCore
	#time control dict
	'''######<<<<<<   TimeControl   >>>>>>######
	maxDeltaT: max allowable time step dt
	physicalTime: physical time
	delta: initial time step. the smaller one between 1e-6 and max allowable time step dt
	maxCo: single-phase is 15 and VOF is 150
	maxAlphaCo: single-phase is -1, not necessary, and VOF is 50
	'''
	def timeControlDicts(self):
		TimeControl = {}
		deltaT = min(1e-6,self.CFDdata['dt'])
		#single phase
		if abs(self.CFDdata['CFDMode'] - 1.0 ) <= tolerance :
			maxCo = 15
			maxAlphaCo = -1
			TimeControl = {'maxDeltaT':(self.CFDdata['dt']),'physicalTime':(self.CFDdata['physicalTime']),\
	 'deltaT':(deltaT),'maxCo':(maxCo),'maxAlphaCo':(maxAlphaCo)}
		#VOF
		if abs(self.CFDdata['CFDMode'] - 2.0 ) <= tolerance :
			maxCo = 150
			maxAlphaCo = 50
			TimeControl = {'maxDeltaT':(self.CFDdata['dt']),'physicalTime':(self.CFDdata['physicalTime']),\
	 'deltaT':(deltaT),'maxCo':(maxCo),'maxAlphaCo':(maxAlphaCo)}
		return TimeControl

	#controlDict setup
	def controlDict(self,TimeControl = {}):
		scr = 'system/controlDict_temp'
		route = 'system/controlDict'
		shutil.copyfile(scr,route)
		replacedict = {}
		replacedict['maxDeltaT'] = str(TimeControl['maxDeltaT'])
		replacedict['physicalTime'] = str(TimeControl['physicalTime'])
		replacedict['deltaT'] = str(TimeControl['deltaT'])
		replacedict['maxCo'] = str(TimeControl['maxCo'])
		replacedict['maxAlphaCo'] = str(TimeControl['maxAlphaCo'])
		replacement(route,replacedict)

	#DimensionAdjust dict
	'''######<<<<<<   DimensionAdjustDict   >>>>>>######
	Base_Size
	Xmax,Xmin,Ymax,Ymin
	WSE: water surface elevation
	Zmax: single-phase is WSE.
			VOF is 1.3 * (WSE - Zmin) + Zmin
	Zmin: Zmin of GEOdata - 1 * Base_Size
	'''
	def DimensionAdjustDict(self):
		DimensionAdjust = {}
		DimensionAdjust['Base_Size'] = self.CFDdata['Base_Size']
		DimensionAdjust['Xmax'] = self.GEOdata['Xmax']
		DimensionAdjust['Xmin'] = self.GEOdata['Xmin']
		DimensionAdjust['Ymax'] = self.GEOdata['Ymax']
		DimensionAdjust['Ymin'] = self.GEOdata['Ymin']
		DimensionAdjust['WSE'] = self.CFDdata['WSE']
		DimensionAdjust['Zmin'] = self.GEOdata['Zmin']- self.CFDdata['Base_Size']
		#single phase
		if abs(self.CFDdata['CFDMode'] - 1.0 ) <= tolerance :
			DimensionAdjust['Zmax'] = self.CFDdata['WSE']
		#VOF
		if abs(self.CFDdata['CFDMode'] - 2.0 ) <= tolerance :
			DimensionAdjust['Zmax'] = (self.CFDdata['WSE'] - self.GEOdata['Zmin']) * 1.3 + self.GEOdata['Zmin']
		return DimensionAdjust

	#blockMeshDict Setop
	def blockMeshDict(self,DimensionAdjust = {}):
		scr = 'system/blockMeshDict_temp'
		route = 'system/blockMeshDict'
		shutil.copyfile(scr,route)

		replacedict = {}
		NumX =int(np.rint((DimensionAdjust['Xmax']-DimensionAdjust['Xmin'])/DimensionAdjust['Base_Size']))
		NumY =int(np.rint((DimensionAdjust['Ymax']-DimensionAdjust['Ymin'])/DimensionAdjust['Base_Size']))
		NumZ1 =int(np.rint((DimensionAdjust['WSE']-DimensionAdjust['Zmin'])/DimensionAdjust['Base_Size']))
		NumZ2 =int(np.rint((DimensionAdjust['Zmax']-DimensionAdjust['WSE'])/DimensionAdjust['Base_Size']))
		replacedict['NumX'] = str(NumX)
		replacedict['NumY'] = str(NumY)
		replacedict['NumZ1'] = str(NumZ1)
		replacedict['NumZ2'] = str(NumZ2)
		replacedict['Xmax'] = str(DimensionAdjust['Xmax'])
		replacedict['Xmin'] = str(DimensionAdjust['Xmin'])
		replacedict['Ymax'] = str(DimensionAdjust['Ymax'])
		replacedict['Ymin'] = str(DimensionAdjust['Ymin'])
		replacedict['WSE'] = str(DimensionAdjust['WSE'])
		replacedict['Zmin'] = str(DimensionAdjust['Zmin'])
		replacedict['Zmax'] = str(DimensionAdjust['Zmax'])

		replacement(route,replacedict)

	#SHMParemeter dict
	'''######<<<<<<   SHMParemeterDict   >>>>>>######
	First_Cell: cell size of the first prism layer
	BedLayerN, BridgeLayerN: Prism layer number on riverbed and bridge
	BedSurface, BridgeSurface: Cell size on the surface of riverbed and bridge
	BedRegion,BridgeRegion: Cell size in the region around the riverbed and bridge
	'''
	def SHMParemeterDict(self):
		SHMParemeter = {}
		SHMParemeter['First_Cell'] = self.CFDdata['First_Cell']
		SHMParemeter['BedLayerN'] = self.CFDdata['BedLayerN']
		SHMParemeter['BridgeLayerN'] = self.CFDdata['BridgeLayerN']
		SHMParemeter['BedSurface'] = self.CFDdata['BedSurface']
		SHMParemeter['BridgeSurface'] = self.CFDdata['BridgeSurface']
		SHMParemeter['BedRegion'] = self.CFDdata['BedRegion']
		SHMParemeter['BridgeRegion'] = self.CFDdata['BridgeRegion']
		return SHMParemeter

	#SHMDict Setup
	def SHMDict(self,DimensionAdjust = {},SHMParemeter = {}):
		route = 'system/snappyHexMeshDict'
		scr = 'system/snappyHexMeshDict_temp'
		shutil.copyfile(scr,route)

		expansionRatio = self.CFDdata['Ratio']

		Base_Size = DimensionAdjust['Base_Size']
		Xmax = DimensionAdjust['Xmax']
		Ymax = DimensionAdjust['Ymax']
		Zmax = DimensionAdjust['Zmax']

		First_Cell = SHMParemeter['First_Cell']
		BedLayerN = SHMParemeter['BedLayerN']
		BridgeLayerN = SHMParemeter['BridgeLayerN']
		BedSurface = SHMParemeter['BedSurface']
		BridgeSurface = SHMParemeter['BridgeSurface']
		BedRegion = SHMParemeter['BedRegion']
		BridgeRegion = SHMParemeter['BridgeRegion']

		#mesh inner point
		Xinner = str(Xmax - 0.05 * Base_Size)
		Yinner = str(Ymax - 0.05 * Base_Size)
		Zinner = str(Zmax - 0.05 * Base_Size)
		InsidePoint = "( " + Xinner + " " + Yinner + " " + Zinner + " )"

		#prism layer
		BedLayerContent = ""
		BridgeStructureLayerContent = ""
		if BedLayerN < 0.1 and BridgeLayerN < 0.1:
			addLayers = 'false'
		else:
			addLayers = 'true'
		if BedLayerN > 0:
			BedLayerContent = "Bathymetry { nSurfaceLayers " + str(int(BedLayerN)) +"; }"
		else:
			BedLayerContent = ""
		if BridgeLayerN > 0:
			BridgeStructureLayerContent = "BridgeStructure { nSurfaceLayers " + str(int(BridgeLayerN)) +"; }"
		else:
			BridgeStructureLayerContent = ""

		#Feature and Surface Level
		BedFeatureLevel = int (Base_Size / BedSurface)
		BedSurfaceLevel = "(" + str(BedFeatureLevel)+" " +str(BedFeatureLevel)+")"
		PierFeatureLevel = int (Base_Size / BridgeSurface)
		PierSurfaceLevel = "(" + str(PierFeatureLevel)+" " +str(PierFeatureLevel)+")"

		#Region Level
		RiverBedRegion = ""
		BridgeStructureRegion = ""
		if BedRegion > 0:
			dl1 = 5 * Base_Size
			l1 = max(BedFeatureLevel,int(np.rint(Base_Size/BedRegion)))
			dl2 = 10 * Base_Size
			l2 = max(BedFeatureLevel,int(np.rint(Base_Size/BedRegion)-1))
			levels = "((" + str(dl1) + " " + str(l1) + ") (" + str(dl2) + " " + str(l2) + "));"
			RiverBedRegion = "RiverBed {  mode distance; levels " + levels +" gapLevelIncrement 1;}"
		if BridgeRegion > 0:
			dl1 = 10 * Base_Size
			l1 = max(BedFeatureLevel,int(np.rint(Base_Size/BridgeRegion)))
			dl2 = 20 * Base_Size
			l2 = max(BedFeatureLevel,int(np.rint(Base_Size/BridgeRegion)-1))
			levels = "((" + str(dl1) + " " + str(l1) + ") (" + str(dl2) + " " + str(l2) + "));"
			BridgeStructureRegion = "BridgeStructure {  mode distance; levels " + levels +" gapLevelIncrement 1;}"

		#replacedict
		replacedict = {'addLayers':addLayers,'BedFeatureLevel':str(BedFeatureLevel),\
					  'PierFeatureLevel':str(PierFeatureLevel),'RiverBedRegion':RiverBedRegion,\
					  'BedSurfaceLevel':BedSurfaceLevel,'PierSurfaceLevel':PierSurfaceLevel,\
					  'BridgeStructureRegion':BridgeStructureRegion,'InsidePoint':InsidePoint,\
					  'BedLayerContent':BedLayerContent,'BridgeStructureLayerContent':BridgeStructureLayerContent,\
					  'First_Cell':str(First_Cell),'expansionRatio':str(expansionRatio)}
		replacement(route,replacedict)
