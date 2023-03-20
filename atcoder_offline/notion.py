import requests
import json


def notion_post(problem_name, color):
    url = "https://api.notion.com/v1/pages"

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

    url = "https://api.notion.com/v1/pages"

    headers = {
        "Accept": "application/json",
        "Notion-Version": "2022-06-28",
        "Content-Type": "application/json",
        "Authorization": "Bearer " + api_key,
    }

    payload = {
        "parent": {"database_id": data_base_id},
        "icon": {"emoji": emoji},
        "properties": {
            "Name": {
                "title": [{"text": {"content": title_today}}],
            },
            "Tags": {"multi_select": [{"name": tag_name}]},
            "detail": {
                "rich_text": [{"text": {"content": detail_text}}],
            },
            "date": {"date": {"start": created_iso_format}},
        },
        "children": [
            {
                "object": "block",
                "type": "heading_1",
                "heading_1": {
                    "rich_text": [{"text": {"content": "今日のTopics!!!"}}],
                },
            },
            {
                "object": "block",
                "type": "heading_2",
                "heading_2": {
                    "rich_text": [{"text": {"content": "アジェンダ"}}],
                },
            },
            {
                "object": "block",
                "type": "heading_2",
                "heading_2": {
                    "rich_text": [{"text": {"content": "Action Items"}}],
                },
            },
            {
                "object": "block",
                "type": "to_do",
                "to_do": {
                    "rich_text": [{"text": {"content": "ToDo 1"}}],
                    "checked": False,
                    "color": "default",
                },
            },
        ],
    }

    response = requests.post(url, json=payload, headers=headers)

    result_dict = response.json()
    result = result_dict["object"]
    page_url = result_dict["url"]

    if result == "page":
        print("success")
        requests.post(
            slack_webhook_url,
            data=json.dumps(
                {
                    # メッセージ内容
                    "text": "今日の議事録が作成されたよ～！！　みんなトピックを記載してね！！ \n "
                    + page_url,
                }
            ),
        )
    elif result == "error":
        requests.post(
            slack_webhook_url,
            data=json.dumps(
                {
                    # メッセージ内容
                    "text": "なんかエラーが発生しているみたい！まじごめん！！　手動で議事録作って！！ \n "
                    + page_url,
                }
            ),
        )
    else:
        requests.post(
            slack_webhook_url,
            data=json.dumps(
                {
                    # メッセージ内容
                    "text": "例外起きて草。なんも分からん。とりあえず手動で議事録作って。ごめんね。。 \n "
                    + page_url,
                }
            ),
        )
