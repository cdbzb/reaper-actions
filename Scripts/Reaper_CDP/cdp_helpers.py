from reaper_python import *
from subprocess import call
import uuid
import os
import time
import json
import subprocess

cdp_prog_dir="/Applications/cdpr7/_cdp/_cdprogs/"

def key_exists_and_true(dict,key):
	if key in dict and dict[key]==True:
		return True
	return False

def remove_file_if_exists(fn):
	if os.path.isfile(fn):
		os.remove(fn)

def filename_of_selected_item():
	item=RPR_GetSelectedMediaItem(0, 0)
	take=RPR_GetActiveTake(item)
	source=RPR_GetMediaItemTake_Source(take)
	return RPR_GetMediaSourceFileName(source, "", 1024)[1]

def num_chans_of_selected_item():
	item=RPR_GetSelectedMediaItem(0, 0)
	take=RPR_GetActiveTake(item)
	source=RPR_GetMediaItemTake_Source(take)
	return RPR_GetMediaSourceNumChannels(source)

def file_time_interval_of_selected_item():
	item=RPR_GetSelectedMediaItem(0, 0)
	take=RPR_GetActiveTake(item)
	soffs=RPR_GetMediaItemTakeInfo_Value(take, "D_STARTOFFS")
	itemlength=RPR_GetMediaItemInfo_Value(item, "D_LENGTH")
	return [soffs,soffs+itemlength]
	
def run_pvoc_analysis(inpcmfn,wsize,olap):
	projpath=RPR_GetProjectPath("", 2048)[0]
	sizehash=os.path.getsize(inpcmfn) % 9973
	analfn=projpath+"/"+os.path.basename(inpcmfn)+"-"+str(wsize)+"-"+str(olap)+"-"+str(sizehash)+".ana"
	if not os.path.isfile(analfn):
		call([cdp_prog_dir+"pvoc", "anal","1",inpcmfn,analfn,"-c"+wsize,"-o"+olap])
		if os.path.isfile(analfn):
			return analfn
		else:
			return ""
	else:
		return analfn
	return ""

def default_spectral_paramsformatfunc(info,split_input,pvocfn,analfn1):
	if "mode" in info:
		prog_params=[cdp_prog_dir+"/"+info["mainprog"], info["subprog"],info["mode"],pvocfn,analfn1]
	else:
		prog_params=[cdp_prog_dir+"/"+info["mainprog"], info["subprog"],pvocfn,analfn1]
	for i in range(0,len(split_input)-2):
		progarg=""
		if "paramprefixes" in info:
			progarg=progarg+info["paramprefixes"][i]
		progarg=progarg+split_input[i+2]
		prog_params.append(progarg)
	#RPR_ShowConsoleMsg(prog_params)
	return prog_params
	
def default_paramsformatfunc(info,split_input,infn,outfn):
	if "mode" in info:
		prog_params=[cdp_prog_dir+"/"+info["mainprog"], info["subprog"],info["mode"],infn,outfn]
	else:
		prog_params=[cdp_prog_dir+"/"+info["mainprog"], info["subprog"],infn,outfn]
	for i in range(0,len(split_input)):
		progarg=""
		if "paramprefixes" in info:
			progarg=progarg+info["paramprefixes"][i]
		progarg=progarg+split_input[i]
		prog_params.append(progarg)
	#RPR_ShowConsoleMsg(prog_params)
	return prog_params
	
def check_cdp_binaries():
	if not cdp_prog_dir:
		RPR_ShowMessageBox("CDP binaries directory not set", "CDP error", 0)
		return False
	return True

def make_settings_key(info):
	key=info["mainprog"]+"/"+info["subprog"]
	if "mode" in info:
		key=key+"/"+info["mode"]
	return key

def cut_sound_file(fn,time_interval):
	projpath=RPR_GetProjectPath("", 2048)[0]
	tinthash=hash((time_interval[0],time_interval[1])) % 9973
	outfn=projpath+"/"+os.path.basename(fn)+str(tinthash)+"-cut.wav"
	call([cdp_prog_dir+"sfedit", "cut","1",fn,outfn,str(time_interval[0]),str(time_interval[1]),"-w2.0"])
	if os.path.isfile(outfn):
		return outfn
	return ""
	
def save_settings(userinputs,info,data):
	jsonfn=RPR_GetResourcePath()+"/xenakios_cdp.json"
	key=make_settings_key(info)
	settingsdict={"settings":userinputs}
	data[key]=settingsdict
	json.dump(data, open( jsonfn,"w"),indent=4)

def load_settings(info):
	jsonfn=RPR_GetResourcePath()+"/xenakios_cdp.json"
	data={}
	didload=False
	try: 
		data = json.load( open(jsonfn, "r" ) )
	except:
		pass
	if data:
		settingskey=make_settings_key(info)
		if settingskey in data:
			info["paramdefaults"]=data[settingskey]["settings"]
			didload=True
	return [data,info,didload]
	
