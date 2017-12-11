from cdp_helpers import process_cdp_spectral
from reaper_python import *

info={"title":"CDP Blur Blur", "mainprog":"blur","subprog":"blur",
	  "paramnames":["Amount (1.0-1000.0)"],"paramdefaults":["50.0"]}
process_cdp_spectral(info)
