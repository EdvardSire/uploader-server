# Links
# https://developers.google.com/youtube/v3/docs/videos/insert?apix=true
# https://stackoverflow.com/a/60425453
# https://web-u-project.com/tech/2019/06/12/google_api_client_for_python.html

import os
import pickle
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from googleapiclient.http import MediaFileUpload

def upload():
    scopes = ["https://www.googleapis.com/auth/youtube.upload"]

    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "YOUR_CLIENT_SECRET_FILE.json"
    credentials_pickle_file = "credentials_pickle_file"

    if os.path.exists(credentials_pickle_file):
        with open(credentials_pickle_file, 'rb') as f:
            credentials = pickle.load(f)
    else:
        flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(client_secrets_file, scopes)
        credentials = flow.run_console()
        with open(credentials_pickle_file, 'wb') as f:
            pickle.dump(credentials, f)

    youtube = googleapiclient.discovery.build(api_service_name, api_version, credentials=credentials)

    request = youtube.videos().insert(
        part="snippet,status",
        body={
          "snippet": {
            "categoryId": "22",
            "description": "Description of uploaded video.",
            "title": "Test video upload."
          },
          "status": {
            "privacyStatus": "private"
          }
        },
        
        # Name of video
        media_body=MediaFileUpload("video.mp4")
    )
    response = request.execute()

    print(response)

if __name__ == "__main__":
    upload()
