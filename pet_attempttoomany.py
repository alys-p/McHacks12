import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QTimer


class TransparentWindow(QMainWindow):
    def __init__(self, max_width, max_height, kill_time=30, step_size=10):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.current_width = 300
        self.current_height = 300
        self.max_width = max_width
        self.max_height = max_height
        self.step_size = step_size

        self.label = QLabel(self)
        pixmap = QPixmap('./capyybara.png')
        self.pixmap = pixmap.scaled(self.current_width, self.current_height, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.label.setPixmap(self.pixmap)

        self.label.resize(self.current_width, self.current_height)
        self.setFixedSize(self.label.size())

        screen = QApplication.primaryScreen().geometry()
        screen_width = screen.width()
        screen_height = screen.height()

        x_position = screen_width - self.current_width
        y_position = screen_height - self.current_height
        self.move(x_position, y_position)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.close)
        self.timer.start(kill_time * 1000)

        self.growth_timer = QTimer(self)
        self.growth_timer.timeout.connect(self.grow)
        self.growth_timer.start(50)

    def grow(self):
        if self.current_width < self.max_width:
            self.current_width += self.step_size
        if self.current_height < self.max_height:
            self.current_height += self.step_size

        self.current_width = min(self.current_width, self.max_width)
        self.current_height = min(self.current_height, self.max_height)

        self.pixmap = QPixmap('./capyybara.png').scaled(self.current_width, self.current_height, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.label.setPixmap(self.pixmap)
        self.label.resize(self.pixmap.width(), self.pixmap.height())

        self.setFixedSize(self.label.size())

        screen = QApplication.primaryScreen().geometry()
        screen_width = screen.width()
        screen_height = screen.height()

        x_position = screen_width - self.current_width
        y_position = screen_height - self.current_height
        self.move(x_position, y_position)

        if self.current_width >= self.max_width and self.current_height >= self.max_height:
            self.growth_timer.stop()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)

    # Create the window and set parameters for growth
    pet = TransparentWindow(max_width=1000, max_height=1000, step_size=10)
    pet.show()
    sys.exit(app.exec_())
