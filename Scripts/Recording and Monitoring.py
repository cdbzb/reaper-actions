#for i in range(0,RPR_CountSelectedTracks(0)):
track = RPR_GetSelectedTrack(0,0);
recMode = RPR_GetMediaTrackInfo_Value(track,"I_RECMODE");
armed = RPR_GetMediaTrackInfo_Value(track,"I_RECARM");
monItems = RPR_GetMediaTrackInfo_Value(track,"I_RECMONITEMS");
monitor = RPR_GetMediaTrackInfo_Value(track,"I_RECMON");
# get monitoring / recording state

if recMode == 2: 
	recording = "not recording";
else: 
	recording = "recording";
if monItems:
	monitorItems = "on"
else:
	monitorItems = "off"
if monitor:
	if monitor == 2: inputMon = "auto";
	else: inputMon = "input";
else: inputMon = "off";
RPR_ShowConsoleMsg(recMode)
#RPR_SetMediaTrackInfo_Value(track,"I_HEIGHTOVERRIDE",height);
RPR_UpdateTimeline();
