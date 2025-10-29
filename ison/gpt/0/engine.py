import json, sys

with open("scenario.json", "r", encoding="utf-8") as f:
    data = json.load(f)

state = {"will": 0, "sleep": 0}
node_id = data["start"]

def apply_effect(effect):
    if not effect: return
    for k,v in effect.items():
        state[k] = state.get(k,0) + v

def render(node):
    print("\n" + node["text"])
    if not node.get("choices"):
        print("\n=== END ==="); sys.exit(0)
    for i, ch in enumerate(node["choices"], 1):
        print(f"{i}. {ch['label']}")

while True:
    node = data["nodes"][node_id]
    render(node)
    try:
        i = int(input("> ")) - 1
        ch = node["choices"][i]
    except Exception:
        print("番号を選んでね"); continue
    apply_effect(ch.get("effect"))
    node_id = ch["next"]

