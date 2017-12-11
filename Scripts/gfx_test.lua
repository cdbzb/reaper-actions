last_mouse_cap = 0;

function onframe()

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
  last_mouse_cap = gfx.mouse_cap
  
  local c=gfx.getchar();
  local t=reaper.time_precise();
  local zsc = 0.01*math.cos(t*0.73);
  
  if c >= 0 and c ~= 27 then
    reaper.defer(onframe);
    if c == 32 then
      mode = mode + 1
      if mode >= 2 then mode = 0 end
    end
  end
  
  gfx.mode = 256; -- filtering on

  gfx.blit(-1,0,0.1*(math.sin(t*0.3)^2),
     gfx.w*zsc,gfx.h*zsc, 
     gfx.w*(1-2*zsc),gfx.h*(1-2*zsc), 0,0,gfx.w,gfx.h);
           
  gfx.transformblit(-1,0,0,gfx.w,gfx.h,
    3,3,
    { -- table of 9 pairs of values (x,y source coordinates)
      0,0, gfx.w/2,0,  gfx.w, 0, 
      0,gfx.h/2, gfx.w/2,gfx.h/2*0.9, gfx.w, gfx.h/2, 
      0,gfx.h, gfx.w/2,gfx.h*1.1, gfx.w*0.93, gfx.h,   
    }
  );
  
  gfx.set((math.cos(t)+1.0)*0.5,
          (math.cos(t*1.74)+1.0)*0.5,
          (math.cos(t*1.2+0.56)+1.0)*0.5,
          0.25,
          1); -- additive
          
  local sz=math.floor(gfx.w*0.03);
  for x=1,10 do
    if mode == 1 then
     gfx.circle(math.random(sz//2,gfx.w-sz//2),math.random(sz//2,gfx.h-sz//2),sz,1)
    elseif mode == 0 then
     gfx.rect(math.random(0,gfx.w-sz),math.random(0,gfx.h-sz),sz,sz);
    end
  end
  
  gfx.update();
end

dockstate = reaper.GetExtState("gfx_test","dock");
if dockstate == nil or dockstate == "" then dockstate = 1 end

gfx.init("gfx_test.lua",640,480,dockstate)

reaper.atexit(function() 
     reaper.SetExtState("gfx_test","dock",gfx.dock(-1),true)
     gfx.quit() 
    end)
    
    
gfx.clear=-1;
mode = 1;

reaper.atexit(gfx.quit)

onframe();

