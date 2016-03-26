Calclate SecurityClearance color RGB data
=============
_This software is released under the MIT License, see LICENSE.txt._  

# Description  
This program is Python script to calculate SecurityClearance color RGB value (following Paranoia TRPG).  

User can set MIN, MAX and input value.  
This script calculate security clearance color of input value.  
If the input value is MIN and under, this security clearance is Infrared.  
If the input value is MAX and over, this security clearance is Ultraviolet.  
If the input value is over MIN and under MAX, this script can calculate the security clearance color.  

# Usage  
	import CalcSC  
  
	MIN = 0  
	MAX = 40  
	secc = CalcSC.CalcSC(False, MIN, MAX)  
	input = 18.9  
	secc.setVal(input)  
	[r, g, b] = secc.return_rgb()  
	[rp, gp, bp] = secc.return_rgbrate()  
	print ([r,g,b])  
	print ([rp,gp,bp]) # calculate each 0-255 value to 0-100 to use RaspberryPi PWM  

