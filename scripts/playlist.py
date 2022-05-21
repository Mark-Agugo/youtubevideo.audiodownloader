import time
import requests
from pytube import YouTube
from pytube import Playlist
import sys
import re
from pathlib import Path

class Playlist:

    def __init__(self):
        self.downloads_path = str(Path.home() / "Downloads")
        try:
            self.playlist()
        except Exception:
            print("[-] Something Went Wrong ):")
            sys.exit()

    def checkConnection(self):
        print("[+] Checking Connection...")
        return requests.get(url="http://www.youtube.com")


    def playlist(self):
        response = self.checkConnection()
        if response.status_code == 200:
            print("[+] Connection Ok.")
            time.sleep(5)
            print("PLAYLIST DOWNLOADER")

            url = input("Playlist Url >> ")

            pl = Playlist(url=url)
            print(pl.title)
            print(pl.description)

            for video in pl.videos:
                print("[+] Downloading Video..")
                video.streams.filter(file_extension="mp4", progressive=True).get_highest_resolution()\
                    .download(output_path=self.downloads_path)
                print("[+] Download Complete!")
                sys.exit()


