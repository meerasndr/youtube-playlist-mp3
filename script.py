'''
Code snippet to extract MP3 audio from videos
that are part of a YouTube playlist
'''
# !/usr/bin/env python3
# script.py

import os
import sys
try:
    from pytube import Playlist
    import yt_dlp as youtube_dl
except ModuleNotFoundError:
    os.system('pip3 install pytube')
    os.system('pip3 install yt_dlp')


def get_video_urls(playlist_url):
    ''' Get the URLs of all the videos in the playlist '''
    video_urls = []
    try:
        playlist = Playlist(playlist_url)
    except Exception as e:
        print(f"There is a problem:: {e}")
    else:
        for url in playlist:
            video_urls.append(url)
        return video_urls


def write_video_urls(video_urls, filename):
    '''
       Optional function: write all the video URLs to a text file.
       Useful where one may want to share the URLs with another person.
    '''
    with open(filename, 'w') as f:
        for url in video_urls:
            f.write(url+'\n')
    print(f'Urls saved in {filename}')


def download_mp3(video_urls):
    '''
    Extract MP3 audio and download to the same folder
    '''
    options = {
      'format': 'bestaudio/best',
      'extractaudio': True,  # only keep the audio
      'audioformat': "mp3",  # convert to mp3
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
            except Exception as e:
                print(f"Problem downloading video {url}:: {e}")


def main():
    ''' Drumroll '''
    try:
        playlist_url = sys.argv[1]
    except Exception as e:
        print(f"Error!! Provide argument:: YouTube playlist URL {e}")
    else:
        video_urls = get_video_urls(playlist_url)
        download_mp3(video_urls)


if __name__ == '__main__':
    main()
