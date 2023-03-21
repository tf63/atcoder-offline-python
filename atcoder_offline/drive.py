from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive

from atcoder_offline.api import API


def save_file_to_drive(filename, folder_id):
    """
    ローカルのファイル(/work/out/img/*)をGoogleドライブのfolder_idに対応するフォルダにアップロードする

    Args:
        filename: ローカルの画像のファイル名 image.png
        folder_id: Googleドライブのfolder_id
    Returns: (None)
    """

    # 認証
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()

    # driveを操作するオブジェクト
    drive = GoogleDrive(gauth)

    # 付属する情報
    metadata = {
        "parents": [{"id": folder_id}],
        "title": filename,
        "mimeType": "image/png",
    }

    # ファイルを作成
    f = drive.CreateFile(metadata=metadata)

    # ファイルの中身を作成
    f.SetContentFile(f"/work/out/img/{filename}")

    # ファイルをアップロード
    print(f"Uploading {filename}...")
    f.Upload()


def delete_problem_file(problem_names, colors):
    """
    Googleドライブ内の問題のスクショを削除する

    Args:
        problem_names: 削除する問題のリスト abc293_a.png
        colors: 削除する問題のcolorのリスト
    Returns: (None)
    """

    # 認証
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()

    # driveを操作するオブジェクト
    drive = GoogleDrive(gauth)

    for problem_name, color in zip(problem_names, colors):
        query = f"'{API.get_folder_id_from_color(color)}' in parents and title contains '{problem_name}' and trashed = False"
        file_list = drive.ListFile({"q": query}).GetList()

        if len(file_list) == 0:
            # ファイルが存在しない
            print("Not Found")
        else:
            # ファイルを削除
            for file in file_list:
                file.Delete()

            print(f"Delete {problem_name}")
