import librosa  # type: ignore
from noisereduce import reduce_noise  # type: ignore
import soundfile  # type: ignore
import os


class RemoveNoise:
    def __init__(self, audio_path):
        self.audio_path = audio_path

    def process(self) -> str:
        la = self.__load_audio()
        sns = self.__select_noise_sample()
        rn = self.__reduce_noise()
        cfn = self.__change_file_name()
        sa = self.__save_audio()
        return f'{la} \n{sns} \n{rn} \n{cfn} \n{sa}'

    def __load_audio(self) -> str:
        self.audio, self.sample_rate = librosa.load(self.audio_path)
        return f'Loaded audio: {self.audio_path}'

    def __select_noise_sample(self) -> str:
        self.noise_sample = self.audio / 2.5
        return f'Selected noise sample: {self.noise_sample}'

    def __reduce_noise(self) -> str:
        try:
            self.reduce_noise = reduce_noise(
                y=self.audio,
                y_noise=self.noise_sample,
                sr=self.sample_rate,
                prop_decrease=1.0,
                stationary=True,
            )
            return f'Noise reduced: {self.reduce_noise}'
        except Exception as error:
            return f'ERROR: {error}'

    def __change_file_name(self) -> str:
        audio_path, audio_extension = os.path.splitext(
            self.audio_path)
        self.audio_path = f'{audio_path}'\
            f'-noise-remove{audio_extension}'
        return f'Changed file name: {self.audio_path}'

    def __save_audio(self) -> str:
        try:
            soundfile.write(f'{self.audio_path}',
                            self.reduce_noise, self.sample_rate)
            return 'Noise saved successfully'
        except Exception as error:
            return f'ERROR: {error}'
