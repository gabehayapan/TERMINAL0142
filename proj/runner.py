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

SCENARIO_FILE = os.path.join(os.path.dirname(__file__), "scenario.json")

def wait_for_start():
	input("Press ENTER to start the game!")

def load_scenario(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print("scenario.json が見つかりません。同じフォルダに置いてください。")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print("scenario.json の読み込みに失敗しました:", e)
        sys.exit(1)

def print_node(node):
    print("\n" + node.get("text",""))
    choices = node.get("choices", [])
    if not choices:
        print("\n=== THE END ===")
        return False
    for i, ch in enumerate(choices, 1):
        print(f"{i}. {ch['label']}")
    return True

def apply_effect(state, effect):
    if not effect:
        return
    for k, v in effect.items():
        state[k] = state.get(k, 0) + v

def parse_duration(s):
	if ":" in s:
		m, s = s.split(":")
		return int(m) * 60 + int(s)
	return int(s)

async def asyncio_timer(timer_sec, story):
	await asyncio.sleep(timer_sec)
	story.cancel()

async def asyncio_story(node_id, nodes, state):
	try:
		while True:
			clear_screen()
			if (node_id == "room_0"):
				print_clock_room_0()
			node = nodes.get(node_id)
			if node is None:
				print(f"ノード '{node_id}' が見つかりません。scenario.json を確認してください。")
				sys.exit(1)
	
			more = print_node(node)
			if not more:
				break
	
			try:
				raw = input("> ").strip()
				if raw.lower() in ("q", "quit", "exit"):
					print("終了します。")
					break
				idx = int(raw) - 1
				choice = node["choices"][idx]
			except (ValueError, IndexError):
				print("番号を選んでください（終了: q）")
				continue
	
			apply_effect(state, choice.get("effect"))
			node_id = choice["next"]

	except asyncio.CancelledError:
		return node;

def time_to_eat(data, nodes, last_node):
	print("\n" + "ピピピッ, ピピピッ, ...タイマーが鳴った。")
	end_node_id = last_node["end"]
	clear_screen()
	node = nodes.get(node_id)
	more = print_node(node)


async def main():
	opening_animation()
	data = load_scenario(SCENARIO_FILE)
	node_id = data.get("start")
	nodes = data.get("nodes", {})
	state = {"will": 0, "sleep": 0}
	wait_for_start();

#	user_input = input("タイマーを設定してください(sec or mm:ss) : ")
#	timer_sec = parse_duration(user_input)
	story = asyncio.create_task(asyncio_story(node_id, nodes, state))
#	await_timer = asyncio.create_task(asyncio_timer(timer_sec, story))

#	await await_timer
#	last_node = await story

#	time_to_eat(data, nodes, last_node)

	await story

	clear_screen()
#	display_current_time(timer_sec)
	time.sleep(2)
	clear_screen()
	ending_animation()

	# エンディング後にステート表示（デバッグ用）
	print("\n[あなたのステータス]")
	for k, v in state.items():
		print(f"- {k}: {v}")

if __name__ == "__main__":
    asyncio.run(main())
