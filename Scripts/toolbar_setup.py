

nop = 65535

RPR_SetExtState("points",'7',RPR_NamedCommandLookup('_SWS_BRMOVEEDITTOPREVENV')  ,1);
RPR_SetExtState("points",'107',"",1);
RPR_SetExtState("points",'8',41180  ,1);
RPR_SetExtState("points",'108',"",1);
RPR_SetExtState("points",'9',RPR_NamedCommandLookup('_SWS_BRMOVEEDITTONEXTENV')  ,1);
RPR_SetExtState("points",'109',"",1);
RPR_SetExtState("points",'4',RPR_NamedCommandLookup('_BR_ENV_SEL_PREV_POINT')  ,1);
RPR_SetExtState("points",'104',"",1);
RPR_SetExtState("points",'5',40330 ,1);
RPR_SetExtState("points",'105',"",1);
RPR_SetExtState("points",'6',RPR_NamedCommandLookup('_BR_ENV_SEL_NEXT_POINT') ,1);
RPR_SetExtState("points",'106',"",1);
RPR_SetExtState("points",'1',nop ,1);
RPR_SetExtState("points",'101',"",1);
RPR_SetExtState("points",'2',41181,1);
RPR_SetExtState("points",'102',"",1);
RPR_SetExtState("points",'3',nop ,1);
RPR_SetExtState("points",'103',"",1);
RPR_SetExtState("points",'-',41863 ,1);
RPR_SetExtState("points",'10-',"",1);
RPR_SetExtState("points",'+',41864 ,1);
RPR_SetExtState("points",'10+',"",1);

RPR_SetExtState("nudge",'7',RPR_NamedCommandLookup('_SWS_SELTRKWITEM') ,1);
RPR_SetExtState("nudge",'107',"<=" ,1);
RPR_SetExtState("nudge",'8',40117 ,1);
RPR_SetExtState("nudge",'108',"^" ,1);
RPR_SetExtState("nudge",'9',nop ,1);
RPR_SetExtState("nudge",'109',"NOP" ,1);

RPR_SetExtState("nudge","4",40120 ,1);
RPR_SetExtState("nudge","104","<" ,1);
RPR_SetExtState("nudge",'5',nop ,1);
RPR_SetExtState("nudge",'105',"NOP",1);
RPR_SetExtState("nudge",'6',40119 ,1);
RPR_SetExtState("nudge",'106',">" ,1);

RPR_SetExtState("nudge",'1',40123 ,1);
RPR_SetExtState("nudge",'101',"<Cont" ,1);
RPR_SetExtState("nudge",'2',40118 ,1);
RPR_SetExtState("nudge",'102',"V" ,1);
RPR_SetExtState("nudge",'3',40124 ,1);
RPR_SetExtState("nudge",'103',"Cont>" ,1);
RPR_SetExtState("nudge",'10-',"Tk^" ,1);
RPR_SetExtState("nudge",'-',40126 ,1);
RPR_SetExtState("nudge",'10+',"Tkv" ,1);
RPR_SetExtState("nudge",'+',40125 ,1);


RPR_SetExtState("tempo",'7',RPR_NamedCommandLookup('_BR_MOVE_L_GRID_TO_EDIT_CUR') ,1);
RPR_SetExtState("tempo",'107',"| >|  " ,1);
RPR_SetExtState("tempo",'8',40484 ,1);#Item Timeabase to Beats, Length, Rate
RPR_SetExtState("tempo",'108'," B.R " ,1);
RPR_SetExtState("tempo",'9',RPR_NamedCommandLookup('_BR_MOVE_R_GRID_TO_EDIT_CUR') ,1);
RPR_SetExtState("tempo",'109',"|< |" ,1);

RPR_SetExtState("tempo","4",40120 ,1);
RPR_SetExtState("tempo","104","<" ,1);
RPR_SetExtState("tempo",'5',41885 ,1); #toggle framegrid
RPR_SetExtState("tempo",'105',"Frm",1);
RPR_SetExtState("tempo",'6',40119 ,1);
RPR_SetExtState("tempo",'106',">" ,1);

RPR_SetExtState("tempo",'1',40123 ,1);
RPR_SetExtState("tempo",'101',"<Cont" ,1);
RPR_SetExtState("tempo",'2',40433 ,1);#Item timebase to Time
RPR_SetExtState("tempo",'102',"Tme" ,1);
RPR_SetExtState("tempo",'3',40124 ,1);
RPR_SetExtState("tempo",'103',"Cont>" ,1);
RPR_SetExtState("tempo",'10-',"Tk^" ,1);
RPR_SetExtState("tempo",'-',40126 ,1);
RPR_SetExtState("tempo",'10+',"Tkv" ,1);
RPR_SetExtState("tempo",'+',40125 ,1);


