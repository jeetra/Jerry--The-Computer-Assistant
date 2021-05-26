from pytube import YouTube
link=input("Enter the link of video: ")
video=YouTube(link)
stream=video.streams.get_highest_resolution()
stream.download()

print("Video Downloading done.")