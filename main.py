# This is the main code for the GUI, and functions of the application.
# Provide your own Groq API key in the config.py file.

from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QTextBrowser, QTextEdit, QPushButton, QComboBox, QLabel, QCheckBox
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt, QEvent
import markdown2
import sys
from config import MODELS, client, SYSTEM_PROMPT

class ChatbotApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("GroQT Chat")
        self.setGeometry(100, 100, 800, 700)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)

        self.header_layout = QHBoxLayout()
        self.main_layout.addLayout(self.header_layout)

        self.title_label = QLabel("GroQT Chat")
        self.title_label.setFont(QFont("Helvetica", 20, QFont.Weight.Bold))
        self.header_layout.addWidget(self.title_label)

        self.header_layout.addStretch()

        # Dark mode switcher
        self.dark_mode_switch = QCheckBox("Dark Mode")
        self.dark_mode_switch.setFont(QFont("Helvetica", 14))
        self.dark_mode_switch.setChecked(True)
        self.dark_mode_switch.stateChanged.connect(self.toggle_dark_mode)
        self.header_layout.addWidget(self.dark_mode_switch)

        # Chat display
        self.chat_display = QTextBrowser()
        self.chat_display.setOpenExternalLinks(True)
        self.chat_display.setReadOnly(True)
        self.chat_display.setFont(QFont("Helvetica", 16))
        self.main_layout.addWidget(self.chat_display)

        # Input layout
        self.input_layout = QHBoxLayout()
        self.main_layout.addLayout(self.input_layout)

        # User input
        self.user_input = QTextEdit()
        self.user_input.setPlaceholderText("Type your message here...")
        self.user_input.setFont(QFont("Helvetica", 18))
        self.user_input.setFixedHeight(110)
        self.user_input.installEventFilter(self)
        self.input_layout.addWidget(self.user_input)

        # Button layout
        self.button_layout = QVBoxLayout()
        self.input_layout.addLayout(self.button_layout)

        # Send button
        self.send_button = QPushButton("Send")
        self.send_button.setFont(QFont("Helvetica", 16))
        self.send_button.setStyleSheet("background-color: #007BFF; color: white; padding: 15px; border: none; border-radius: 10px;")
        self.send_button.clicked.connect(self.send_message)
        self.button_layout.addWidget(self.send_button)

        # Model selection dropdown
        self.model_selector = QComboBox()
        self.model_selector.addItems(MODELS.keys())
        self.model_selector.setCurrentText("Meta Llama 3 70B")
        self.model_selector.setFont(QFont("Helvetica", 18))
        self.button_layout.addWidget(self.model_selector)

        # Apply dark mode by default
        self.is_dark_mode = True
        self.apply_dark_mode()

    def toggle_dark_mode(self):
        self.is_dark_mode = self.dark_mode_switch.isChecked()
        self.apply_dark_mode()

    def apply_dark_mode(self):
        if self.is_dark_mode:
            dark_style = """
            QWidget {
                background-color: #2e2e2e;
                color: #ffffff;
            }
            QTextEdit, QTextBrowser, QComboBox {
                background-color: #3e3e3e;
                border: 1px solid #1e1e1e;
                color: #ffffff;
                border-radius: 10px;
            }
            QPushButton {
                background-color: #007BFF;
                border: none;
                padding: 10px;
                color: #ffffff;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #0056b3;
            }
            QComboBox QAbstractItemView {
                background-color: #3e3e3e;
                border: 1px solid #1e1e1e;
                color: #ffffff;
                border-radius: 10px;
            }
            """
        else:
            dark_style = """
            QWidget {
                background-color: #f0f0f0;
                color: #000000;
            }
            QTextEdit, QTextBrowser, QComboBox {
                background-color: #ffffff;
                border: 1px solid #cccccc;
                color: #000000;
                border-radius: 10px;
            }
            QPushButton {
                background-color: #007BFF;
                border: none;
                padding: 10px;
                color: #ffffff;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #0056b3;
            }
            QComboBox QAbstractItemView {
                background-color: #ffffff;
                border: 1px solid #cccccc;
                color: #000000;
                border-radius: 10px;
            }
            """
        self.setStyleSheet(dark_style)

    def send_message(self):
        user_message = self.user_input.toPlainText()
        if user_message.strip():
            self.display_message("You", user_message, is_user=True)
            self.user_input.clear()
            self.get_bot_response(user_message)

    def display_message(self, sender, message, is_user=False):
        user_style = "margin-bottom: 15px;"
        bot_style = "margin-bottom: 15px; padding: 5px; border: 2px solid #FF5722; border-radius: 5px;"
        style = user_style if is_user else bot_style

        formatted_message = f"""
        <div style='margin-bottom: 10px;'>
            <b>{sender}:</b> <div style='{style}'>{message}</div>
        </div>
        """
        self.chat_display.append(formatted_message)

    def display_markdown_message(self, sender, markdown_message):
        html_message = markdown2.markdown(markdown_message)
        self.display_message(sender, html_message, is_user=False)

    def get_bot_response(self, user_message):
        selected_model_id = MODELS[self.model_selector.currentText()]
        try:
            chat_completion = client.chat.completions.create(
                messages=[
                    SYSTEM_PROMPT,
                    {"role": "user", "content": user_message}
                ],
                model=selected_model_id,
            )
            bot_response = chat_completion.choices[0].message.content
            self.display_markdown_message("Bot", bot_response)
        except Exception as e:
            self.display_message("Bot", f"An error occurred: {str(e)}")

    def eventFilter(self, source, event):
        if event.type() == QEvent.Type.KeyPress:
            if event.key() == Qt.Key.Key_Return and event.modifiers() == Qt.KeyboardModifier.ShiftModifier:
                self.user_input.insertPlainText("\n")
                return True
            elif event.key() == Qt.Key.Key_Return:
                self.send_message()
                return True
        return super().eventFilter(source, event)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ChatbotApp()
    window.show()
    sys.exit(app.exec())
