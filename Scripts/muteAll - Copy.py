# This Reaper script toggles Mute for all tracks
# RPR_ShowConsoleMsg("Starting script...\n")

# count # tracks
numTracks = RPR_CountTracks(0)
# RPR_ShowConsoleMsg("Main project has " + str(numTracks) + " tracks.\n")

# iterate through all tracks
for trackIdx in range(0,numTracks):
# get the track object for this track number
	track = RPR_GetTrack(0, trackIdx)	
	isMuted = RPR_GetMediaTrackInfo_Value(track, "B_MUTE")
	if isMuted==0:
# track IS NOT muted: mute track
		RPR_SetMediaTrackInfo_Value(track, "B_MUTE", 1.0)
	else: 
# track IS muted, unmute track
		RPR_SetMediaTrackInfo_Value(track, "B_MUTE", 0.0)

# RPR_ShowConsoleMsg("Toggled mute for all tracks\n");
