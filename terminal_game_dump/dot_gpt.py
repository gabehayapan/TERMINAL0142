import time
import sys

def pouring_water_animation():
    # Frames of the animation (each frame will overwrite the previous one)
    frames = [
        """\
     ________
    |        |
    |  RAMEN |
    |________|""",  # Empty cup (initial state)
        
        """\
     ________
    |        |
    |  RAMEN |
    |________|
    ~""",  # First pour (water level 1)

        """\
     ________
    |        |
    |  RAMEN |
    |________|
    ~ ~""",  # Second pour (water level 2)

        """\
     ________
    |        |
    |  RAMEN |
    |________|
    ~ ~ ~""",  # Third pour (water level 3)

        """\
     ________
    |        |
    |  RAMEN |
    |________|
    ~ ~ ~ ~""",  # Fourth pour (water level 4)

        """\
     ________
    |        |
    |  RAMEN |
    |________|
    ~ ~ ~ ~
    ~~~~~~~~~~"""  # Lid closing after full cup
    ]
    
    # Display each frame with a delay to simulate the pouring animation
    print("Pouring hot water into the ramen cup...")
    for frame in frames:
        sys.stdout.write("\r" + " " * 80)  # Clear the current line (write spaces)
        sys.stdout.write("\r" + frame)  # Overwrite the current line
        sys.stdout.flush()  # Force the output to update immediately
        time.sleep(0.5)  # Time interval between frames

    print("\nThe lid is now closed!")

# Call the function to display the animation
pouring_water_animation()

