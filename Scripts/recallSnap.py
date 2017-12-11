def msg(m):
    RPR_ShowConsoleMsg(m+'\n')    
names = 'Recall Snap #?';
dvalues = '';
maxreturnlen = 10;
nitems = len(dvalues.split(','));
# call dialog and get result
res = RPR_GetUserInputs('recording monitoring setup',nitems,names,dvalues,maxreturnlen);

# check if res[0] is true ('ok' pressed)
if res[0]:
    # the fourth item holds the input values
    resvalues = res[4].split(',');
    # get length of the new array and output all items
    rvlen = len(resvalues);
    i=0;




###################### 
######################

    if resvalues[0] == '1':
	    RPR_Main_OnCommand(53112, 0)
    elif resvalues[0] == '2':
	    RPR_Main_OnCommand(53113, 0);
