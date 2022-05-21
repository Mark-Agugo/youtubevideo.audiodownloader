import os
import time
import requests
from pytube import YouTube
from pytube import Playlist
import sys
import re
from pathlib import Path

class VideoAudio:

    def __init__(self):
        self.downloads_path = str(Path.home() / "Downloads")
        try:
            self.videoaudio()
        except Exception:
            print("[-] Something Went Wrong ):")
            sys.exit()

    def checkConnection(self):
        print("[+] Checking Connection...")
        return requests.get(url="http://www.youtube.com")


    def videoaudio(self):
        response = self.checkConnection()
        if response.status_code == 200:
            print("[+] Connection Ok.")
            time.sleep(5)
            print("VIDEO --> AUDIO DOWNLOADER")

            url = input("Youtube Video Url >> ")

            yt = YouTube(url=url,
                         allow_oauth_cache=True,
                         use_oauth=False)

            print("Video Title >> " + yt.title + "\n")
            print("Video Description :> " + yt.description + "\n")
            print("Download Mp3"
                  "\n[1] Yes"
                  "\n[2] No")

            ans = int(input(">> "))

            if ans == 1:
                print("[+] Downloading Audio...")
                yts = yt.streams.filter(only_audio=True).first()
                downloaded_file = yts.download(output_path=self.downloads_path)
                base, ext = os.path.splitext(downloaded_file)
                new_file = base + '.mp3'
                os.rename(downloaded_file, new_file)

                print("[+] Download Complete!")
                sys.exit()
            else:
                sys.exit()