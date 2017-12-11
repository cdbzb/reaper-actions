from cdp_helpers import cdp_prog_dir
from cdp_helpers import process_cdp_spectral
from reaper_python import *

info={"title":"CDP Stretch Time","mainprog":"stretch","subprog":"time","mode":"1","chgdur":True,
	  "paramnames":["Time factor"],
	  "paramdefaults":["2.0"]}
process_cdp_spectral(info)