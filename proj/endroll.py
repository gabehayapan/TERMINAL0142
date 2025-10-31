import time
import os
import sys

def clear_screen():
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')

def endroll_animation():
    frames = [
	"""\

	4 4                      2 2 2 2 2 2 2                            kk                                                                                               
	4 4                   2 2             2 2         tt              kk                                                                                           
	4 4                   2 2             2 2       t tt t      o o   kk   k   yy   y     o o                                                                        
	4 4      4 4                          2 2         tt      oo   o  kk k     yy   y   oo   o                                                                             
	4 4      4 4                          2 2         tt   t  oo   o  kk k     yy   y   oo   o                                                                       
	4 4      4 4                          2 2         tt t      o o   kk   k   yy y y     o o                                                                             
	4 4 4 4 4 4 4 4 4 4      2 2 2 2 2 2 2                                          y                        
	4 4 4 4 4 4 4 4 4 4      2 2 2 2 2 2 2                                     yy y y                     
	         4 4          2 2                                                                          
	         4 4          2 2                                                                   
	         4 4          2 2                                                                             
	         4 4          2 2                                                                                
	         4 4             2 2 2 2 2 2 2 2                                                                              

	""",
	"""\

	hh                                   kk                                                               
	hh                                   kk                                                                  
	hh        a a a   nn n n     a a a   kk   k    a a a   mm m mm m                                          
	hh h h  aa   a    nn    n  aa   a    kk k    aa   a    mm   m   m                                                 
	hh   h  aa   a    nn    n  aa   a    kk k    aa   a    mm   m   m                                            
	hh   h     a a a  nn    n     a a a  kk   k     a a a  mm   m   m                                             

	kk                                                         kk      
	kk              ii    tt                tt                 kk                     
	kk   k    e e       t tt t      o o   t tt t      a a a    kk   k           
	kk k    ee e e  ii    tt      oo   o    tt      aa   a     kk k                       
	kk k    ee      ii    tt   t  oo   o    tt   t  aa   a     kk k                          
	kk   k    e e   ii    tt t      o o     tt t       a a a   kk   k                         

	"""

    ]

    print("\n")
    for frame in frames:
        clear_screen()
        sys.stdout.write("\r" + frame)  # Overwrite the current line
        sys.stdout.flush()  # Force the output to update immediately
        time.sleep(2)  # Time interval between frames
    clear_screen()

    print("\n")



