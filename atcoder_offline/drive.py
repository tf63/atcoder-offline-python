from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive


def save_file_to_drive(filename, folder_id):
    """
    ローカルのファイル(/work/out/img/*)をgoogleドライブのfolder_idに対応するフォルダにアップロードする

    Args:
        filename: ローカルの画像のファイル名 image.png
        folder_id: Google ドライブのfolder_id
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
