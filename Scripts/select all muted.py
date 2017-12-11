RPR_Main_OnCommand(40331,0) #unselect all

trackNum = RPR_CountSelectedTracks(0)
for trackIdx in range(0,trackNum):
	thisTrack = RPR_GetSelectedTrack(0,trackNum)
	numItems = RPR_CountTrackMediaItems(thisTrack)
	
	for itemIdx in range(0,numItems):
		thisItem = RPR_GetTrackMediaItem(track, itemIdx)
		muteState = RPR_GetMediaItemInfo_Value(thisItem, "B_MUTE")
		RPR_SetMediaItemInfo_Value(thisItem,"B_UISEL", muteState )
RPR_UpdateTimeline();

