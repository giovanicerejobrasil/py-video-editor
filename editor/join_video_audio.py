import os
from moviepy import (  # type: ignore
    VideoFileClip,
    AudioFileClip,
    CompositeAudioClip,
    CompositeVideoClip
)


class JoinVideoAudio:
    def __init__(self, video_path: str, audio_path: str):
        self.video_path = video_path
        self.audio_path = audio_path

    def process(self):
        self.__load_video_without_audio()
        self.__load_audio()
        self.__join_video_audio()
        self.__change_file_name()
        self.__save_new_video()

    def __load_video_without_audio(self):
        self.video = VideoFileClip(self.video_path).without_audio()

    def __load_audio(self):
        self.audio = AudioFileClip(self.audio_path)

    def __join_video_audio(self):
        try:
            new_audioclip = CompositeAudioClip([self.audio])

            self.video_with_audio = CompositeVideoClip([self.video])
            self.video_with_audio.audio = new_audioclip
        except Exception as error:
            print(f'Error: {error}')

    def __change_file_name(self):
        video_path, video_extension = os.path.splitext(
            self.video_path)
        self.video_path = f'{video_path}'\
            '-with-new-audio.mp4'

    def __save_new_video(self):
        try:
            self.video_with_audio.write_videofile(
                self.video_path,
                codec='libx264',
                audio_codec='aac',
                threads=4,
                logger=None,
            )

            self.video.close()
            self.audio.close()
            self.video_with_audio.close()

            print('Video with new audio joined successfully')
        except Exception as error:
            print(f'ERROR: {error}')
