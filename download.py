import os
import sys

def download(url):
    options = "youtube-dl " + url + " -o video.mp4 >/dev/null 2>&1"
    # Supress the output
    os.system(options)

if __name__ == "__main__":
    # Parse the url
    url = sys.argv[1:][0]
    download(url)
    # Manually trigger the callback
    print("Video downloaded")
