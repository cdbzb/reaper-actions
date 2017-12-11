from cdp_helpers import cdp_prog_dir
from cdp_helpers import process_cdp_time_domain
from reaper_python import *

info={"title":"CDP Modify Radical Shred","mainprog":"modify","subprog":"radical","mode":"2",
	  "paramnames":["Repeats","Chunklen"],"paramdefaults":["1","0.5"]}
process_cdp_time_domain(info)