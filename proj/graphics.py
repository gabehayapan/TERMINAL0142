import sys
import asyncio

def print_clock_start():
	graphic = """
 _______________________
|                       |
| ##     #     #  #  ## |
|#  #    #   * #  #    #|
|#  #    #      ###  ## |
|#  #    #   *    # #   |
| ##     #        #  ## |
 _______________________
"""
	sys.stdout.write("\r" + graphic)
	sys.stdout.flush()

def display_60():
	graphic = """
 _______________________
|                       |
| ##     #     #  #  ## |
|#  #    #   * #  #    #|
|#  #    #      ###  ## |
|#  #    #   *    #    #|
| ##     #        #  ## |
 _______________________
"""
	sys.stdout.write("\r" + graphic)
	sys.stdout.flush()

def display_120():
	graphic = """
 _______________________
|                       |
| ##     #     #  # #  #|
|#  #    #   * #  # #  #|
|#  #    #      ###  ###|
|#  #    #   *    #    #|
| ##     #        #    #|
 _______________________
"""
	sys.stdout.write("\r" + graphic)
	sys.stdout.flush()

def display_180():
	graphic = """
 _______________________
|                       |
| ##     #     #  #  ## |
|#  #    #   * #  # #   |
|#  #    #      ###  ## |
|#  #    #   *    #    #|
| ##     #        =#  ## |
 _______________________
"""
	sys.stdout.write("\r" + graphic)
	sys.stdout.flush()

def display_240():
	graphic = """
 _______________________
|                       |
| ##     #     #  #  ## |
|#  #    #   * #  # #   |
|#  #    #      ### ### |
|#  #    #   *    # #  #|
| ##     #        #  ## |
 _______________________
"""
	sys.stdout.write("\r" + graphic)
	sys.stdout.flush()

def display_300():
	graphic = """
 _______________________
|                       |
| ##     #     #  #  ## |
|#  #    #   * #  #    #|
|#  #    #      ###    #|
|#  #    #   *    #    #|
| ##     #        #    #|
 _______________________
"""
	sys.stdout.write("\r" + graphic)
	sys.stdout.flush()

def display_broken():
	graphic = """
 _______________________
|                       |
| ~#   ~ #     #~~   ## |
|   # #  ~   * ~  #  ~~~|
|#  ~  ~ #      #~~    ~|
|#  ~~   #   *  ~ # #~  |
| ~~  ~      ~  #__    #|
 _______________________
"""
	sys.stdout.write("\r" + graphic)
	sys.stdout.flush()

def display_current_time(timer_sec):
	if (timer_sec < 60):
		display_clock_start()
	else if (timer_sec < 120):
		display_60()
	elif (timer_sec < 180):
		display_120()
	elif (timer_sec < 240):
		display_180()
	elif (timer_sec < 300):
		display_240()
	elif (timer_sec < 360):
		display_300()
	else:
		display_broken()
