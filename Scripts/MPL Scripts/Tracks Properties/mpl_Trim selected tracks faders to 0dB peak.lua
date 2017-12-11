--[[
   * ReaScript Name: Trim selected tracks faders to 0dB peak
   * Lua script for Cockos REAPER
   * Author: Michael Pilyavskiy (mpl)
   * Author URI: http://forum.cockos.com/member.php?u=70694
   * Licence: GPL v3
   * Version: 1.0
  ]]
  
  script_title = "Trim selected tracks faders to 0dB peak"
  reaper.Undo_BeginBlock()
  
  counttracks = reaper.CountSelectedTracks(0)
  if counttracks ~= nil then
    for i=1, counttracks  do
      track = reaper.GetSelectedTrack(0,i-1)
      if track ~= nil then
        peak = reaper.Track_GetPeakInfo(track, 1)
        if peak > 1 then
          vol = reaper.GetMediaTrackInfo_Value(track, 'D_VOL')
          reaper.SetMediaTrackInfo_Value(track, 'D_VOL',vol-(peak-1))
        end
      end
    end
    reaper.UpdateArrange()
  end
  
  reaper.Undo_EndBlock(script_title,0)
