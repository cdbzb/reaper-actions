local io = require("io");
TrackNumber = reaper.CountTracks(0)

for i = 0,(TrackNumber-1) do
	track = reaper.GetTrack(0,i)
	local _, name = reaper.GetSetMediaTrackInfo_String(track,"P_NAME","",false)
	io.popen ( "echo " ..i .."  " ..name .." >> ~/ActionWindowData/TrackList.txt")
	reaper.ShowConsoleMsg(name)
	reaper.ShowConsoleMsg("\n")
end




