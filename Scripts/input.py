#-------------------------------------------------------------------
# get_user_input_example.py
#-------------------------------------------------------------------
# define msg alias (custom)
def msg(m):
    RPR_ShowConsoleMsg(m+'\n')    
names = 'monitor but dont record,play media while recording,in2';
dvalues = '20,21,22';
maxreturnlen = 10;
nitems = len(dvalues.split(','));
# call dialog and get result
res = RPR_GetUserInputs('recording monitoring setup',nitems,names,dvalues,maxreturnlen);
# we get a tuple
msg('type is: '+type(res).__name__);
# check if res[0] is true ('ok' pressed)
if res[0]:
    # the fourth item holds the input values
    resvalues = res[4].split(',');
    # get length of the new array and output all items
    rvlen = len(resvalues);
    i=0;
    while i<rvlen:
        msg('resvalues['+str(i)+'] = '+resvalues[i]);
        i+=1;
#-------------------------------------------------------------------