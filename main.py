from termcolor import colored, cprint
from scripts import singlevideo, playlist, videoaudio


def print_banner(title=""):

    cprint("""
 \ \           / /      ____              ____      _______________
  \ \         / /       |  |\            /|  |      | |          \ \    
   \ \       / /        |  | \          / |  |      | |    __     \ \M
    \ \     / /         |  |  \        /  |  |      | |   |  |     \ \A
     \ \   / /          |  |   \      /   |  |      | |   |  |      \ \C
      \ \ / /           |  |    \    /    |  |      | |   |  |       | |
      | | | |           |  |     \  /     |  |      | |   |  |       | |
      | | | |           |  |      \/      |  |      | |   |  |      /  /
      | | | |           |  |              |  |      | |    --      /  /
      | | | |           |__|              |__|      | |___________/  /
                                                    |_______________/
""", "red")
    total_len = 80
    if title:
        padding = total_len - len(title) - 4
        cprint("{} {}\n".format(title, "=" * padding), "blue")
    else:
        print("{}\n".format("=" * total_len))

print_banner("Youtube Video Downloader! \nCreated By mactechloop. \n\n\nWhat do you wanna do "
      "\n[1] Single Video Download \n[2] Playlist Download \n[3] Video --> Audio Download")

ans = input("Your Choice >> ")

while True:
    if str(ans) == "1":
        singlevideoclass = singlevideo.SingleVideo()
        singlevideoclass.singleVideo()
        break
    elif str(ans) == "2":
        playlistclass = playlist.Playlist()
        playlistclass.playlist()
        break
    elif str(ans) == "3":
        videoaudioclass = videoaudio.VideoAudio()
        videoaudioclass.videoaudio()
        break
    else:
        ans = input("Your Choice >> ")


