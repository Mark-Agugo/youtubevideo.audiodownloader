import time
import requests
from pytube import YouTube
from pytube import Playlist
import sys
import re
from pathlib import Path

class SingleVideo:
    def __init__(self):
        self.downloads_path = str(Path.home() / "Downloads")
        try:
            self.singleVideo()
        except Exception:
            print("[-] Something Went Wrong ):")
            sys.exit()

    def checkConnection(self):
        print("[+] Checking Connection...")
        return requests.get(url="http://www.youtube.com")


    def singleVideo(self):
        response = self.checkConnection()
        if response.status_code == 200:
            print("[+] Connection Ok.")
            time.sleep(5)
            print("SINGLE VIDEO DOWNLOADER")

            url = input("Youtube Video Url >> ")

            yt = YouTube(url=url,
                         allow_oauth_cache=True,
                         use_oauth=False)
            print("Video Title >> " + yt.title +"\n")
            print("Video Description :> " + yt.description + "\n")
            print("[+] Processing Video Streams...")
            filters = yt.streams.filter(file_extension="mp4", progressive=True)

            res = str(re.findall('res."\d*."', str(filters)))
            resN = re.findall('\d*', res)
            resN = list(filter(None, resN))

            for i in range(len(resN)):
                print((resN[i]))

            val = input("[+] Select Resolution : ")
            while True:
                if str(val) not in str(resN):
                    val = input("[+] Select Resolution : ")

                else:
                    a = filters.get_by_resolution(val + "p")
                    print("[+] Downloading Video...")
                    a.download(output_path=self.downloads_path)
                    print("[+] Download Complete!")
                    sys.exit()
                    break
        else:
            print("[-] No Connection.")
            sys.exit()

