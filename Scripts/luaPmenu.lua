local myscript = 'tell application \"Terminal\" do script \"ActionWindow\"'
file = assert (io.popen('osascript ~/scripts/ActionWindow.scpt'))
local output = file:read('*all')
file:close()
reaper.Main_OnCommand(action)
