import subprocess
from subprocess import Popen, PIPE
import os

cmd = bytes("""
on run
	set x to "Again"
	tell application "QuickTime Player"
		activate
		repeat while x = "Again"
			tell (new movie recording)
				start
				set returnedItems to display dialog "Good?" buttons {"Good", "Again"} default button "Again"
				set x to the button returned of returnedItems
				if x = "Again" then tell application "QuickTime Player"
					close front window
				end tell
				if x = "Good" then stop
				if x = "Good" then tell application "QuickTime Player"
					set myFile to front window's name 
				end tell
			end tell
		end repeat
	end tell
	return myFile
end run
""",'utf-8')


#cmd = """osascript ~/scripts/Quicktime\ Loop\ .scpt"""
# mode: 0=add to current track, 1=add new track, 3=add to selected items as takes, &4=stretch/loop to fit time sel, &8=try to match tempo 1x, &16=try to match tempo 0.5x, &32=try to match tempo 2x

def run_this_scpt(scpt):
     p = Popen(['osascript', '-'] , stdin=PIPE, stdout=PIPE, stderr=PIPE)
     stdout, stderr = p.communicate(scpt)
     return stdout;

directory = "/Volumes/Home/Users/michael/Movies/"
#target = os.path.join(directory, file[4:12] + '-13-Misc.jpg'
#        os.rename(path, target)
myFile = run_this_scpt(cmd)
nums = int(str(myFile,'utf-8').split(' ')[-1].split('.')[0])

RPR_InsertMedia(directory + "Movie Recording " + str(nums) + ".mov", 0);
os.system("""open -a "REAPER.app" """ )
