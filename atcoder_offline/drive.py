from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive


def save_file_to_drive(filename, folder_id):
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()

    drive = GoogleDrive(gauth)

    metadata = {
        "parents": [{"id": folder_id}],
        "title": filename,
        "mimeType": "image/png",
    }

    f = drive.CreateFile(metadata=metadata)
    f.SetContentFile(f"/work/out/img/{filename}")
    f.Upload()
