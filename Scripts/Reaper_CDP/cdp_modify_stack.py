from cdp_helpers import cdp_prog_dir
from cdp_helpers import process_cdp_time_domain
from reaper_python import *

info={"title":"CDP Modify Stack","mainprog":"modify","subprog":"stack","chgdur":True,
	  "paramnames":["Transpose","Count","Lean","Attack offset","Gain","Duration"],
	  "paramdefaults":["12.0","3","1.0","0.0","1.0","0.5"]}
process_cdp_time_domain(info)