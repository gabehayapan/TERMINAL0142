import json, sys, os, time, threading, asyncio

from threading import Thread

from animation import opening_animation
from animation import ending_animation
from animation import clear_screen
from graphics import display_clock_start
from graphics import display_current_time
from endroll import endroll_animation

FILE_NAME = "scenario.json"
SCENARIO_FILE = os.path.join(os.path.dirname(__file__), FILE_NAME)
ITSTIME = threading.Event()

class CustomThread(Thread):
	def __init__(self, group=None, target=None, name=None, args=(), kwargs={}, verbose=None):
		super().__init__(group, target, name, args, kwargs)
		self._return = None

	def run(self):
		if self._target is not None:
			self._return = self._target(*self._args, **self._kwargs)
	
	def join(self):
		super().join()
		return self._return

def wait_for_start():
	input("\n" + "Press ENTER to start the game")

def end_the_game():
	input("\n" + "Press ENTER to end the game")

def enter_to_continue():
	input("\n" + "Press ENTER to continue")

def load_scenario(path):
	try:
		with open(path, "r", encoding="utf-8") as f:
			return json.load(f)
	except FileNotFoundError:
		print(f"{FILE_NAME}の読み込みに失敗しました:", e)
		sys.exit(1)
	except json.JSONDecodeError as e:
		print(f"{FILE_NAME}の読み込みに失敗しました:", e)
		sys.exit(1)

def print_node(node):
	print("\n" + node.get("text", ""))
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

def set_timer(timer_sec):
	time.sleep(timer_sec)
	ITSTIME.set()

def story_before_timer(node_id, nodes, state, timer_sec):
	while not ITSTIME.is_set():
		clear_screen()
		if (node_id == "room_0"):
			display_clock_start()
		node = nodes.get(node_id)
		if node is None:
			print(f"ノード'{node_id}'が見つかりません。{FILE_NAME}を確認してください。")
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
	
	clear_screen()
	print("\n" + "ピピピッ, ピピピッ, ...タイマーが鳴った。")
	display_current_time(timer_sec)
	time.sleep(2)
	return node

def story_time_to_eat(nodes, last_node):
	end_node_id = last_node.get('end')

	node = nodes.get(end_node_id)
	print("\n\n\n" + node.get("text", ""))
	time.sleep(1.5)
	enter_to_continue()

def main():
	opening_animation()
	data = load_scenario(SCENARIO_FILE)
	node_id = data.get("start")
	nodes = data.get("nodes", {})
	state = {"will": 0, "sleep": 0}
	wait_for_start()

	user_input = input("タイマーを設定してください(sec or mm:ss) : ")
	timer_sec = parse_duration(user_input)
	story = CustomThread(target=story_before_timer, args=(node_id, nodes, state, timer_sec))
	timer = threading.Thread(target=set_timer, args=(timer_sec,))

	story.start()
	timer.start()

	last_node = story.join()
	timer.join()

	story_time_to_eat(nodes, last_node)

	clear_screen()
	ending_animation()
	endroll_animation()
	end_the_game()

if __name__ == "__main__":
	main()
