from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import Signal, QThread, QObject
from PySide6.QtGui import QIcon, QTextCursor
from images import Ui_Form
from io import StringIO
from lianshou import download_file
import sys


class Thread(QThread):
    finished = Signal(str)

    def __init__(self, url):
        super().__init__()
        self.url = url

    def run(self):
        download_file(self.url)
        self.finished.emit(self.url)


# class Redirect:
#     def __init__(self, text_edit):
#         self.text_edit = text_edit
#
#     def write(self, str):
#         self.text_edit.appendPlainText(str)
#
#     def flush(self):
#         self.text_edit.setPlainText("")

class EmittingThread(QObject):
    textWritten = Signal(str)

    def write(self, text):
        self.textWritten.emit(str(text))

    def flush(self):
        pass


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        # self.redirect = Redirect(self.ui.plainTextEdit)
        # sys.stdout = self.redirect
        sys.stdout = EmittingThread()
        sys.stdout.textWritten.connect(self.normal_update)
        self.bind()

    def bind(self):
        self.ui.pushButton.clicked.connect(self.start_download)
        self.ui.pushButton_2.clicked.connect(self.clear)

    def normal_update(self, text):
        cursor = self.ui.plainTextEdit.textCursor()
        cursor.movePosition(QTextCursor.End)
        cursor.insertText(text)
        self.ui.plainTextEdit.ensureCursorVisible()

    def start_download(self):
        url = self.ui.lineEdit.text()
        self.thread = Thread(url)
        self.thread.start()
        self.thread.finished.connect(self.thread.finished.emit)

    def clear(self):
        self.ui.plainTextEdit.setPlainText("")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec()
