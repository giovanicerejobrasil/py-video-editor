from moviepy import VideoFileClip  # type: ignore


class ExtractAudio():
    def __init__(self, video_path: str, audio_path_output: str) -> None:
        self.video_path = video_path
        self.audio_path_output = audio_path_output
        self.video = VideoFileClip(video_path)

    def process(self) -> None:
        self.__extract_audio()
        self.__save_audio()

    def __extract_audio(self) -> None:
        self.audio = self.video.audio

    def __save_audio(self) -> None:
        try:
            self.audio.write_audiofile(self.audio_path_output)

            print('Audio extracted successfully')
            self.video.close()
            self.audio.close()
        except Exception as error:
            print(f'ERROR: {error}')
