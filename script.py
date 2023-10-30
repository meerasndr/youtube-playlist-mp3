''' 
    Code snippet to extract MP3 audio from videos that are part of a YouTube playlist
'''
import os
import sys
try:
    from pytube import Playlist
    import yt_dlp as youtube_dl
except ModuleNotFoundError:
    os.system('pip3 install pytube')
    os.system('pip3 install yt_dlp')

def get_video_urls(playlist_url):
    ''' Given a playlist URL, get the URLs of all the videos in the playlist '''
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

def download_mp3(video_urls):    
    options = {
      'format': 'bestaudio/best',
      'extractaudio' : True,  # only keep the audio
      'audioformat' : "mp3",  # convert to mp3 
      'outtmpl': '%(title)s',    # name of output file
      'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    }
    with youtube_dl.YoutubeDL(options) as ydl:
        for url in video_urls:
            try:
                ydl.download(url)
            except:
                print(f"Problem downloading video {url}")

def main():
    try:
        playlist_url = sys.argv[1]
    except:
        print("Error :: Provide argument:: YouTube playlist URL")
    else:
        video_urls = get_video_urls(playlist_url)
        download_mp3(video_urls)   

if __name__ == '__main__' :
    main()

