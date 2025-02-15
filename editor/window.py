from pathlib import Path
from .extract_audio import ExtractAudio
from .remove_noise import RemoveNoise
from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout,
    QFileDialog,
    QPlainTextEdit,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Window")
        self.setFixedSize(400, 300)

        # Create central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Create main layout
        main_layout = QVBoxLayout(central_widget)

        # Create horizontal layout for label and input
        video_path_layout = QHBoxLayout()
        render_path_layout = QHBoxLayout()

        # Create widgets
        label = QLabel("Video Path:")
        self.video_field = QLineEdit()
        self.video_field.setEnabled(False)  # Disable input field
        video_path = QPushButton("...")

        # Add label and input to horizontal layout
        video_path_layout.addWidget(label)
        video_path_layout.addWidget(self.video_field)
        video_path_layout.addWidget(video_path)

        # Create widgets
        label = QLabel("Render Path:")
        self.render_field = QLineEdit()
        self.render_field.setEnabled(False)  # Disable input field
        render_path = QPushButton("...")

        # Add label and input to horizontal layout
        render_path_layout.addWidget(label)
        render_path_layout.addWidget(self.render_field)
        render_path_layout.addWidget(render_path)

        # Create a render button
        send_button = QPushButton("Render")

        # Create a text editor log
        self.text_editor = QPlainTextEdit()

        # Add layouts and button to main layout
        main_layout.addLayout(video_path_layout)
        main_layout.addLayout(render_path_layout)
        main_layout.addWidget(send_button)
        main_layout.addWidget(self.text_editor)

        # Add stretch to push button to bottom
        main_layout.addStretch()

        # Connect button click
        video_path.clicked.connect(self.on_video_path_clicked)
        render_path.clicked.connect(self.on_render_path_clicked)
        send_button.clicked.connect(self.on_send_clicked)

    def on_send_clicked(self):
        video_path = self.video_field.text()
        render_path = self.render_field.text()

        self.text_editor.appendPlainText(f"Video Path: {video_path}")
        self.text_editor.appendPlainText(f"Render Path: {render_path}")

        self.__extract_audio()

    def on_video_path_clicked(self):
        path = QFileDialog()
        text_path = path.getOpenFileName(
            self,
            "Open Video",
            "/",
            "Video Files (*.mp4 *.mkv *.avi *.flv *.mov *.wmv)"
        )
        self.video_field.setText(text_path[0])

    def on_render_path_clicked(self):
        path = QFileDialog()
        text_path = path.getExistingDirectory(
            self,
            "Save Video",
            "/",
        )
        self.render_field.setText(text_path)

    def __extract_audio(self):
        video_path = Path(self.video_field.text())
        audio_output_path = Path(self.video_field.text()).parent / 'sources'

        extract_audio = ExtractAudio(
            video_path,
            audio_output_path
        )
        extract_audio_process = extract_audio.process()

        self.text_editor.appendPlainText(f"{extract_audio_process}")

    def __remove_noise(self):
        audio_path = Path(self.video_field.text()).parent / \
            'sources' / 'audio.wav'
        remove_noise = RemoveNoise(audio_path)
        remove_noise_process = remove_noise.process()

        self.text_editor.appendPlainText(f"{remove_noise_process}")
