import json


def load_ytd(path):
    with open(path, "r", encoding="utf-8") as f:
      text = f.read()

    text = text.split("=", 1)[1]
    return json.loads(text)