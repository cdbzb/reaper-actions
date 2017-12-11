from cdp_helpers import cdp_prog_dir
from cdp_helpers import process_cdp_time_domain
from reaper_python import *

info={"title":"CDP Distort Pitch","mainprog":"distort","subprog":"pitch","chgdur":True,"onlymono":True,
	  "paramnames":["Amount","Cycle count","Skip cycles"],
	  "paramdefaults":["0.1","1","0"],
	  "paramprefixes":["","-c","-s"]}
process_cdp_time_domain(info)