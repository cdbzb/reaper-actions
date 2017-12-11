from cdp_helpers import cdp_prog_dir
from cdp_helpers import process_cdp_time_domain
from reaper_python import *

info={"title":"CDP Distort Fractal","mainprog":"distort","subprog":"fractal","chgdur":True,"onlymono":True,
	  "paramnames":["Scaling","Loudness"],
	  "paramdefaults":["10","0.5"]}
process_cdp_time_domain(info)