import json


def get_env():
    data = {}
    with open("config/env.json", mode="r") as f:
        data = json.load(f)

    return data


def get_notion_token():
    return get_env()["TOKEN_NOTION"]
