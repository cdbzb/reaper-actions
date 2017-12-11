toolbar = RPR_GetExtState("toolbars","active")
keypress = RPR_GetExtState("toolbars","keypress")
nop = 65535

numpadtool = {};


numpadtool [ ("points",'7') ] = RPR_NamedCommandLookup('_SWS_BRMOVEEDITTOPREVENV')  
numpadtool [ ("points",'8') ] = 41180  
numpadtool [ ("points",'9') ] = RPR_NamedCommandLookup('_SWS_BRMOVEEDITTONEXTENV')  
numpadtool [ ("points",'4') ] = RPR_NamedCommandLookup('_BR_ENV_SEL_PREV_POINT')  
numpadtool [ ("points",'5') ] = 40330 
numpadtool [ ("points",'6') ] = RPR_NamedCommandLookup('_BR_ENV_SEL_NEXT_POINT') 
numpadtool [ ("points",'1') ] = nop 
numpadtool [ ("points",'2') ] = 41181
numpadtool [ ("points",'3') ] = nop 
numpadtool [ ("points",'-') ] = 41863 
numpadtool [ ("points",'+') ] = 41864 


numpadtool [ ("nudge",'7') ] = RPR_NamedCommandLookup('_SWS_SELTRKWITEM') 
numpadtool [ ("nudge",'8') ] = 40117 
numpadtool [ ("nudge",'9') ] = nop 
numpadtool [ ("nudge",'4') ] = 40120 
numpadtool [ ("nudge",'5') ] = nop 
numpadtool [ ("nudge",'6') ] = 40119 
numpadtool [ ("nudge",'1') ] = 40123 
numpadtool [ ("nudge",'2') ] = 40118 
numpadtool [ ("nudge",'3') ] = 40124 
numpadtool [ ("nudge",'-') ] = 40126 
numpadtool [ ("nudge",'+') ] = 40125 




RPR_Main_OnCommand( numpadtool[(toolbar,keypress)], 0 );





