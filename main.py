import openai
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPalette, QColor, QLinearGradient, QPainter, QCursor
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QTextEdit

openai.api_key = 'YOUR_OPENAI_API_KEY'

class ModernWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # set up window
        self.setWindowTitle("GPT3 Chatbot")
        self.setGeometry(100, 100, 800, 600)

        # set up palette
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor("#202225"))
        palette.setColor(QPalette.WindowText, QColor("#ffffff"))
        palette.setColor(QPalette.Base, QColor("#36393f"))
        palette.setColor(QPalette.AlternateBase, QColor("#40444b"))
        palette.setColor(QPalette.ToolTipBase, QColor("#ffffff"))
        palette.setColor(QPalette.ToolTipText, QColor("#000000"))
        palette.setColor(QPalette.Text, QColor("#ffffff"))
        palette.setColor(QPalette.Button, QColor("#7289da"))
        palette.setColor(QPalette.ButtonText, QColor("#ffffff"))
        palette.setColor(QPalette.Highlight, QColor("#7289da"))
        palette.setColor(QPalette.HighlightedText, QColor("#ffffff"))
        self.setPalette(palette)

        # set up font
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.setFont(font)

        # set up main widget and layout
        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)
        main_layout = QVBoxLayout(main_widget)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(0)

        # set up output field
        self.output_field = QTextEdit()
        self.output_field.setObjectName("output-field")
        self.output_field.setReadOnly(True)
        self.output_field.setFrameShape(QTextEdit.NoFrame)
        self.output_field.setFixedHeight(450)
        main_layout.addWidget(self.output_field)

        # set up input widget and layout
        input_widget = QWidget(main_widget)
        input_layout = QHBoxLayout(input_widget)
        input_layout.setContentsMargins(0, 0, 0, 0)
        input_layout.setSpacing(0)
        main_layout.addWidget(input_widget)

        # set up input field and button
        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("Type here to chat...")
        self.input_field.setObjectName("input-field")
        input_layout.addWidget(self.input_field)

        self.input_button = QPushButton("Send")
        self.input_button.setObjectName("input-button")
        self.input_button.setCursor(QCursor(Qt.PointingHandCursor))
        input_layout.addWidget(self.input_button)

        # load CSS
        with open("style.css") as f:
            self.setStyleSheet(f.read())

        self.input_button.clicked.connect(self.gpt)

    def gpt(self):
        prompt = self.input_field.text()
        self.input_field.setText("")
        self.output_field.append("<span style='color:#ffffff;'>You:</span> " + prompt)

        response = openai.Completion.create(
            engine="text-davinci-003", prompt=prompt,
            max_tokens=2000)

        output_text = response["choices"][0]["text"]
        self.output_field.append("<span style='color:#ffffff;'>GPT-3:</span> " + output_text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ModernWindow()
    window.show()
    sys.exit(app.exec_())
