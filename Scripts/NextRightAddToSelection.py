#if there are multiple items selected
#choose right
numSelected = RPR_CountSelectedMediaItems(0)
item = RPR_GetSelectedMediaItem(0,numSelected-1)
StartPos = RPR_GetMediaItemInfo_Value(item, "D_POSITION")	
track = RPR_GetMediaItem_Track(item)
numItems = RPR_CountTrackMediaItems(track)
maxStartPos = 10000000
nextLeft = item

	#find closest item to left

for itemIdx in range(0,numItems):
# get the start position for this item
	thisItem = RPR_GetTrackMediaItem(track, itemIdx)
	thisStartPos = RPR_GetMediaItemInfo_Value(thisItem, "D_POSITION")	
	if thisStartPos > StartPos and thisStartPos <= maxStartPos:
		maxStartPos=thisStartPos
		nextLeft = thisItem
RPR_SetMediaItemInfo_Value(nextLeft, "B_UISEL", 1)	
RPR_UpdateTimeline();
