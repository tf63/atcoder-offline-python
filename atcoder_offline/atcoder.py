import requests
import re
import sys

sys.path.append("lib.bs4")
from bs4 import BeautifulSoup
from atcoder_offline.api import API


def get_difficulty(contest_name, problem_idf):
    """
    Args:
        contest_name = "abc293"
        problem_idf = ["a", "b", "c"]
    Returns:
        {'abc293_a': '灰', 'abc293_b': '灰', 'abc293_c': '茶'}
    """

    data_json = read_json_from_url(API.get_url_atcoder_problem())

    datas = {}
    for idf in problem_idf:
        problem_name = f"{contest_name}_{idf}"
        data = data_json[problem_name]
        color = get_color_from_difficulty(data["difficulty"])

        datas[problem_name] = color

    return datas


def read_json_from_url(url):
    """
    web上のjsonファイルを取得する

    Args: url
    Returns: json data (dictionary)
    """
    response = requests.get(url)
    data = response.json()

    return data


def get_color_from_difficulty(difficulty):
    """
    difficultyを色に変換する
    """

    color = ""
    if difficulty < 400:
        color = "灰"
    elif difficulty < 800:
        color = "茶"
    elif difficulty < 1200:
        color = "緑"
    elif difficulty < 1600:
        color = "水"
    elif difficulty < 2000:
        color = "青"
    elif difficulty < 2400:
        color = "黄"
    else:
        color = "橙"

    return color


def get_url_from_explain(contest_name, problem_name):
    """
    問題の解説ページを取得する

    Args:
        contest_name: abc293
        problem_name: abc293_a
    Returns:
        url
    """

    # コンテストの解説タブのページを取得する
    url = f"https://atcoder.jp/contests/{contest_name}/editorial?lang=ja"
    response = requests.get(url)
    html = response.content

    # BeautifulSoup
    soup = BeautifulSoup(html, "lxml")

    # problem_nameに対応するリンクを探す
    soup = soup.find(
        "a",
        attrs={
            "class": "small",
            "href": f"/contests/{contest_name}/tasks/{problem_name}",
        },
    )

    # -> <a href="/contests/abc293/editorial/5956" rel="noopener" target="_blank">解説</a>
    soup = soup.find_next(
        "a",
        attrs={
            "target": "_blank",
            "rel": "noopener",
            "href": re.compile(f"^/contests/{contest_name}/editorial/"),
        },
    )

    # -> "/contests/abc293/editorial/5956"
    dist = soup["href"]

    return f"https://atcoder.jp{dist}/?lang=ja"
