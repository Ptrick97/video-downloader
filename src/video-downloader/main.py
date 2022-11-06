from models.video import Video

video_link = input("Insert a video link: ")

my_video = Video(link=video_link)

my_video.download_video()
print(f"{my_video.title} download done.")
