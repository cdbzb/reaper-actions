from cdp_helpers import process_cdp_spectral
from reaper_python import *

info={"title":"CDP Blur Average","mainprog":"blur","subprog":"avrg",
	  "paramnames":["Bands (odd <= 1/2 analysis)"],"paramdefaults":["511"]}
process_cdp_spectral(info)
