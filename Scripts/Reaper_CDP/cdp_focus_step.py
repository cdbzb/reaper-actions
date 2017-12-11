from cdp_helpers import cdp_prog_dir
from cdp_helpers import process_cdp_spectral
from reaper_python import *

info={"title":"CDP Focus Step","mainprog":"focus","subprog":"step",
	  "paramnames":["Step duration"],
	  "paramdefaults":["0.125"]}
process_cdp_spectral(info)