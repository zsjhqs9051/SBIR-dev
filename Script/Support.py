from itertools import islice
import numpy as np
import pandas as pd
import os
import sys
import shutil
import time

#find the index of the substring appeared the Nth times
def findSubstring(string,substring,times):
	current = 0
	for i in range(1,times+1):
		current = string.find(substring,current) + 1
	if current == 0 :return -1
	return current-1

#read the file from the last n Line
def file_last_N_line(route,n=0):
	content_NOT_enough = True
	i = 1
	while content_NOT_enough:
		Nbite = -3000 * i
		file = open(route,'rb')
		file.seek(0,2)
		file.seek(-3000,2)
		#content = file.read()
		content = file.read().decode('utf-8')
		#content1 = file.read()
		Nline = content.count('\n',0,-1)+1
		if Nline >= n:
			enterN = Nline - n
			index = findSubstring(content,'\n',enterN) + 1
			filedata = content[index:].split('\n')
			content_NOT_enough = False
		else:
			i = i +1
	return filedata

#inpute check
def input_check(title,data):#need to change
	value = -1.0
	Error_Log = "Temp/Error_Log.txt"
	if len(data) == 0:
		pass
	else:
		try:
			value = float(data)
		except ValueError:
			with open (Error_Log, "a") as Error_Log :
				content = title + " is NaN\n"
				Error_Log.write(content)
	return value

#replace the target symble
def replacement(route,replacedict = {}):
	with open(route) as file:
		content = file.read()
	for key, value in replacedict.items():
		keyword = '%' + key + '%'
		content = content.replace(keyword,value)
	with open(route,'w') as newfile:
		newfile.write(content)

#TimeStamp
def TimeStamp ():
	return time.strftime ( '%Y-%m-%d %H:%M:%S: ' )

#Log write function
class SimpleLog ( ):
	def __init__ ( self, FileName=None ):
		self.File = None
		if FileName is not None:
			self.File = open ( FileName, 'a' )
			self.File.write ( '\n' )
			self.File.write ( '\n' )
	def Log ( self, *Args ):
		Message = ' '.join ( map ( str, Args ) )
		if self.File is not None:
			for Line in Message.rstrip ().split ( '\n' ):
				self.File.write ( TimeStamp () + Line.rstrip () + '\n' )
		else:
			for Line in Message.rstrip ().split ( '\n' ):
				print (TimeStamp() + Line.rstrip())
	def Flush ( self ):
		if self.File is not None:
			self.File.flush ()
		else:
			sys.stdout.flush ()
	def __del__ ( self ):
		if self.File is not None:
			self.File.close ()

#recover from fail
def RecoverOpenFoam(RecoveryId,Tool,Log,DimensionAdjust={}):
	MaxRecoveryIter = 5
	basesize = DimensionAdjust['Base_Size']
	Xmax = DimensionAdjust['Xmax']
	Xmin = DimensionAdjust['Xmin']
	Ymax = DimensionAdjust['Ymax']
	Ymin = DimensionAdjust['Ymin']
	LogFile = SimpleLog ( 'log_recovery.log' )
	if RecoveryId >= MaxRecoveryIter - 1:
		Log.Log ( '"' + Tool + '" failed (no more recovery options left)' )
		LogFile.Log ( '"' + Tool + '" failed (no more recovery options left)' )
		del LogFile
		sys.exit ()
	Log.Log ( '"' + Tool + '" failed (now starting recovery #' + str ( RecoveryId + 1 ) + ')' )
	Log.Log ( 'The previous base size was', basesize )
	LogFile.Log ( '"' + Tool + '" failed (now starting recovery #' + str ( RecoveryId + 1 ) + ')' )
	LogFile.Log ( 'The previous base size was', basesize )

	CorrectionId = RecoveryId + 1
	if CorrectionId % 2 == 1:
		DimensionAdjust['Base_Size'] = basesize * 0.9
	else:
		DimensionAdjust['Base_Size'] = basesize * 1.1

	Log.Log ( 'The base cell size is changed as', DimensionAdjust['Base_Size'])
	LogFile.Log ( 'The base cell size is changed as', DimensionAdjust['Base_Size'])
	del LogFile
	return DimensionAdjust

