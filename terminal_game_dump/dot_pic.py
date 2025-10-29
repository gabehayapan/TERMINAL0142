import time
import sys

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
        """,  # Second pour (water level 2)

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
             GGGGGGGGGGGG                AAAAAA
	    GG          GG             AA
	   GG            GG          OO
	  GG              GG        OO
          GG              GG        OO
          GG                        OO
          GG                        OO
          GG          GGGGGG        OO
          GG          GGGGGG        OO
          GG              GG        OO
           GG             GG         OO
            GG           GG
             GGGGGGGGGGGGG





        """  # Lid closing after full cup
    ]

    # Display each frame with a delay to simulate the pouring animation
    print("Pouring hot water into the ramen cup...")
    for frame in frames:
        sys.stdout.write("\r" + frame)  # Overwrite the current line
        sys.stdout.flush()  # Force the output to update immediately
        time.sleep(0.5)  # Time interval between frames

    print("\nThe lid is now closed!")

# Call the function to display the animation
opening_animation()

# def ending_animation();
