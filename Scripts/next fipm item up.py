# next item up in same track

item = RPR_GetSelectedMediaItem(0,0)
startPos = RPR_GetMediaItemInfo_Value(item, "D_POSITION")
length = RPR_GetMediaItemInfo_Value(item, "D_LENGTH")
endPos = startPos + length
vertPos = RPR_GetMediaItemInfo_Value(item, "F_FREEMODE_Y")
track = RPR_GetMediaItem_Track(item)
numItems = RPR_CountTrackMediaItems(track)
itemIdx = 0
minVertPos = 0
nextUp = item

# deselect
RPR_SetMediaItemInfo_Value(item, "B_UISEL", 0)

for itemIdx in range(0,numItems):
	thisItem = RPR_GetTrackMediaItem(track, itemIdx)
	thisStartPos = RPR_GetMediaItemInfo_Value(thisItem, "D_POSITION")	
	thisEndPos = RPR_GetMediaItemInfo_Value(thisItem, "D_LENGTH")	+ thisStartPos
# does it overlap?
	if endPos>thisStartPos and thisEndPos>startPos:
		thisVertPos = RPR_GetMediaItemInfo_Value(thisItem, "F_FREEMODE_Y")
		if thisVertPos<vertPos and thisVertPos>minVertPos:
			nextUp = thisItem
			minVertPos = thisVertPos
RPR_SetMediaItemInfo_Value(nextUp, "B_UISEL", 1)	
RPR_UpdateTimeline();
