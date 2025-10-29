import time
import os
import sys

def clear_screen():
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')

def opening_animation():
    # Frames of the animation (each frame will overwrite the previous one)
    frames = [
	"""\





	  __________________________________
	 /EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE\\
	/\E                                E/\\
	  \E                              E/
	   \E                            E/
	    \E                          E/
	     \E                        E/
	      \E                      E/
	       \E                    E/
		\EEEEEEEEEEEEEEEEEEEE/



	""",  # Empty cup (initial state)

	"""\
		  __
		  EI\\
		   EI\\
		    EI\\
		     EI\\
		      EQ\\
		       VMmmmmmmmmmmmmmmmmmmm\\
	/\E77777777777777777777777777777777E/\\
	  \E                              E/
	   \E                            E/
	    \E                          E/
	     \E                        E/
	      \E                      E/
	       \E                    E/
		\EEEEEEEEEEEEEEEEEEEE/



	""",  # First pour (water level 1)

        """\
     88HO         __
      ''H         EI\\
	+OO        EI\\
	  H         EI\\
	             EI\\
	              EQ\\
	               VMmmmmmmmmmmmmmmmmmmm\\
	/\E77777777777777777777777777777777E/\\
	  \E                              E/
	   \E                            E/
	    \E                          E/
	     \E                        E/
	      \E                      E/
	       \E                    E/
		\EEEEEEEEEEEEEEEEEEEE/



        """,  # Second pour (water level 2)
	"""\
     88HO         __
      ''H         EI\\
	+OO        EI\\
	  HO'       EI\\
	  ;HO'       EI\\
	   'HO        EQ\\
	   ;OHH        VMmmmmmmmmmmmmmmmmmmm\\
	/\E77777777777777777777777777777777E/\\
	  \E                              E/
	   \E                            E/
	    \E                          E/
	     \E                        E/
	      \E                      E/
	       \E                    E/
		\EEEEEEEEEEEEEEEEEEEE/



	""",

        """\
		  __
		  EI\\
		   EI\\
		    EI\\
		     EI\\
		      EQ\\
		       VMmmmmmmmmmmmmmmmmmmm\\
	/\E77777777777777777777777777777777E/\\
	  \E                              E/
	   \E                            E/
	    \E                          E/
	     \E                        E/
	      \E                      E/
	       \E                    E/
		\EEEEEEEEEEEEEEEEEEEE/



        """,  # Third pour (water level 3)

        """\





	   __________________________________
	 /EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE\\
	/\E                                E/\\
	  \E                              E/
	   \E                            E/
	    \E                          E/
	     \E                        E/
	      \E                      E/
	       \E                    E/
		\EEEEEEEEEEEEEEEEEEEE/



         """,  # Fourth pour (water level 4)

        """\



     GGGGGGGG      A       M     M  EEEEEEE    SSSSSSS  TTTTTTT      A       RRRRRR   TTTTTTT
    G             A A      MM   MM  E         S            T        A A      R     R     T
    G            A   A     M M M M  E         S            T       A   A     R     R     T
    G    GGG    A     A    M  M  M  EEEEEE     SSSSSS      T      A     A    RRRRRR      T
    G      G    AAAAAAA    M     M  E                S     T      AAAAAAA    R    R      T
    G      G   A       A   M     M  E                S     T     A       A   R     R     T
     GGGGGGG  A         A  M     M  EEEEEEE   SSSSSSS      T    A         A  R     R     T



        """  # Lid closing after full cup
    ]

    # Display each frame with a delay to simulate the pouring animation
    print("\n")
    for frame in frames:
        clear_screen()
        sys.stdout.write("\r" + frame)  # Overwrite the current line
        sys.stdout.flush()  # Force the output to update immediately
        time.sleep(0.5)  # Time interval between frames

    print("\n")

def ending_animation():
    frames = [
	"""\





	  __________________________________
	 /EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE\\
	/\E                                E/\\
	  \E                              E/
	   \E                            E/
	    \E                          E/
	     \E                        E/
	      \E                      E/
	       \E                    E/
		\EEEEEEEEEEEEEEEEEEEE/



	""",
	"""\
		  __
		  EI\\
		   EI\\
		    EI\\
		     EI\\
		      EQ\\
		       VMmmmmmmmmmmmmmmmmmmm\\
	/\E77777777777777777777777777777777E/\\
	  \E                              E/
	   \E                            E/
	    \E                          E/
	     \E                        E/
	      \E                      E/
	       \E                    E/
		\EEEEEEEEEEEEEEEEEEEE/



	""",
	"""\
	                        __
		                EI\\
		                 EI\\
		                  EI\\
		                   EI\\
		                    EQ\\
		                     VMmmmmm\\
	/\E77777777777777777777777777777777E/\\
	  \E                              E/
	   \E                            E/
	    \E                          E/
	     \E                        E/
	      \E                      E/
	       \E                    E/
		\EEEEEEEEEEEEEEEEEEEE/



	""",
	"""\







	/\E77777777777777777777777777777777E/\\
	  \E                              E/
	   \E                            E/
	    \E                          E/
	     \E                        E/
	      \E                      E/
	       \E                    E/
		\EEEEEEEEEEEEEEEEEEEE/



	""",
	"""\
        _____________________
        ________________^^^^_
                        ((((
                        ]]]]
                        []]]
                        ))))
                        ((((
	/\E77777777777777777777777777777777E/\\
	  \E                              E/
	   \E                            E/
	    \E                          E/
	     \E                        E/
	      \E                      E/
	       \E                    E/
		\EEEEEEEEEEEEEEEEEEEE/



	""",
	"""\







	/\E77777777777777777777777777777777E/\\
	  \E                              E/
	   \E                            E/
	    \E                          E/
	     \E                        E/
	      \E                      E/
	       \E                    E/
		\EEEEEEEEEEEEEEEEEEEE/



	""",
	"""\
        _____________________
        ________________^^^^_
                        ((((
                        ]]]]
                        []]]
                        ))))
                        ((((
	/\E77777777777777777777777777777777E/\\
	  \E                              E/
	   \E                            E/
	    \E                          E/
	     \E                        E/
	      \E                      E/
	       \E                    E/
		\EEEEEEEEEEEEEEEEEEEE/



	""",
	"""\







	/\E77777777777777777777777777777777E/\\
	  \E                              E/
	   \E                            E/
	    \E                          E/
	     \E                        E/
	      \E                      E/
	       \E                    E/
		\EEEEEEEEEEEEEEEEEEEE/



	""",
	"""\



     GGGGGGGG      A       M     M  EEEEEEE    EEEEEEE  N     N  DDDD
    G             A A      MM   MM  E          E        NN    N  D   D
    G            A   A     M M M M  E          E        N N   N  D    D
    G    GGG    A     A    M  M  M  EEEEEE     EEEEEE   N  N  N  D    D
    G      G    AAAAAAA    M     M  E          E        N   N N  D    D
    G      G   A       A   M     M  E          E        N    NN  D   D
     GGGGGGG  A         A  M     M  EEEEEEE    EEEEEEE  N     N  DDDD



	"""
    ]

    print("\n")
    for frame in frames:
        clear_screen()
        sys.stdout.write("\r" + frame)  # Overwrite the current line
        sys.stdout.flush()  # Force the output to update immediately
        time.sleep(0.5)  # Time interval between frames
    time.sleep(3)
    clear_screen()

    print("\n")

