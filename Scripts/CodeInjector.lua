reaper.Main_OnCommand (40001,0)
 track = reaper.GetSelectedTrack(0,0) 
 reaper.GetSetMediaTrackInfo_String (track,"P_NAME","sys-recording" ,1)
reaper.SetMediaTrackInfo_Value(track, "B_PHASE",0)
reaper.SetMediaTrackInfo_Value(track, "I_RECINPUT",1040)
reaper.SetMediaTrackInfo_Value(track, "I_RECMON",0)
reaper.SetMediaTrackInfo_Value(track, "I_SOLO",1)
reaper.SetMediaTrackInfo_Value(track, "I_RECARM",1)
