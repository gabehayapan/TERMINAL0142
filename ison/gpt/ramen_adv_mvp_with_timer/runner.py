# -*- coding: utf-8 -*-
"""
Ultra-fast MVP: Text-based 'No Midnight Ramen' ADV
- Adds a configurable countdown timer that starts immediately after you enter it.
- Input formats: seconds (e.g., 300) or mm:ss (e.g., 5:00). Use 0 to disable.
- On timeout, the game ends with a TIME OUT message.
"""
import json, sys, os, time

# POSIX alarm (Linux/macOS). On Windows, alarm is unavailable; we fall back to no hard timeout.
USE_ALARM = True
try:
    import signal
    if not hasattr(signal, "alarm"):
        USE_ALARM = False
except Exception:
    USE_ALARM = False

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

def parse_duration(s: str) -> int:
    s = s.strip()
    if not s:
        return 0
    if ":" in s:
        parts = s.split(":")
        if len(parts) != 2:
            raise ValueError("mm:ss 形式が正しくありません")
        m, sec = parts
        return int(m) * 60 + int(sec)
    return int(s)

class Timeout(Exception):
    pass

def setup_alarm(seconds: int):
    if seconds <= 0:
        return 0
    if not USE_ALARM:
        print("※ この環境ではハードタイムアウトは無効です（Windowsなど）。経過時間のみ計測します。")
        return 0
    def handler(signum, frame):
        raise Timeout()
    signal.signal(signal.SIGALRM, handler)
    signal.alarm(seconds)
    return seconds

def main():
    # === Timer setup ===
    print("タイマーを設定してください（秒 または mm:ss、0で無効）")
    while True:
        try:
            raw = input("Timer> ").strip()
            duration = parse_duration(raw)
            break
        except Exception as e:
            print("入力例: 300 / 5:00 / 0  :", e)

    start_time = time.time()
    remaining = setup_alarm(duration)  # start countdown immediately
    if duration > 0:
        print(f"⏳ カウントダウン開始: {duration} 秒")

    # === Scenario ===
    data = load_scenario(SCENARIO_FILE)
    node_id = data.get("start")
    nodes = data.get("nodes", {})
    state = {"will": 0, "sleep": 0}

    try:
        while True:
            node = nodes.get(node_id)
            if node is None:
                print(f"ノード '{node_id}' が見つかりません。scenario.json を確認してください。")
                sys.exit(1)

            more = print_node(node)
            if not more:
                break

            # show prompt with remaining seconds (approximate)
            if duration > 0 and USE_ALARM:
                elapsed = int(time.time() - start_time)
                left = max(0, duration - elapsed)
                prompt = f"> （残り{left}秒）"
            else:
                prompt = "> "

            try:
                raw = input(prompt).strip()
            except Timeout:
                # input() interrupted by SIGALRM
                print("\n⏰ 時間切れ！ラーメンは冷めてしまった…（TIME OUT END）")
                raise

            if raw.lower() in ("q", "quit", "exit"):
                print("終了します。")
                break
            try:
                idx = int(raw) - 1
                choice = node["choices"][idx]
            except (ValueError, IndexError):
                print("番号を選んでください（終了: q）")
                continue

            apply_effect(state, choice.get("effect"))
            node_id = choice["next"]

    except Timeout:
        pass
    finally:
        # cancel alarm and report elapsed
        if USE_ALARM:
            try:
                signal.alarm(0)
            except Exception:
                pass
        total = time.time() - start_time
        print(f"\n[プレイ時間] {total:.1f} 秒")
        print("[あなたのステータス]")
        for k, v in state.items():
            print(f"- {k}: {v}")

if __name__ == "__main__":
    main()
