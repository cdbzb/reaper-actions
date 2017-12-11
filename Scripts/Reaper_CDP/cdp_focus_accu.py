from cdp_helpers import cdp_prog_dir
from cdp_helpers import process_cdp_spectral
from reaper_python import *

info={"title":"CDP Focus Accu","mainprog":"focus","subprog":"accu",
	  "paramnames":["Decay","Gliss"],
	  "paramdefaults":["0.75","-0.9"],
	  "paramprefixes":["-d","-g"]}
process_cdp_spectral(info)