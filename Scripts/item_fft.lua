last_take = nil
last_accessor = nil
last_offs = -1e20
last_mouse_cap = 0
fft_size = 2048

function make_window(sz, mode) 
  local isz = 0.5/sz
  local dwindowpos = 3.14159*2/(sz-1)
  local windowpos=0
  local ret = reaper.new_array(sz)
  for i=1,sz do
    if mode == 1 then ret[i] = (0.53836 - math.cos(windowpos)*0.46164)*isz
    elseif mode == 2 then ret[i] = (0.35875 - 0.48829 * math.cos(windowpos) + 0.14128 * math.cos(2*windowpos) - 0.01168 * math.cos(6*windowpos)*isz)
    elseif mode == 3 then ret[i] = (0.42 - 0.50 * math.cos(windowpos) + 0.08 * math.cos(2.0*windowpos))*isz
    else 
      ret[i] = 1.0 * isz
    end
    windowpos=windowpos + dwindowpos
  end
  return ret
end

buffer = reaper.new_array(fft_size*2)
buffer_l = reaper.new_array(fft_size*2)
buffer_r = reaper.new_array(fft_size*2)
window = make_window(fft_size,2)
buffer_l.resize(0)
buffer_r.resize(0)

function item_iter(proj) -- iterates all items in project
  local iidx, tidx, th = -1, 0, reaper.GetTrack(proj,0)
  return function()
    while true do
      iidx = iidx + 1
      local ih = reaper.GetTrackMediaItem(th,iidx)
      if ih then return ih end      
      tidx = tidx + 1
      th = reaper.GetTrack(proj,tidx)
      if not th then return end
      iidx=-1
    end
  end
end  

function get_selected_take(fortime)
  for ih in item_iter() do
    if reaper.IsMediaItemSelected(ih) then
      local pos = reaper.GetMediaItemInfo_Value(ih,"D_POSITION")
      local len = reaper.GetMediaItemInfo_Value(ih,"D_LENGTH")
      if fortime >= pos and fortime < pos+len then
        local tk = reaper.GetActiveTake(ih)
        if tk then return tk, pos end
      end
    end
  end
end

function run()
  if gfx.mouse_cap == 0 and last_mouse_cap == 2 then
    local str = "Dock|Exit";
    if (gfx.dock(-1)&1) == 1 then
      str = "!" .. str
    end
    gfx.x=gfx.mouse_x
    gfx.y=gfx.mouse_y
    local cmd = gfx.showmenu(str)
    if cmd == 1 then
      gfx.dock(gfx.dock(-1)~1)
    elseif cmd == 2 then
      return -- avoid defer below
    end
  end
  if gfx.getchar() >= 0 then
    reaper.defer(run)
  end
  last_mouse_cap = gfx.mouse_cap
  gfx.set(1)
  gfx.x=0
  gfx.y=0
  if (reaper.GetPlayState()&1)==1 then 
    offs = reaper.GetPlayPosition()
  else
    offs = reaper.GetCursorPosition()
  end 
    
  local tk,itempos = get_selected_take(offs)
  if tk ~= last_take then
    if last_accessor then 
      reaper.DestroyAudioAccessor(last_accessor)
    end
    if tk then
      last_accessor = reaper.CreateTakeAudioAccessor(tk)
    else
      last_accessor = nil
    end
    last_offs = -1e20
    last_take = tk 
    buffer_l.resize(0)
    buffer_r.resize(0)
  end

  if tk then
    offs = offs - itempos
    if offs ~= last_offs then
      if last_accessor and
          reaper.GetAudioAccessorSamples(last_accessor,44100,2,offs,fft_size,buffer) > 0
      then
        buffer_l.resize(fft_size*2)
        buffer_r.resize(fft_size*2)
        local wi=1
        for i=1,fft_size*2,2 do
          buffer_l[i] = buffer[i] * window[wi]
          buffer_r[i] = buffer[i+1] * window[wi]
          buffer_l[i+1]=0
          buffer_r[i+1]=0
          wi=wi+1
        end
        
        buffer_l.fft(fft_size,true)
        buffer_r.fft(fft_size,true)
      else
        buffer_l.resize(0)
        buffer_r.resize(0)
      end
    end
  end
  --gfx.printf("buffer_valid = %d, last accessor = %f\n",#buffer_l, last_accessor)
  gfx.setpixel(0,0,0) -- force update (hack) 
  gfx.set(1,1,0)
  local b = buffer_l
  local yoffs = gfx.h / 4;
  local gsc = (gfx.h-yoffs)*20/(96*math.log(10))
  
  for chan=1,2 do
    gfx.x=0
    local xsc=gfx.w / (#b/2-2)
    for i=1,#b/2-2,2 do
      local nx = i * xsc
      local re,im = b[i], b[i+1]
      local ny = math.max(re*re+im*im, 1e-20)
      ny = -math.log(ny)*0.5 * gsc + yoffs
      if i > 1 then
        gfx.lineto(nx,ny)
      else
        gfx.y=ny
      end
    end
    
    -- right channel
    b = buffer_r
    gfx.set(0,1,1,1,1) -- additive blue
  end
  gfx.update()
end


dockstate = reaper.GetExtState("item_fft","dock");
if dockstate == nil or dockstate == "" then dockstate = 1 end

gfx.init("item_fft.lua",640,480,dockstate)

reaper.atexit(function() 
     reaper.SetExtState("item_fft","dock",gfx.dock(-1),true)
     gfx.quit() 
    end)

run()
