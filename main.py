import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTextBrowser, QWidget
from PySide6.QtGui import QPixmap, QColor, QPalette, Qt
import requests

from design import Ui_Dialog

class DotaPlayerInfoApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Инициализируем интерфейс из предоставленного дизайна
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # Устанавливаем тему
        self.set_dark_theme()

        # Устанавливаем обработчик нажатия кнопки поиска
        self.ui.pushButton.clicked.connect(self.search_player)

        # Выводим данные о первом игроке при запуске
        self.ui.lineEdit.setText("154944191")  # Пример ID
        self.search_player()

    def set_dark_theme(self):
        # Настройка темной темы для приложения
        app.setStyle("Fusion")
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(53, 53, 53))
        palette.setColor(QPalette.WindowText, Qt.white)
        palette.setColor(QPalette.Base, QColor(35, 35, 35))
        palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
        palette.setColor(QPalette.ToolTipBase, QColor(255, 255, 220))
        palette.setColor(QPalette.ToolTipText, QColor(0, 0, 0))
        palette.setColor(QPalette.Text, Qt.white)
        palette.setColor(QPalette.Button, QColor(53, 53, 53))
        palette.setColor(QPalette.ButtonText, Qt.white)
        palette.setColor(QPalette.BrightText, Qt.red)
        palette.setColor(QPalette.Link, QColor(42, 130, 218))
        palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
        palette.setColor(QPalette.HighlightedText, QColor(255, 255, 255))
        self.setPalette(palette)

    def search_player(self):
        account_id = self.ui.lineEdit.text()
        if account_id:
            player_info = self.get_player_info(account_id)
            if player_info:
                account_info = (
                    f"Account ID: {account_id}\n"
                    f"Personaname: {player_info['profile']['personaname']}\n"
                    f"Country: {player_info['profile']['loccountrycode']}\n"
                    f"Last login: {player_info['profile']['last_login']}\n"
                    f"DotaPlus: {'Activate' if player_info['profile']['plus'] else 'No or private'}\n"
                    f"Leaderboard Rank: {player_info.get('leaderboard_rank', 'N/A')}\n"
                    f"ProfileURL: {player_info['profile']['profileurl']}\n"
                )

                self.ui.textBrowser.setText(account_info)

                avatar_url = player_info.get("profile", {}).get("avatarfull")
                if avatar_url:
                    pixmap = QPixmap()
                    pixmap.loadFromData(requests.get(avatar_url).content)
                    self.ui.label.setPixmap(pixmap)
                else:
                    self.ui.label.setText("Avatar not found")
            else:
                self.ui.textBrowser.setText("Player information not found")

    def get_player_info(self, account_id):
        url = f"https://api.opendota.com/api/players/{account_id}"
        response = requests.get(url)
        if response.status_code == 200:
            player_info = response.json()
            return player_info
        else:
            print("Error while requesting API")

if __name__ == "__main__":
    app = QApplication([])
    window = DotaPlayerInfoApp()
    window.show()
    sys.exit(app.exec())
