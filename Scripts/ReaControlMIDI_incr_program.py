from reaper_python import *

def msg(m):
    RPR_ShowConsoleMsg(str(m) + '\n')

incrTrackHeight = lambda : RPR_Main_OnCommand(41325, 0) #Increase selected track heights
decrTrackHeight = lambda : RPR_Main_OnCommand(41326, 0) #Decrease selected track heights
undoBeginBock = lambda : RPR_Undo_BeginBlock2(0)
undoEndBlock = lambda name : RPR_Undo_EndBlock2(0,name,-1)

undoBeginBock()

#ReaControlMIDI parameters
BankMSB=0
BankLSB=1
Program=2

tr = RPR_GetSelectedTrack(0,0) #first selected track
numFX = RPR_TrackFX_GetCount(tr)
for fxIndex in range(0,numFX):
	rc = RPR_TrackFX_GetFXName(tr, fxIndex, "", 1024)
	plugname = rc[3]
	#msg(plugname)
	if "ReaControlMIDI" in plugname:
		# Get current parameter value, min. & max.
		fxp = RPR_TrackFX_GetParam(tr, fxIndex, Program, 0, 0);
		currProgram = fxp[0]
		minProgram = fxp[4]
		maxProgram = fxp[5]
		progInt = int(round(currProgram / (maxProgram/127)))
		#msg(progInt)
		if currProgram < maxProgram:
			newProg = (progInt+1.1)*(maxProgram/127)
			if newProg > maxProgram:
				newProg = maxProgram
			RPR_TrackFX_SetParam(tr, fxIndex, Program, newProg)
			#refresh tcp FX param controls
			incrTrackHeight()
			decrTrackHeight()
			#msg(newProg)
		break

undoEndBlock( 'Increment ReaControlMIDI Program' ) 