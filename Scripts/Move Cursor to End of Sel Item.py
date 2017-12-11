# Move Cursor to start of item
item = RPR_GetSelectedMediaItem(0,0)
startPos = RPR_GetMediaItemInfo_Value(item, "D_POSITION")
length = RPR_GetMediaItemInfo_Value(item, "D_LENGTH")
itemEnd = startPos + length
RPR_SetEditCurPos(itemEnd,1,0);
