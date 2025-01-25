import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QTimer


class TransparentWindow(QMainWindow):
    def __init__(self, kill_time=10):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.label = QLabel(self)
        pixmap = QPixmap('./capyybara.png')
        pixmap = pixmap.scaled(300, 300, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.label.setPixmap(pixmap)

        self.dragging = False
        self.offset = None

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.close)
        self.timer.start(kill_time * 1000)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(True)
    pet = TransparentWindow(kill_time=10)
    pet.show()
    sys.exit(app.exec_())