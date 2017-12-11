import re
#-------------------------------------------------------------------
# get_user_input_example.py
#-------------------------------------------------------------------
# define msg alias (custom)
def msg(m):
    RPR_ShowConsoleMsg(m+'\n')    
names = 'input';
dvalues = 'command';
maxreturnlen = 20;
nitems = len(dvalues.split(','));
# call dialog and get result
res = RPR_GetUserInputs('',nitems,names,dvalues,maxreturnlen);

# check if res[0] is true ('ok' pressed)
if res[0]:
	# the fourth item holds the input values
	resvalues = res[4].split(',')
	# get length of the new array and output all items
	rvlen = len(resvalues)
	i=0
	inputString = resvalues[0];
	inputStringList = re.split('(\d+)',inputString)
	argStringList = inputString.split(" ")
	argString = ""
	command = inputStringList[0]
	if len(argStringList)>1:
		command = argStringList[0]
		argString = argStringList[1]
	elif len(inputStringList)>1:
		args = int(inputStringList[1])


    #####Playrate Controls######
	if command == 'v-':
		RPR_Main_OnCommand(40523, 0)

	elif command == 'v+':
		RPR_Main_OnCommand(40522, 0)

	elif command == 'vv':
		RPR_Main_OnCommand(40521, 0)

#    elif command == 'ss':
#	    RPR_Main_OnCommand(RPR_NamedCommandLookup("_ACTIONSTRING"), 0)


	    

    ######   fipm
	elif command == 'fipm':
		RPR_Main_OnCommand(40751, 0)

	elif command == 'nofipm':
		RPR_Main_OnCommand(40752, 0)

	elif command == 'cleanup':
		RPR_Main_OnCommand(40645, 0)

    ######   folders
	elif command == 'zc':
		RPR_Main_OnCommand(RPR_NamedCommandLookup("_SWS_FOLDSMALL"), 0)

	elif command == 'zC':
		RPR_Main_OnCommand(RPR_NamedCommandLookup("_SWS_COLLAPSE"), 0)

	elif command == 'zo':
		RPR_Main_OnCommand(RPR_NamedCommandLookup("_SWS_UNCOLLAPSE"), 0)

	elif command == 'zs':
		RPR_Main_OnCommand(53539, 0)

	elif command == 'zp':
		RPR_Main_OnCommand(53642, 0)

   ######   tracks
	elif command == 'template':
		RPR_Main_OnCommand(46000, 0)

	elif command == 'anticipate':
		RPR_Main_OnCommand(40609, 0)

	elif command == 'noanticipate':
		RPR_Main_OnCommand(40610, 0)

	elif command == 'freeze':
		RPR_Main_OnCommand(54029, 0)

	elif command == 'unfreeze':
		RPR_Main_OnCommand(54030, 0)


   #####   preferences
	elif command == 'audio':
		RPR_Main_OnCommand(40099, 0)

   #####    Master
	elif command == 'mmute':
		RPR_Main_OnCommand(14, 0)

	#    elif command == 'mshow':
	#	    RPR_Main_OnCommand(14, 0)
   ##### Transport
	elif command == 'loop':
		RPR_Main_OnCommand(1068, 0)

   ##### Snapshots
	elif command == 'sw':
		RPR_Main_OnCommand(53145, 0)

	elif command == 'snap':
		RPR_Main_OnCommand(53075, 0)

	elif command == 'ssel':
		RPR_Main_OnCommand(53076, 0)

	elif command == 'scur':
		RPR_Main_OnCommand(53077, 0)
		
	elif command == 's':
		getOne = RPR_NamedCommandLookup("_SWSSNAPSHOT_GET1")
#	 snapNum = int(inputStringList[1])-1
	 
		RPR_Main_OnCommand(getOne + args - 1,0)


	elif command == 'S':
		getOne = RPR_NamedCommandLookup("_SWSSNAPSHOT_SAVE1")
		snapNum = int(inputStringList[1])-1
		RPR_Main_OnCommand(getOne + args - 1,0)

	elif command == "swind":
		RPR_Main_OnCommand(RPR_NamedCommandLookup("_SWSSNAPSHOT_OPEN"),0);

	elif command == "sname":
		RPR_Main_OnCommand(RPR_NamedCommandLookup("_SWSSNAPSHOT_NEWEDIT"),0);

	elif command == "svis":
		RPR_Main_OnCommand(RPR_NamedCommandLookup("_SWSSNAPSHOT_VISMODE"),0);

	elif command == "smix":
		RPR_Main_OnCommand(RPR_NamedCommandLookup("_SWSSNAPSHOT_MIXMODE"),0);

    ####### TrackView

	elif command == "tv":
		RPR_Main_OnCommand(40444 + args - 1,0);
	    

	elif command == "Tv":
		RPR_Main_OnCommand(40464 + args - 1,0);

    ######## Templates
	elif command == "pf":
		RPR_Main_OnCommand(RPR_NamedCommandLookup("_S&M_ADD_TRTEMPLATE1"),0);

    ######## Monitoring
	
	elif command == "mon":
		if argString == "tape":
			RPR_Main_OnCommand(40494,0)
		elif argString == "off":
			RPR_Main_OnCommand(40492,0)
		else: 	
			RPR_Main_OnCommand(40493,0)
	elif command == "lock":
		RPR_Main_OnCommand(40127,0) 
    ########### Toolbars 
	elif command == "nudge":
		RPR_SetExtState ("toolbars","active","nudge",1)
	elif command == "points":
		RPR_SetExtState ("toolbars","active","points",1)
	elif command == "tempo":
		RPR_SetExtState ("toolbars","active","tempo",1)
		

	RPR_Main_OnCommand(40679,0)
		

	RPR_Main_OnCommand(2,0)

