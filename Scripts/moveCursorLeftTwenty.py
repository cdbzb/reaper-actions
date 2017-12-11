
pixPerSec = RPR_GetHZoomLevel()
NumPix = ( -20 / pixPerSec)
RPR_MoveEditCursor(NumPix ,0)
RPR_UpdateTimeline();




