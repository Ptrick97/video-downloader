from pytube import YouTube


OUTPUT_PATH = "../../downloaded-videos"
FILENAME_PREFIX = "my_video_"


class Video:
    def __init__(self, link: str):
        self.youtube_video = YouTube(link)

        self.link = link
        self.title = self.youtube_video.title
        self.views = self.youtube_video.views
        self.length = self.youtube_video.length
        self.author = self.youtube_video.author

    def download_video(self, output_path: str = OUTPUT_PATH, filename_prefix: str = FILENAME_PREFIX):
        self.youtube_video.streams.get_highest_resolution().download(
            output_path=output_path,
            filename_prefix=filename_prefix
        )
        print(f"{self.title} download done. Saved in {output_path}")

    def download_audio(self, output_path: str = OUTPUT_PATH, filename_prefix: str = FILENAME_PREFIX):
        self.youtube_video.streams.get_audio_only().download(
            output_path=output_path,
            filename_prefix=filename_prefix
        )
        print(f"Audio from {self.title} downloaded. Saved in {output_path}")
