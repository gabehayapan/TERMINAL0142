# -*- coding: utf-8 -*-
"""
Ultra-fast MVP: Text-based 'No Midnight Ramen' ADV
Usage: python3 runner.py
"""
import json, sys, os

SCENARIO_FILE = os.path.join(os.path.dirname(__file__), "scenario.json")

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

def main():
	data = load_scenario(SCENARIO_FILE)
	node_id = data.get("start")
	nodes = data.get("nodes", {})
	state = {"will": 0, "sleep": 0}

	while True:
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

# エンディング後にステート表示（デバッグ用）
	print("\n[あなたのステータス]")
	for k, v in state.items():
		print(f"- {k}: {v}")

if __name__ == "__main__":
    main()