def process_cdp_spectral_impl(info, paramsformatfunc=default_spectral_paramsformatfunc):
	if check_cdp_binaries()==False:
		return "cancel"
	if num_chans_of_selected_item()!=1:
		RPR_ShowMessageBox("Only mono input files supported for now", "CDP error", 0)
		return "cancel"
	inputs_csv="FFT window size,Overlap factor"
	defaults_csv="1024,3"
	(data,info,didload)=load_settings(info)
	if didload==True:
		defaults_csv=""
	for parelem in info["paramnames"]:
		inputs_csv=inputs_csv+","+parelem
	for parelem in info["paramdefaults"]:
		if defaults_csv:
			defaults_csv=defaults_csv+","
		defaults_csv=defaults_csv+parelem
	user_in=RPR_GetUserInputs(info["title"], 2+len(info["paramnames"]), inputs_csv, defaults_csv, 200)
	if user_in[0]==True:
		time0=time.time()
		split_input=user_in[4].split(',')
		win_size=split_input[0]
		overlapfact=split_input[1]
		filename=filename_of_selected_item()
		if filename!="":
			time_interval=file_time_interval_of_selected_item()
			cut_file_name=cut_sound_file(filename,time_interval)
			if cut_file_name!="":
				pvocfn=run_pvoc_analysis(cut_file_name,win_size,overlapfact)
				remove_file_if_exists(cut_file_name)
				if pvocfn!="":
					projpath=RPR_GetProjectPath("", 1024)[0]
					procanalfn1=projpath+"/"+str(uuid.uuid4())+".ana"
					remove_file_if_exists(procanalfn1)
					prog_params=paramsformatfunc(info,split_input,pvocfn,procanalfn1)
					cmd=subprocess.Popen(prog_params,stdout=subprocess.PIPE,universal_newlines=True)
					cmd_out, cmd_err=cmd.communicate()
					if cmd.returncode==0:
						outfn=projpath+"/"+os.path.basename(filename)+"-"+str(int(time.time()))+".wav"
						call([cdp_prog_dir+"/pvoc", "synth",procanalfn1,outfn])
						if os.path.isfile(outfn):
							RPR_InsertMedia(outfn, 3)
							save_settings(split_input,info,data)
							if ("chgdur" in info) and (info["chgdur"]==True):
								# adjust item length to added take's length
								RPR_Main_OnCommand(40612, 0)
							return "ok"
						else:
							RPR_ShowMessageBox("Error when running resynthesis program\n", "CDP error", 0)
						time1=time.time()
						#RPR_ShowConsoleMsg("processing took "+str(time1-time0)+" seconds\n")
					else:
						answer=RPR_ShowMessageBox("Error when running process program\n"+str(cmd_out)+"\nTry again with different settings?", "CDP error", 4)
						if answer==6:
							return "retry"
						return "cancel"
					remove_file_if_exists(procanalfn1)
				else:
					RPR_ShowMessageBox("Could not create PVOC analysis file", "CDP error", 0)
			else:
				RPR_ShowMessageBox("Could not cut sound file", "CDP error", 0)
		else:
			RPR_ShowMessageBox("Could not get input file name", "CDP error", 0)
	return "cancel"

def process_cdp_spectral(info, paramsformatfunc=default_spectral_paramsformatfunc):
	result="retry"
	while result=="retry":
		result=process_cdp_spectral_impl(info,paramsformatfunc)
			
def process_cdp_time_domain_impl(info, paramsformatfunc):
	if check_cdp_binaries()==False:
		return "cancel"
	numchans=num_chans_of_selected_item()
	if "onlymono" in info and numchans!=1:
		RPR_ShowMessageBox("Only mono input files supported for now", "CDP error", 0)
		return "cancel"
	inputs_csv=""
	defaults_csv=""
	(data,info,didload)=load_settings(info)
	for parelem in info["paramnames"]:
		if inputs_csv:
			inputs_csv=inputs_csv+","
		inputs_csv=inputs_csv+parelem
	for parelem in info["paramdefaults"]:
		if defaults_csv:
			defaults_csv=defaults_csv+","
		defaults_csv=defaults_csv+parelem
	user_in=RPR_GetUserInputs(info["title"], len(info["paramnames"]), inputs_csv, defaults_csv, 100)
	if user_in[0]==True:
		split_input=user_in[4].split(',')
		filename=filename_of_selected_item()
		if filename!="":
			projpath=RPR_GetProjectPath("", 1024)[0]
			time_interval=file_time_interval_of_selected_item()
			cut_file_name=cut_sound_file(filename,time_interval)
			if cut_file_name!="":
				outfn=projpath+"/"+os.path.basename(filename)+"-"+str(int(time.time()))+".wav"
				prog_params=paramsformatfunc(info,split_input,cut_file_name,outfn)
				cmd=subprocess.Popen(prog_params,stdout=subprocess.PIPE,universal_newlines=True)
				cmd_out, cmd_err=cmd.communicate()
				if cmd.returncode==0:
					if os.path.isfile(outfn):
						RPR_InsertMedia(outfn, 3)
						save_settings(split_input,info,data)
						if key_exists_and_true(info,"chgdur"):
							# adjust item length to added take's length
							RPR_Main_OnCommand(40612, 0)
						return "ok"
				else:
					answer=RPR_ShowMessageBox("Error when running process program\n"+str(cmd_out)+"\nTry again with different settings?", "CDP error", 4)
					if answer==6:
						return "retry"
					return "cancel"
				remove_file_if_exists(cut_file_name)
			else:
				RPR_ShowMessageBox("Could not cut sound file\n", "CDP error", 0)
		else:
			RPR_ShowMessageBox("Could not get input file name", "CDP error", 0)
	return "cancel"

def process_cdp_time_domain(info, paramsformatfunc=default_paramsformatfunc):
	result="retry"
	while result=="retry":
		result=process_cdp_time_domain_impl(info,paramsformatfunc)
