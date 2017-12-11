# script to select next item left without moving cursor

#number of selected items
numberSelected = RPR_CountSelectedMediaItems(0)-1
item = RPR_GetSelectedMediaItem(0,numberSelected)
StartPos = RPR_GetMediaItemInfo_Value(item, "D_POSITION")	
track = RPR_GetMediaItem_Track(item)
numItems = RPR_CountTrackMediaItems(track)
maxStartPos = 10000000000
nextRight = item

#find closest item to right

for itemIdx in range(0,numItems):
# get the start position for this item
	thisItem = RPR_GetTrackMediaItem(track, itemIdx)
	thisStartPos = RPR_GetMediaItemInfo_Value(thisItem, "D_POSITION")	
	if thisStartPos > StartPos and thisStartPos <= maxStartPos:
		maxStartPos=thisStartPos
		nextRight = thisItem
RPR_SetMediaItemInfo_Value(nextRight, "B_UISEL", 1)	
RPR_UpdateTimeline();
	
	
