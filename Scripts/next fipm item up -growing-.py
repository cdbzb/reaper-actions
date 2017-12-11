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
changed = 0

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
			changed = 1
			minVertPos = thisVertPos
#did we find an averlapping item on the same track?
if changed = 1:
	RPR_SetMediaItemInfo_Value(nextUp, "B_UISEL", 1)	
	RPR_UpdateTimeline();
#if not search the tracks above
else trackNumber = RPR_GetMediaTrackInfo_Value(track , "IP_TRACKNUMBER")
	for upFromTrackIdx in range(1,trackNumber):
		thisTrack = RPR_GetTrack(0,trackNumber - upFromTrackIdx)
		thisNumItems = RPR_CountTrackMediaItems(thisTrack)
		
		if RPR_GetMediaTrackInfo_Value(track , "B_SHOWINTCP"):
		
