
n mainloop()
  gfx.x = 10
    gfx.y = 10
      
      gfx.printf("Press 'd' to open the dialog")
        gfxchar=gfx.getchar()

	  gfx.update()
	    
	    if gfxchar == 100 then -- ascii code for 'd' key is 100
		        retval, retvals = reaper.GetUserInputs("title", 2, "This is input1,input2", "default_val1,default_val2")
			    reaper.ShowConsoleMsg("")
			        reaper.ShowConsoleMsg(retvals)
				  end
				    
				    if gfxchar >= 0 then 
					        reaper.defer(mainloop)
						  end
						    
					  end 

					  gfx.init("",300,50)

					  mainloop()
