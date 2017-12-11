
item = RPR_GetSelectedMediaItem(0,0)
track = RPR_GetMediaItem_Track(item)
startPos = RPR_GetMediaItemInfo_Value(item, "D_POSITION")
length = RPR_GetMediaItemInfo_Value(item, "D_LENGTH")
endPos = startPos + length
maxVertPos = 1
numItems = RPR_CountTrackMediaItems(track)
changed = 2
vertPos = RPR_GetMediaItemInfo_Value(item, "F_FREEMODE_Y")
nextUp = item


for itemIdx in range(0,numItems):
	thisItem = RPR_GetTrackMediaItem(track, itemIdx)
	thisStartPos = RPR_GetMediaItemInfo_Value(thisItem, "D_POSITION")	
	thisEndPos = RPR_GetMediaItemInfo_Value(thisItem, "D_LENGTH")	+ thisStartPos
# does it overlap?
	if endPos>thisStartPos and thisEndPos>startPos:
		thisVertPos = RPR_GetMediaItemInfo_Value(thisItem, "F_FREEMODE_Y")
		changed = 1
		if thisVertPos>vertPos and thisVertPos<maxVertPos: #keeps track of lowest
			nextUp = thisItem	
			maxVertPos = thisVertPos

if nextUp == item:
	RPR_Main_OnCommand(53387,0)
	RPR_Main_OnCommand(41140,0)	
	RPR_Main_OnCommand(53388,0)
	

RPR_SetMediaItemInfo_Value(nextUp, "B_UISEL", 1)
RPR_UpdateTimeline();






