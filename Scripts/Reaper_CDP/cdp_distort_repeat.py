from cdp_helpers import cdp_prog_dir
from cdp_helpers import process_cdp_time_domain
from reaper_python import *

info={"title":"CDP Distort Repeat","mainprog":"distort","subprog":"repeat","chgdur":True,"onlymono":True,
	  "paramnames":["Multiplier","Cycle count","Skip cycles"],
	  "paramdefaults":["2","1","0"],
	  "paramprefixes":["","-c","-s"]}
process_cdp_time_domain(info)