import pandas as pd
import numpy as np
import shutil
import os
import sys
import shlex
import select
import subprocess
from Script.Support import *

# delete Processor Folder
def DeleteProcessors():
	cmd = 'rm -rf processor*'
	os.system (cmd)

#OpenFOAMCMD, return RetCode
def RunOpenFOAMTool(Tool, Options = '',NumberCores = 16, Log = None, TimeControl = {}):
	if Log is None:
		Log = SimpleLog()
	if Options !='':
		Options = ' ' + Options
	if NumberCores is None:
		cmd = Tool + Options
		RetCode = Execute(cmd, Tool, Log)
	else:
		if Tool == 'snappyHexMesh' or Tool == 'pimpleFoam' or Tool == 'interFoam':
			cmd = 'mpirun -np ' + str (int(NumberCores)) + ' ' + Tool + Options + ' -parallel'
		else:
			cmd = Tool + Options
		RetCode = Execute(cmd, Tool, Log,TimeControl = TimeControl)
	Log.Log ( 'Return code from "' + Tool + '" is ' + str ( RetCode ) )
	return RetCode

class DummyProcessor ( ):
	def __init__ ( self ):
		pass
	def Process ( self, Line ):
		return 0, 'OK'

class SolverProcessor ( ):
	def __init__ ( self,TimeControl ):
		self.NumSmallDeltaT = 0
		self.MinimumDeltaT = 1e-7
		self.TargetDeltaT = TimeControl['maxDeltaT']
		self.AllowableTargetCount = TimeControl['maxCo']
	def Process ( self, Line ):
		if Line.startswith ( 'deltaT = ' ):
			DeltaT = float ( Line.strip ().split ( '=' )[1] )
			if DeltaT < self.MinimumDeltaT:
				return 1, 'deltaT at ' + str (DeltaT) + ' is below the minimum of ' + str ( self.MinimumDeltaT )
		return 0, 'OK'

#Execute openfoam cmd
def Execute(Command,Tool,Log = None, TimeControl = {}):
	TimeOut = 300.0
	if Log is None:
		Log = SimpleLog()
	if Tool == 'pimpleFoam':
		LineProcessor = SolverProcessor (TimeControl)
	else:
		LineProcessor = DummyProcessor ()
	Args = shlex.split ( Command )
	Process = subprocess.Popen ( Args, bufsize=0, stdout=subprocess.PIPE, stderr=subprocess.STDOUT )
	LogFile = SimpleLog ( 'log_' + Tool + '.log' )
	Log.Log ( '********** Executing "' + Command + '" **********' )
	LogFile.Log ( '********** Executing "' + Command + '" **********' )
	# these variables are used to check for special conditions in the output
	UserRetCode = 0
	MpiRetCode = 0
	Reason = ''
	AbortRequested = False
	EndLineCounter = None
	LastFlush = time.time ()
	NeedsFlush = False
	FlushInterval = 1.0
	LastAlive = time.time ()
	Line = ''
	while True:
		ProcessRetCode = Process.poll ()
		Streams = select.select ( [ Process.stdout ], [], [], 0.1 )[0]
		for Stream in Streams:
			while True:
				Byte = Stream.read ( 1 ).decode("utf-8")
				if Byte != '\n':
					Line = Line + Byte
					break
				Log.Log ( Line )
				LogFile.Log ( Line )
				NeedsFlush = True
				LastAlive = time.time ()
				if Line.strip ().lower () in ( 'end', 'end.' ):
					EndLineCounter = 0
				if EndLineCounter != None:
					EndLineCounter += 1
				UserRetCode, Reason = LineProcessor.Process ( Line )
				if UserRetCode > 0:
					AbortRequested = True
				if Line.startswith ( 'MPI_ABORT' ):
					AbortRequested = True
					MpiRetCode = 1
				if AbortRequested:
					break
				Line = ''
			if AbortRequested:
				break
		if ProcessRetCode is not None:
			break
		if AbortRequested:
			break
		Now = time.time ()
		if NeedsFlush and Now > LastFlush + FlushInterval:
			Log.Flush ()
			LogFile.Flush ()
			LastFlush = Now
			NeedsFlush = False

		if Now - LastAlive > TimeOut:
			AbortRequested = True
			UserRetCode = 3
			Reason = 'No output lines received for ' + str ( Now - LastAlive ) + ' seconds, "' + str ( Tool ), '" is assumed to be dead'
			break

	if AbortRequested:
		if ProcessRetCode is None:
			try:
				Process.kill ()
			except:
				pass
		if UserRetCode > 0:
			Log.Log ( '********** Output analysis triggered termination:', Reason )
			return 1
		if MpiRetCode > 0:
			if EndLineCounter is None:
				Log.Log ( '********** MPI problem triggered termination' )
				return 2
			else:
				Log.Log ( '********** MPI problem at the end of the run, possible problem' )
				return 0
		Log.Log ( '********** Unhandled OpenFOAM tool termination, this should not happen!' )
		sys.exit ()
	else:
		if ProcessRetCode is not None:
			if ProcessRetCode != 0:
				Log.Log ( '********** An error code was returned by the tool' )
				return ProcessRetCode
	Log.Log ( '********** Done "' + Command + '" **********\n' )
	Log.Flush ()
	LogFile.Log ( '********** Done "' + Command + '" **********\n' )
	del LogFile
	return 0
