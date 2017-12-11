from cdp_helpers import process_cdp_spectral
from reaper_python import *

info={"title":"CDP Repitch Transpose", "mainprog":"repitch","subprog":"transpose","mode":"3",
	  "paramnames":["Semitones"],"paramdefaults":["-12.0"]}
process_cdp_spectral(info)
