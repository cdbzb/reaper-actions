#script to select next overlapping item above selected item in FIPM track
#checks if an item in 'track' overlaps 'item', 
#if so returns the lowest overlapper otherwise returns 0

def lowestOverlapper (item,track): 
	startPos = RPR_GetMediaItemInfo_Value(item, "D_POSITION")
	length = RPR_GetMediaItemInfo_Value(item, "D_LENGTH")
	endPos = startPos + length
	minVertPos = 0.0
	numItems = RPR_CountTrackMediaItems(track)
	changed = 0
	vertPos = RPR_GetMediaItemInfo_Value(item, "F_FREEMODE_Y")
	nextUp = item
	for itemIdx in range(0,numItems):
		thisItem = RPR_GetTrackMediaItem(track, itemIdx)
		thisStartPos = RPR_GetMediaItemInfo_Value(thisItem, "D_POSITION")	
		thisEndPos = RPR_GetMediaItemInfo_Value(thisItem, "D_LENGTH") + thisStartPos
	# does it overlap?
		if (endPos > thisStartPos) and (thisEndPos > startPos):
			thisVertPos = RPR_GetMediaItemInfo_Value(thisItem, "F_FREEMODE_Y")
			changed = 1
			if (thisVertPos < vertPos) and (thisVertPos > minVertPos): #keeps track of lowest
				nextUp = thisItem	
				minVertPos = thisVertPos
	if changed > 0:	
		return nextUp
	else:
	    return nextUp;

item = RPR_GetSelectedMediaItem(0,0)
track = RPR_GetMediaItem_Track(item)
nextItem = lowestOverlapper( item , track )
if nextItem == item:
	RPR_Main_OnCommand(41139,0)
else:
	RPR_SetMediaItemInfo_Value(nextItem, "B_UISEL", 1)	
RPR_UpdateTimeline();

