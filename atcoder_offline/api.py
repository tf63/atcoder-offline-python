import json


def get_folder_id():
    d = {}
    with open("config/env.json", mode="r") as f:
        d = json.load(f)

    return d["FOLDER_ID"]


def get_color_to_tag():
    pass
