# script to select next item left without moving cursor

item = RPR_GetSelectedMediaItem(0,0)
StartPos = RPR_GetMediaItemInfo_Value(item, "D_POSITION")	
track = RPR_GetMediaItem_Track(item)
numItems = RPR_CountTrackMediaItems(track)
maxStartPos = 10000000
nextLeft = item

# deselect
RPR_SetMediaItemInfo_Value(item, "B_UISEL", 0)

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
	
	
