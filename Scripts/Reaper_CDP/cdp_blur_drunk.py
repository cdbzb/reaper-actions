from cdp_helpers import process_cdp_spectral
from reaper_python import *

info={"title":"CDP Blur Drunk","mainprog":"blur","subprog":"drunk","chgdur":True,
	  "paramnames":["Range","Start Time","Duration"],"paramdefaults":["8","0.0","5.0"]}
process_cdp_spectral(info)