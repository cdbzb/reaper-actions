{\rtf1\ansi\ansicpg1252\cocoartf1038\cocoasubrtf250
{\fonttbl\f0\fmodern\fcharset0 Courier;}
{\colortbl;\red255\green255\blue255;\red205\green216\blue215;}
\margl1440\margr1440\vieww9000\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\ql\qnatural

\f0\fs26 \cf0 \cb2 #  \
# SetTrackHeight.pl  \
#  \
 \
use strict;  \
use warnings;  \
 \
use constant CURR_PROJ => 0;  \
use constant FIRST_SEL => 0;  \
use constant PNAME => 'I_HEIGHTOVERRIDE';  \
use constant NEWHEIGHT => 52; \
\
my $tr;  \
my $result; \
my $Track_Count;\
my $Track_Index;\
\
\
# Get number of tracks currently selected\
$Track_Count = RPR_CountSelectedTracks(0);\
$Track_Index = 0;\
\
# Update Height for each selected Track\
while ($Track_Index < $Track_Count) \{\
        $tr = RPR_GetSelectedTrack(CURR_PROJ, $Track_Index);  \
        $result = RPR_SetMediaTrackInfo_Value($tr, PNAME, NEWHEIGHT);\
\
	$Track_Index++;\
\}\
\
RPR_TrackList_AdjustWindows(CURR_PROJ);  \
RPR_UpdateTimeline();}