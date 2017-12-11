# move cursor to offset of take
item = RPR_GetSelectedMediaItem(0,0)
take = RPR_GetTake(item, 0)
offset = RPR_GetMediaItemTakeInfo_Value(take, "D_STARTOFFS")
offset2 = ( offset )  * (1.001) 
RPR_SetEditCurPos(offset2 ,1, 0);

