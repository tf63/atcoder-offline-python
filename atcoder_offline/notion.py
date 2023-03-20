import requests
from atcoder_offline.api import API


def notion_post(problem_name, color):
    """
    Notionのデータベースにproblem_name, colorをもつデータを追加する
    (colorはこの関数内で求めるべき?)

    Args:
        problem_name: abc293_a
        color: 灰
    Returns: (None)
    """

    # request先
    url = f"{API.get_url_notion()}/pages"

    # ヘッダ
    headers = {
        "Accept": "application/json",
        "Notion-Version": "2022-06-28",
        "Content-Type": "application/json",
        "Authorization": "Bearer " + API.get_notion_token(),
    }

    # 中身
    payload = {
        "parent": {"database_id": API.get_notion_database_id()},
        "properties": {
            "contest": {
                "type": "title",
                "title": [{"type": "text", "text": {"content": problem_name}}],
            },
            "color": {
                "select": {"name": color, "color": API.get_tag_from_color(color)}
            },
            "status": {"select": {"name": "Not started", "color": "gray"}},
        },
    }

    # 送信
    requests.post(url, json=payload, headers=headers)


def notion_get():
    """
    Notionのデータベースを取得する
    (動作テスト用)

    Args: (None)
    Returns: データベース (json)
    """

    # リクエスト先
    url = f"{API.get_url_notion()}/databases/{API.get_notion_database_id()}/query"

    # ヘッダ
    headers = {
        "Notion-Version": "2022-06-28",
        "Content-Type": "application/json",
        "Authorization": "Bearer " + API.get_notion_token(),
    }

    # レスポンス
    response = requests.get(url, headers=headers)

    # 結果
    result_dict = response.json()
    result = result_dict["results"]

    return result


def notion_exist_data(problem_name):
    """
    問題がNotionのデータベースに存在するかどうかを返す

    Args: abc293_a
    Returns: DBにproblem_nameが
                存在する: true,
                存在しない: false
    """

    # リクエスト先
    url = f"{API.get_url_notion()}/databases/{API.get_notion_database_id()}/query"

    # ヘッダ
    headers = {
        "Notion-Version": "2022-06-28",
        "Content-Type": "application/json",
        "Authorization": "Bearer " + API.get_notion_token(),
    }

    # titleがproblem_nameのデータを取得する
    payload = {"filter": {"property": "contest", "title": {"equals": problem_name}}}

    # レスポンス
    response = requests.post(url, json=payload, headers=headers)

    # 結果
    result_dict = response.json()
    result = result_dict["results"]

    # resultが空かどうかを返す
    for res in result:
        print(res)
    if len(result) > 0:
        return True
    else:
        return False
