#-------------------------------------------------------------------
# get_user_input_example.py
#-------------------------------------------------------------------
# define msg alias (custom)
def msg(m):
    RPR_ShowConsoleMsg(m+'\n')    
maxreturnlen = 10;
nitems = 1
# call dialog and get result
res = RPR_GetUserInputs('recording monitoring setup',1,'input',0,maxreturnlen);
# we get a tuple
msg('type is: '+type(res).__name__);
# check if res[0] is true ('ok' pressed)
if res[0]:
    # the fourth item holds the input values
    # resvalues = res[4].split(',');

    resvalues = res[4];
    # get length of the new array and output all items
    msg('resvalues['+str(0)+'] = '+resvalues);

#-------------------------------------------------------------------
