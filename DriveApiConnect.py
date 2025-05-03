from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

def upload_to_gdrive(file_path):
    gauth = GoogleAuth()

    # Try to load saved client credentials
    gauth.LoadCredentialsFile("mycreds.txt")

    if gauth.credentials is None:
        # Authenticate if they're not there
        gauth.LocalWebserverAuth()
    elif gauth.access_token_expired:
        # Refresh the credentials if expired
        gauth.Refresh()
    else:
        # Authorize the credentials if still valid
        gauth.Authorize()

    # Save the credentials for next run
    gauth.SaveCredentialsFile("mycreds.txt")

    # Initialize Google Drive object
    drive = GoogleDrive(gauth)

    # Create a new file and upload it
    file_to_upload = drive.CreateFile({'title': file_path.split("/")[-1]})
    file_to_upload.SetContentFile(file_path)
    file_to_upload.Upload()
    print(f"✅ File '{file_path}' uploaded to Google Drive.")
