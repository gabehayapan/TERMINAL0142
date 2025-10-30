# -*- coding: utf-8 -*-
"""
Ultra-fast MVP: Text-based 'No Midnight Ramen' ADV
Usage: python3 runner.py
"""
import json, sys, os, time, threading, asyncio

from animation import opening_animation
from animation import ending_animation
from animation import clear_screen
from graphics import print_clock_room_0
from graphics import display_current_time
from endroll import endroll_animation

def wait_for_start():
	input("Press ENTER to start the game!")

async def main():
	opening_animation()
	wait_for_start();

	clear_screen()
	time.sleep(2)
	clear_screen()
	ending_animation()
	endroll_animation()

if __name__ == "__main__":
    asyncio.run(main())
