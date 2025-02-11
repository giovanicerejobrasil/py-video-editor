import librosa  # type: ignore
from noisereduce import reduce_noise  # type: ignore
import soundfile  # type: ignore
import os


class RemoveNoise:
    def __init__(self, audio_path):
        self.audio_path = audio_path

    def process(self):
        self.__load_audio()
        self.__select_noise_sample()
        self.__reduce_noise()
        self.__change_file_name()
        self.__save_audio()

    def __load_audio(self):
        self.audio, self.sample_rate = librosa.load(self.audio_path)

    def __select_noise_sample(self):
        self.noise_sample = self.audio / 2.5

    def __reduce_noise(self):
        try:
            self.reduce_noise = reduce_noise(
                y=self.audio,
                y_noise=self.noise_sample,
                sr=self.sample_rate,
                prop_decrease=1.0,
                stationary=True,
            )
        except Exception as error:
            print(f'ERROR: {error}')

    def __change_file_name(self):
        audio_path, audio_extension = os.path.splitext(
            self.audio_path)
        self.audio_path = f'{audio_path}'\
            f'-noise-remove{audio_extension}'

    def __save_audio(self):
        try:
            soundfile.write(f'{self.audio_path}',
                            self.reduce_noise, self.sample_rate)
            print('Noise removed successfully')
        except Exception as error:
            print(f'ERROR: {error}')
