import re

def SelectTracksByName(name, exclusive) :
	for i in range(0, RPR_CountTracks(0) ) :
		pTrack = RPR_GetTrack(0, i)
		
		if name in RPR_GetSetMediaTrackInfo_String(pTrack, "P_NAME", "", 0)[3] :
			RPR_SetTrackSelected(pTrack, 1)
		elif exclusive :
			RPR_SetTrackSelected(pTrack, 0)

trackName = ""
retvals_csv_sz = ""
res=RPR_GetUserInputs("track Name", 1 , "name" , "" , 20)
if res[0]:
	# the fourth item holds the input values
	trackName = res[4]
SelectTracksByName(trackName,1);



# check if res[0] is true ('ok' pressed)

