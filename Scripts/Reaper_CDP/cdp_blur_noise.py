from cdp_helpers import process_cdp_spectral
from reaper_python import *

info={"title":"CDP Blur Noise", "mainprog":"blur","subprog":"noise",
	  "paramnames":["Noise amount (0.0-1.0)"],"paramdefaults":["0.20"]}
process_cdp_spectral(info)
