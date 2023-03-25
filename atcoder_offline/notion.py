import requests
import json
import time

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
    if len(result) > 0:
        return True
    else:
        return False


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


def notion_get_from_status(status):
    """
    Notionのデータベースを取得し，statusが(status)となっている問題名と色を返す

    Args:
        status: Not Started/Done/Complete
    Returns:
        problem_names: statusの問題のリスト ['abc293_a', ...]
        colors: statusの問題の色のリスト ['灰', ...]
    """

    # リクエスト先
    url = f"{API.get_url_notion()}/databases/{API.get_notion_database_id()}/query"

    # ヘッダ
    headers = {
        "Notion-Version": "2022-06-28",
        "Content-Type": "application/json",
        "Authorization": "Bearer " + API.get_notion_token(),
    }

    # statusがDoneのデータを取得する
    payload = {"filter": {"property": "status", "select": {"equals": status}}}

    # レスポンス
    response = requests.post(url, json=payload, headers=headers)

    # 結果
    result_dict = response.json()
    results = result_dict["results"]

    problem_names = []
    colors = []

    for result in results:
        problem_names.append(
            result["properties"]["contest"]["title"][0]["text"]["content"]
        )
        colors.append(result["properties"]["color"]["select"]["name"])

    print(f"Find problems (Done): {problem_names}")
    return problem_names, colors


def notion_update_status(before="Done", after="Complete"):
    """
    Notionのデータベースを取得し，statusがDoneとなっているデータをCompleteに置き換える

    Args:
        before: 更新前のstatus (Done)
        after: 更新後のstatus (Complete)
    Returns: (None)
    """

    # リクエスト先
    url = f"{API.get_url_notion()}/databases/{API.get_notion_database_id()}/query"

    # ヘッダ
    headers = {
        "Notion-Version": "2022-06-28",
        "Content-Type": "application/json",
        "Authorization": "Bearer " + API.get_notion_token(),
    }

    # statusがDoneのデータを取得する
    payload = {"filter": {"property": "status", "select": {"equals": before}}}

    # レスポンス
    response = requests.post(url, json=payload, headers=headers)

    # 結果
    result_dict = response.json()
    results = result_dict["results"]

    for result in results:
        print(
            f"Update! Done -> Complete: {result['properties']['contest']['title'][0]['text']['content']}, wait 5 seconds..."
        )

        page_id = result["id"]

        url = f"{API.get_url_notion()}/pages/{page_id}"

        data = {"properties": {"status": {"select": {"name": after, "color": "green"}}}}
        response = requests.patch(url, headers=headers, data=json.dumps(data))

        time.sleep(5)
