from cdp_helpers import cdp_prog_dir
from cdp_helpers import process_cdp_time_domain
from reaper_python import *

info={"title":"CDP Envelope Warp Exaggerate","mainprog":"envel","subprog":"warp","mode":"3",
	  "paramnames":["Window size","Param"],"paramdefaults":["40","0.5"]}
process_cdp_time_domain(info)