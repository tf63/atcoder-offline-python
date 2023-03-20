import requests
import json
from atcoder_offline import api


def get_difficulty(contest_name, problem_idf):
    """
    Args:
        contest_name = "abc293"
        problem_idf = ["a", "b", "c"]
    Returns:
        {'abc293_a': '灰', 'abc293_b': '灰', 'abc293_c': '茶'}
    """

    env = api.get_env()
    data_json = read_json_from_url(env["API_ATCODER_PROBLEM"])

    datas = {}
    for idf in problem_idf:
        problem_name = f"{contest_name}_{idf}"
        data = data_json[problem_name]
        color = get_color_from_difficulty(data["difficulty"])

        datas[problem_name] = color

    return datas


def read_json_from_url(url):
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
