import time
from atcoder_offline import atcoder
from atcoder_offline import drive
from atcoder_offline import notion
from atcoder_offline import screenshot
from atcoder_offline.api import API


def main():
    # save_contest_page("abc289", ["c"])
    clear_screenshot()
    pass


def save_contest_page(contest_name, problem_idf):
    """
    コンテストのproblem_idfのタグがついた問題についてスクショをとる
    Googleドライブに保存
    Notionのデータベースにページを作成する

    Args:
        contest_name: abc293
        problem_idf: ["a", "b", "c"]
    Returns: (None)
    """

    # AtCoder problemからdifficultyを取得
    difficulties = atcoder.get_difficulty(contest_name, problem_idf)

    # スクショの撮影
    for idf in problem_idf:
        # 問題名の取得
        problem_name = f"{contest_name}_{idf}"
        print(f"problem_name: {problem_name}")
        print("-----------------------------------------------")

        # notionにproblem_nameが存在したらスキップ
        if notion.notion_exist_data(problem_name):
            continue

        # 問題の色を取得
        color = difficulties[problem_name]

        # 色に応じた保存先を設定
        folder_id = API.get_folder_id_from_color(color)

        # 問題ページの撮影
        url = f"https://atcoder.jp/contests/{contest_name}/tasks/{problem_name}?lang=ja"
        print(f"URL: {url}")

        filename = f"{problem_name}_problem.png"
        screenshot.save_screenshot(url, filename)

        # google driveへ保存
        drive.save_file_to_drive(filename, folder_id)

        print("Complete! wait 5 seconds...")
        print("")
        time.sleep(5)

        # 解説ページの撮影
        url = atcoder.get_url_from_explain(contest_name, problem_name)
        print(f"URL: {url}")

        filename = f"{problem_name}_explain.png"
        screenshot.save_screenshot(url, filename)

        # google driveへ保存
        drive.save_file_to_drive(filename, folder_id)

        print("Complete! wait 5 seconds...")
        time.sleep(5)

        # notion APIでデータを挿入
        notion.notion_post(problem_name, color)

        print("===============================================")


def clear_screenshot():
    """
    NotionのデータベースでstatusをDoneとしたデータについて，
    Googleドライブからスクショを削除し，
    statusをCompleteに置き換える

    Args: (None)
    Returns: (None)
    """

    # statusがDoneのデータを取得
    problem_names, colors = notion.notion_get_from_status("Done")

    if len(problem_names) == 0:
        return

    # Googleドライブからファイルを削除
    drive.delete_problem_file(problem_names, colors)

    # NotionのstatusをDone -> Complete
    notion.notion_update_status()


if __name__ == "__main__":
    main()
