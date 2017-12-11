

keys = {'7','8','9','-','4','5','6','+','1','2','3','0'}

points,tempo,nudge = {},{},{}

points.name='points' tempo.name='tempo' nudge.name='nudge'

--menus = {}

points[7]={"_SWS_BRMOVEEDITTOPREVENV","<-|"}
points[8]={41180,"^"} -- nudge points up
points[9]={'_SWS_BRMOVEEDITTONEXTENV',"|->"}
points[4]={'_BR_ENV_SEL_PREV_POINT',".<-"}
points[5]={40330 ," |..| "}
points[6]={'_BR_ENV_SEL_NEXT_POINT',"->."}
points[1]={'nop' ," "}
points[2]={41181,"v"} -- nudge points down
points[3]={'nop' ," "}
points["-"]={41863 ,"^En"} -- prev env
points["+"]={41864 ,"vEn"} -- next env

menus[1] = {points}--,tempo,nudge}

for i,menu in pairs(menus) do
  for j = 1 , #keys do
    reaper.SetExtState(menu.name,keys[j],menu[j][1],1)
    print (menu,keys[j],menu[j][1])
    reaper.SetExtState(menu.name,keys[j].."Glyph",menu[j][2],1)
  end
end

    







