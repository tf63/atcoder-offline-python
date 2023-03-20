import requests
import json
import atcoder_offline.api as api


def notion_post(problem_name, color):
    env = api.get_env()
    url = f'{env["API_NOTION"]}/pages'

    headers = {
        "Accept": "application/json",
        "Notion-Version": "2022-06-28",
        "Content-Type": "application/json",
        "Authorization": "Bearer " + env["TOKEN_NOTION"],
    }

    payload = {
        "parent": {"database_id": env["DATABASE_ID"]},
        "properties": {
            "contest": {
                "type": "title",
                "title": [{"type": "text", "text": {"content": problem_name}}],
            },
            "color": {"select": {"name": color, "color": env["COLOR_TO_TAG"][color]}},
            "status": {"select": {"name": "Not started", "color": "gray"}},
        },
    }

    requests.post(url, json=payload, headers=headers)


def notion_get(problem_name):
    env = api.get_env()
    url = f'{env["API_NOTION"]}/databases/{env["DATABASE_ID"]}/query'

    headers = {
        "Notion-Version": "2022-06-28",
        "Content-Type": "application/json",
        "Authorization": "Bearer " + env["TOKEN_NOTION"],
    }

    response = requests.get(url, headers=headers)

    result_dict = response.json()
    result = result_dict["results"]

    return result


def notion_exist_data(problem_name):
    """
    DBにproblem_nameが
    存在する: true,
    存在しない: false
    """

    env = api.get_env()
    url = f'{env["API_NOTION"]}/databases/{env["DATABASE_ID"]}/query'

    headers = {
        "Notion-Version": "2022-06-28",
        "Content-Type": "application/json",
        "Authorization": "Bearer " + env["TOKEN_NOTION"],
    }

    payload = {"filter": {"property": "contest", "title": {"equals": problem_name}}}
    response = requests.post(url, json=payload, headers=headers)

    result_dict = response.json()
    result = result_dict["results"]
    print(result_dict, len(result))
    for res in result:
        print(res)
    if len(result) > 0:
        return True
    else:
        return False