#Mesh analysis and modification
class MeshAnalysis():
	def __init__(self):
		pass
	#Prism Layer Check, return dict LayerCover {'surface': coverage}
	def PrismLayerCheck(self):
		SHMLog = 'log_snappyHexMesh.log'
		LogPM = SimpleLog()
		LayCoverInfo = []
		LayCoverInfo.append('Prism Layer Analysis')

		logfile = open(SHMLog,'rb')
		logcontents = file_last_N_line(SHMLog,50)
		LayerCover = {}
		SHMFail = 0
		for i in range(5):
			j = -1*i - 1
			line = logcontents[j]
			if line.find("Finalising") < 0:
				SHMFail = SHMFail -1
			else:
				SHMFail = 1
				break
		if SHMFail >= 0:
			for i in range(len(logcontents)):
				line = logcontents[i]
				if line.find("overall thickness") >0 :
					for k in range(3):
						locationa = findSubstring(logcontents[i+k],':',3) + 2
						NoTimeContent = logcontents[i+k][locationa:]
						LayCoverInfo.append(NoTimeContent)

					for j in range (2):
						PrismInfo = logcontents[i+3+j]
						location = findSubstring(PrismInfo,':',3) + 2
						MeanfullInfo = PrismInfo[location:]
						if MeanfullInfo is not '':
							LayCoverInfo.append(MeanfullInfo)
							clean_str = ' '.join(MeanfullInfo.split())
							LayerCover[clean_str.split(' ')[0]] = float(clean_str.split(' ')[4])
					if not 'Bathymetry' in LayerCover.keys():
						LayerCover['Bathymetry' ] = 999
					if not 'BridgeStructure' in LayerCover.keys():
						LayerCover['BridgeStructure' ] = 999
			if not LayerCover :
				LayCoverInfo.append('      ')
				LayCoverInfo.append('There is no prism layer')
		else:
			LayCoverInfo.append('\tSnappyHexMesh Fail')
		return SHMFail,LayerCover,LayCoverInfo

	#Prism Layer Modification
	def PrismLayerModification(self,PMID,DimensionAdjust={},SHMParemeter={}):
		LayerCover = {}
		LayCoverInfo = []
		SHMFail,LayerCover,LayCoverInfo = self.PrismLayerCheck()
		PMCode = -1
		if SHMFail < 0:
			PMCode = 1
		else:
			if LayerCover['Bathymetry'] > 100 and LayerCover['BridgeStructure'] > 100:
				LayerCover = {}
			if LayerCover:
				if PMID == 2:
					PMCode = 1
					SHMParemeter['BedLayerN'] = 0
					SHMParemeter['BridgeLayerN'] = 0
					SHMParemeter['BedRegion'] = 0
					SHMParemeter['BridgeRegion'] = 0
				else:
					if LayerCover['Bathymetry'] <= 75:
						PMCode = 1
						SHMParemeter['First_Cell'] = 0.5 * DimensionAdjust['Base_Size']
						SHMParemeter['BedLayerN'] = 1
						SHMParemeter['BridgeLayerN'] = 0
						SHMParemeter['BedRegion'] = 0
						SHMParemeter['BridgeRegion'] = 0
					elif LayerCover['BridgeStructure'] <= 75:
						PMCode = 1
						SHMParemeter['BridgeLayerN'] = 0
		return SHMParemeter,PMCode,LayCoverInfo

	#check MeshCheck error，return MeshError
	def MeshCheckLog(self):
		MeshCheckLog = 'log_checkMesh.log'
		MeshErrorInfo = []
		MeshCode = -1
		MeshErrorInfo.append( 'Mesh Check Analysis' )
		logfile = open(MeshCheckLog,'r')
		logdata = logfile.read()
		start_index = logdata.find('Checking geometry')
		end_index = logdata.rfind('End')
		contents = logdata[start_index:end_index].split('\n')
		MeshError = 0
		for line in contents:
			if line.find('***') > 0:
				MeshError = MeshError + 1
				index = findSubstring(line,':',3) + 1
				MeshErrorInfo.append(line[index:])
		if MeshError > 1:
			MeshCode = 1
			MeshErrorInfo.append('Too Many Mesh Error')
		else:
			MeshErrorInfo.append('Mesh is Acceptable')
		return MeshCode,MeshErrorInfo
