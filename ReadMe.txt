Support.py
	1. findSubstring(string,substring,times)
		finde the the index of the Nth of the sub-string appearing in the string
		
	2. file_last_N_line(route,n=0))
		read the file from the end
		
	3. input_check(title,data):
	
	4. replacement(route,replacedict)
		a. route: location of the file, which needs to replace the string with data value
		b. replacedict: string and the value of this string
		
	5. TimeStamp()
	
	6. SimpleLog()
	
	7. RecoverOpenFoam(RecoveryId,Tool,Log,DimensionAdjust={})
		recover from the mesh fail and openfoam running fail
	8. MeshAnalysis()
		a. PrismLayerCheck()
			check whether there is any prism layer
			check the coverage of each prism layer
		b. PrismLayerModification(PMID,DimensionAdjust={},SHMParemeter={})
			PMID = 0,1: modify the SHM setup to only generate 1 layer with size of 0.5*base_size on the bathymetry
			PMID = 2: disable all prism layer
			
		c. MeshCheckLog()
			check the mesh error number
#######################################################################################################################


Main.py
	1. Generate CFD model folder: CFD-Model
	2. Generate the folder for Geometry: Geometry
	3. Generate the folder for geometry informationa and CFD data information: temp
	4. Geometry code, NOT inlcuded now
		a. convert bathymetry point cloud to stl file
		b. insert the bridge model to the right location
	5. CFD information input, NOT included now
		CFD Model: 1 - single phase; 2 - VOF
				1 is the default value
		WSE: water surface elevation;
		d50: d50 of sand
			0.001 m is the default value
		Q: flow rate; 
		Ux: approach velocity. 
			Only one of Q and Ux is allowable to be input
		Base_Size: base size of mesh
		BedLayerN, BridgeLayerN: Prism layer number on riverbed and bridge
								default values are 0
		First_Cell: cell size of the first prism layer
		BedSurface, BridgeSurface: Cell size on the surface of riverbed and bridge
								default values are Base_Size
		BedRegion,BridgeRegion: Cell size in the region around the riverbed and bridge
								default values are 0
		Ratio: ratio of cell sizes between different prism layers, default value is 1.5
								default value is 1.5
		dt: max allowable time step
		physicalTime: physical time
	6. CFD Conduct, single-phase finished
#######################################################################################################################


CFD_executation.py
	1. DeleteProcessors()
		remove processors
	
	2.RunOpenFOAMTool(Tool, Options = '',NumberCores = 16, Log = None, TimeControl = {})
		load openfoam cmd
		a. class DummyProcessor()
		b. class SolverProcessor()
			i. dis-converge
		c. Execute(Command,Tool,Log = None, TimeControl = {})
			run the cmd and record output information
	
		
#######################################################################################################################


Preparation.py //finished
	1. __init__()
		load the input geometry dimension and CFD information 
	2. __srcroute()
		CFD Template Source: 'Configure/SF_Model/' or 'Configure/VOF/'
	3. __initialValue()
		estimated initial k epsilon nut Q and Ux
	4. constantFolder(), zeroFolder(), and systemFolder()
		a. generate folder "constant", "0" and system 
		b. copy geometry files to constant/triSurface
		c. replace the data values in "0/flowCondition"
		d. determines the input of initial velocity:  Q or Ux
		e. replace the process number value in "system/decomposeParDict"
	5. timeControlDicts(TimeControl)
		return dict TimeControl
			maxDeltaT: max allowable time step dt
			physicalTime
			delta: initial time step. the smaller one between 1e-6 and max allowable time step dt
			maxCo: single-phase is 15 and VOF is 150
			maxAlphaCo: single-phase is -1, not necessary, and VOF is 50
	6. controlDict()
		replace the data values in "system/controlDict"
	7. DimensionAdjustDict()
		return dict DimensionAdjustDict
			Base_Size, Xmax,Xmin,Ymax,Ymin
			WSE: water surface elevation
			Zmax: single-phase is WSE. VOF is 1.3 * (WSE - Zmin) + Zmin
			Zmin: Zmin of riverbed - 1 * Base_Size
	8. blockMeshDict(DimensionAdjustDict) 	
		replace the data values in "system/blockMeshDict" 
	9. SHMParemeterDict()
		return dict SHMParemeterDict
			First_Cell: cell size of the first prism layer
			BedLayerN, BridgeLayerN: Prism layer number on riverbed and bridge
			BedSurface, BridgeSurface: Cell size on the surface of riverbed and bridge
			BedRegion,BridgeRegion: Cell size in the region around the riverbed and bridge
	10. SHMDict(DimensionAdjustDict,SHMParemeterDict)
		replace the data values in "system/snappyHexMeshDict" 
#######################################################################################################################
