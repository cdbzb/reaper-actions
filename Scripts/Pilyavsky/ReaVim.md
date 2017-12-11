ideas to make Vim-like console for REAPER:

first pillage cool stuff from this script:

/Users/michael/Library/Application Support/REAPER/Scripts/Pilyavsky/Other/mpl_get_action_info.lua

for example this:

retval, command_ID = reaper.GetUserInputs("Get Action info", 1, "Command ID", "")
--retval = true
--command_ID = "_XENAKIOS_SISFTNEXTRPPIF"
path = reaper.GetExePath()
kb_shortcuts_t = Get_table_from_file(path.."\\".."reaper-kb.ini")

reaper.ShowConsoleMsg("")
if string.sub(command_ID, 0,1) ~= "_" then is_main_action = true end
if string.sub(command_ID, 0,1) == "_" then is_main_action = false end 
