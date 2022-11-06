from models.video import Video

video_link = input("Insert a video link: ")
print((
    "[1] audio\n"
    "[2] video"
))
choice = int(input("What do you want download? "))
my_video = Video(link=video_link)

if choice == 1:
    my_video.download_audio()
elif choice == 2:
    my_video.download_video()
else:
    print("Please choose a valid command")
