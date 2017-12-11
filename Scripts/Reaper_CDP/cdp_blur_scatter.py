from cdp_helpers import process_cdp_spectral
from reaper_python import *

info={"title":"CDP Blur Scatter", "mainprog":"blur","subprog":"scatter",
	  "paramnames":["Keep"],"paramdefaults":["64"]}
process_cdp_spectral(info)
