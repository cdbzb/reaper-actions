track = RPR_GetSelectedTrack(0,0);
RecMode = RPR_GetMediaTrackInfo_Value(track, "I_RECMODE")
if RecMode == 0: mode = 'input'
RPR_ShowConsoleMsg(mode)  ;

