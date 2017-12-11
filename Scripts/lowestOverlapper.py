#checks if an item in 'track' overlapps 'item', 
#if so returns the lowest overlapper otherwise returns 0
def lowestOverlapper (item,track): 
	startPos = RPR_GetMediaItemInfo_Value(item, "D_POSITION")
	length = RPR_GetMediaItemInfo_Value(item, "D_LENGTH")
	endPos = startPos + length
	minVertPos = 0
	numItems = RPR_CountTrackMediaItems(track)
	changed = 0

	for itemIdx in range(0,numItems):
		thisItem = RPR_GetTrackMediaItem(track, itemIdx)
		thisStartPos = RPR_GetMediaItemInfo_Value(thisItem, "D_POSITION")	
		thisEndPos = RPR_GetMediaItemInfo_Value(thisItem, "D_LENGTH")	+ thisStartPos
	# does it overlap?
		if endPos>thisStartPos and thisEndPos>startPos:
			thisVertPos = RPR_GetMediaItemInfo_Value(thisItem, "F_FREEMODE_Y")
			changed = 1
			if thisVertPos<vertPos and thisVertPos>minVertPos: #keeps track of lowest
				nextUp = thisItem	
				minVertPos = thisVertPos
	if changed:	
		return nextUp
	else:
	    return 0;
	    
