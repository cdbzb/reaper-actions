# Move Cursor to start of item
item = RPR_GetSelectedMediaItem(0,0)
StartPos = RPR_GetMediaItemInfo_Value(item, "D_POSITION")
RPR_SetEditCurPos(StartPos,1,0);
