RPR_Main_OnCommand(40289,0)
track = RPR_GetSelectedTrack(0,0)
numItems = RPR_CountTrackMediaItems(track)
for index in range(0 , numItems):
	item = RPR_GetTrackMediaItem(track,index)
	muteState = RPR_GetMediaItemInfo_Value(item, "B_MUTE")
	RPR_SetMediaItemInfo_Value(item, "B_UISEL", muteState)
RPR_UpdateTimeline();
