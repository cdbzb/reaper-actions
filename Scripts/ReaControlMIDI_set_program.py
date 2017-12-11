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
		fxp = RPR_TrackFX_GetParam(tr, fxIndex, BankMSB, 0, 0)
		currBankMSB = fxp[0]
		minBankMSB = fxp[4]
		maxBankMSB = fxp[5]
		bankMsbInt=int(round(currBankMSB / (maxBankMSB/127)))
		fxp = RPR_TrackFX_GetParam(tr, fxIndex, BankLSB, 0, 0)
		currBankLSB = fxp[0]
		minBankLSB = fxp[4]
		maxBankLSB = fxp[5]
		bankLsbInt=int(round(currBankLSB / (maxBankLSB/127)))
		fxp = RPR_TrackFX_GetParam(tr, fxIndex, Program, 0, 0)
		currProgram = fxp[0]
		minProgram = fxp[4]
		maxProgram = fxp[5]
		progInt = int(round(currProgram / (maxProgram/127)))
		# user input dialog
		dialog_name = "ReaControlMIDI: FXparam"
		dialog_fields = 3
		dialog_field_names = 'Program (current='+str(progInt)+'), Bank (MSB), Bank (LSB)'
		dialog_default_values = ','+str(bankMsbInt)+','+str(bankLsbInt)+''
		dialog_maxreturnlength = 20 # have this at least one more than you expect as return length.
		User_Input = RPR_GetUserInputs(dialog_name, dialog_fields, dialog_field_names, dialog_default_values, dialog_maxreturnlength)
		#msg(progInt)
		if User_Input[0] == 1: # first item in the list it returns 1 (true) for "user clicked ok", 0 (false) for "cancel" 
			UserValues = User_Input[4].split(',') 	# the fourth item of the return holds the values the user typed into the fields.
			if UserValues[0]=="":
				UserValues[0]=str(progInt)
			if UserValues[1]=="":
				UserValues[1]=str(bankMsbInt)
			if UserValues[2]=="":
				UserValues[2]=str(bankLsbInt)
			if UserValues[0].isdigit() and UserValues[1].isdigit() and UserValues[2].isdigit():
				newProg = int(UserValues[0])
				newBankMsb = int(UserValues[1])
				newBankLsb = int(UserValues[2])
				if newProg >= 0 and newProg < 128:
					newProg = (newProg+0.1)*(maxProgram/127)
					RPR_TrackFX_SetParam(tr, fxIndex, Program, newProg)
				if newBankMsb >= 0 and newBankMsb < 127:
					newBankMsb = (newBankMsb+0.1)*(maxBankMSB/127)
					RPR_TrackFX_SetParam(tr, fxIndex, BankMSB, newBankMsb)
				if newBankLsb >= 0 and newBankLsb < 127:
					newBankLsb = (newBankLsb+0.1)*(maxBankLSB/127)
					RPR_TrackFX_SetParam(tr, fxIndex, BankLSB, newBankLsb)
				#refresh tcp FX param controls
				incrTrackHeight()
				decrTrackHeight()
				#msg(newProg)
		break

undoEndBlock( 'Set ReaControlMIDI Program/Bank' ) 
