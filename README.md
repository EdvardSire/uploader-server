# Uploader server
The server-side functionality for the Firefox add-on [Uploader-plugin](https://github.com/EdvardSire/uploader-plugin)

## server.js
A Node.js HTTP server that receives POST requests from the plugin and passes a given video-URL to download.py

## download.py
A script that passes a given video-URL to the system install of youtube-dl and saves the video on the server

- Returns a callback to server.js

## upload.py
A script that authenticates and uploads a videos to the [YouTube Data API](https://developers.google.com/youtube/v3/)

- Triggers on the callback of download.py