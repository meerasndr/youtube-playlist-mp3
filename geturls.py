''' 
    Code snippet to grab the URLs of all the videos in a YouTube playlist, given the playlist URL
'''
import os
import sys
try:
	from pytube import Playlist
except ModuleNotFoundError:
	os.system('pip3 install pytube')

def get_video_urls(playlist_url):
    video_urls = []
    try:
        playlist = Playlist(playlist_url)
    except:
        print("There is a problem with the playlist URL")
    else:
        for url in playlist:
            video_urls.append(url)
        return video_urls

def write_video_urls(video_urls, filename):
    with open(filename, 'w') as f:
    	for url in video_urls:
    		f.write(url+'\n')
    print(f'Urls saved in {filename}')    
    

try:
    playlist_url = sys.argv[1]
    filename = sys.argv[2]
except:
    print("Error :: Provide two arguments: 1) YouTube playlist URL 2) filename to write video URLs to")
else:
    video_urls = get_video_urls(playlist_url)
    write_video_urls(video_urls, filename)
