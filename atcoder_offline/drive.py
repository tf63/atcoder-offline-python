from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive


def save_file_to_drive(img_path, savefolder_id):
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()

    drive = GoogleDrive(gauth)

    metadata = {
        "parents": [{"id": savefolder_id}],
        "title": "image_test",
        "mimeType": "image/png",
    }

    f = drive.CreateFile(metadata=metadata)
    f.SetContentFile(img_path)
    f.Upload()
