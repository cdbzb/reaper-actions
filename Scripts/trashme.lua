track = reaper.GetSelectedTrack(0,0) 
test = reaper.GetMediaTrackInfo_Value(track,"I_RECINPUT",1)
reaper.ClearConsole()
reaper.ShowConsoleMsg ((test-4096)/32 )

