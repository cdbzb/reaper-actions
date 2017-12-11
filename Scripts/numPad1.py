toolbar = RPR_GetExtState("toolbars","active");
command = int(RPR_GetExtState(toolbar,"1"));
RPR_Main_OnCommand( command, 0 );
