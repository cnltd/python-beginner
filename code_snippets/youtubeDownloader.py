# project specific libraries
# depedency management
# virtual environments --> venv
# enev syntax : python -m venv env
# to activate: .\env\Scripts\activate
# to deactivate: deactivate

# Python package manager - pip
# pip install pytube
from pytube import YouTube

url = 'https://www.youtube.com/watch?v=6Rt5Pj1XauE'

my_video = YouTube(url)

video_title = my_video.title

print(f"My youtube video title is: {video_title}")

stream = my_video.streams.filter(file_extension='mp4')

print(type(stream))

for video in stream:
    print(video)

itag = 18

stream = my_video.streams.get_by_itag(18)
stream.download()
