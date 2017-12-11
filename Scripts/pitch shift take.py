names = 'set,shift';
dvalues = '0,0';
maxreturnlen = 10;
nitems = len(dvalues.split(','));
# call dialog and get result
res = RPR_GetUserInputs('shift or set pitch',nitems,names,dvalues,maxreturnlen);
# check if res[0] is true ('ok' pressed)
if res[0]:
    # the fourth item holds the input values
    resvalues = res[4].split(',');
	# get set and shiftt amts
    set = float(resvalues[0]);
    shift = float(resvalues[1]);
numItems = RPR_CountSelectedMediaItems(0);
i = 0
for i in range(0, numItems):
	item = RPR_GetSelectedMediaItem(0,i)
	take = RPR_GetActiveTake(item)
	curPitch = RPR_GetMediaItemTakeInfo_Value(take,"D_PITCH");
	if shift <> 0:
		newPitch = curPitch + shift;
	else:
		newPitch = set;
	RPR_SetMediaItemTakeInfo_Value(take,"D_PITCH",newPitch);
RPR_UpdateTimeline();
