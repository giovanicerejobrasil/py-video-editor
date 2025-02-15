import os
from moviepy import VideoFileClip  # type: ignore


class ExtractAudio():
    def __init__(self, video_path: str, audio_path_output: str) -> None:
        self.video_path = video_path
        self.audio_path_output = audio_path_output
        self.video = VideoFileClip(video_path)

    def process(self) -> str:
        ea = self.__extract_audio()
        sa = self.__save_audio()

        return f'{ea} \n{sa}'

    def __extract_audio(self) -> str:
        try:
            self.audio = self.video.audio

            return 'Audio extracted successfully'
        except Exception as error:
            return f'ERROR: {error}'

    def __save_audio(self) -> str:
        try:
            if not os.path.isdir(self.audio_path_output):
                os.mkdir(self.audio_path_output)

            self.audio.write_audiofile(
                f'{self.audio_path_output}/audio-extract.mp3')

            self.video.close()
            self.audio.close()

            return 'Audio saved successfully'
        except Exception as error:
            return f'ERROR: {error}'
