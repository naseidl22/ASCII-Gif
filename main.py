import sys
import os
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QPushButton, QLabel, QFileDialog,
    QVBoxLayout, QHBoxLayout,
    QSlider, QProgressBar, QMessageBox
)
from PySide6.QtCore import Qt
from converter import convert_gif


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("ASCII GIF Converter")
        self.resize(600, 350)

        self.input_path = None
        self.output_path = None

        central = QWidget()
        self.setCentralWidget(central)

        main_layout = QVBoxLayout()

        # File selection
        self.file_label = QLabel("No file selected")
        self.open_button = QPushButton("Select GIF")
        self.open_button.clicked.connect(self.select_file)

        main_layout.addWidget(self.file_label)
        main_layout.addWidget(self.open_button)

        # Scale slider
        self.scale_label = QLabel("Scale: 65%")
        self.scale_slider = QSlider(Qt.Horizontal)
        self.scale_slider.setMinimum(20)
        self.scale_slider.setMaximum(100)
        self.scale_slider.setValue(65)
        self.scale_slider.valueChanged.connect(self.update_scale_label)

        main_layout.addWidget(self.scale_label)
        main_layout.addWidget(self.scale_slider)

        # Font size slider
        self.font_label = QLabel("Font Size: 8")
        self.font_slider = QSlider(Qt.Horizontal)
        self.font_slider.setMinimum(6)
        self.font_slider.setMaximum(20)
        self.font_slider.setValue(8)
        self.font_slider.valueChanged.connect(self.update_font_label)

        main_layout.addWidget(self.font_label)
        main_layout.addWidget(self.font_slider)

        # Convert button
        self.convert_button = QPushButton("Convert")
        self.convert_button.clicked.connect(self.convert)
        main_layout.addWidget(self.convert_button)

        # Progress bar
        self.progress = QProgressBar()
        self.progress.setValue(0)
        main_layout.addWidget(self.progress)

        central.setLayout(main_layout)

    def select_file(self):
        path, _ = QFileDialog.getOpenFileName(
            self, "Select GIF", "", "GIF Files (*.gif)"
        )
        if path:
            self.input_path = path
            self.output_path = os.path.splitext(path)[0] + "_ascii.gif"
            self.file_label.setText(f"Selected: {os.path.basename(path)}")

    def update_scale_label(self):
        self.scale_label.setText(f"Scale: {self.scale_slider.value()}%")

    def update_font_label(self):
        self.font_label.setText(f"Font Size: {self.font_slider.value()}")

    def convert(self):
        if not self.input_path:
            QMessageBox.warning(self, "No File", "Please select a GIF first.")
            return

        try:
            self.progress.setValue(10)

            convert_gif(
                self.input_path,
                self.output_path,
                scale=self.scale_slider.value() / 100,
                font_size=self.font_slider.value(),
                progress_callback=self.update_progress
            )

            self.progress.setValue(100)
            QMessageBox.information(self, "Done", "Conversion complete!")

        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def update_progress(self, value):
        self.progress.setValue(value)


app = QApplication(sys.argv)
app.setStyle("Fusion")
window = MainWindow()
window.show()
sys.exit(app.exec())