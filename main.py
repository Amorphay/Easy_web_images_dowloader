from PySide6.QtWidgets import QApplication, QWidget, QGraphicsScene, QGraphicsView, QGraphicsPixmapItem, QLabel
from PySide6.QtCore import Signal, QThread, QObject
from PySide6.QtGui import QIcon, QTextCursor, QPixmap
from gui import Ui_Form, QFont
from spider import download_file
import sys
from urllib.parse import urlsplit
import os
import random
from extract import match
from qt_material import apply_stylesheet
import static.icon_rc

extral = {
    'font_family': 'mini-wakuwaku'
}


class Thread(QThread):
    finished = Signal(str)

    def __init__(self, url):
        super().__init__()
        self.url = url

    def run(self):
        download_file(self.url)
        self.finished.emit(self.url)


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
        self.setGeometry(0, 0, 1170, 476)
        self.view = QGraphicsView(self)
        self.view.setGeometry(700, 50, 450, 400)
        self.setWindowIcon(QIcon(':/images/icon1.ico'))
        self.scene = QGraphicsScene(self)
        self.view.setSceneRect(self.view.rect())
        self.view.setScene(self.scene)
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
        result = match(text)
        if result:
            code_dir = os.path.dirname(os.path.abspath(__file__))
            domain = "\\{0.netloc}\\".format(urlsplit(self.url))
            path = code_dir + '\\images' + domain + result.group()
            img = QPixmap(path)
            if img.isNull():
                pass
            else:
                item = QGraphicsPixmapItem(img)
                item.setPos(random.randint(0, 250), random.randint(0, 250))
                item.setRotation(random.randint(0, 30))
                item.setScale(0.4)
                self.scene.addItem(item)

        else:
            pass

    def start_download(self):
        temp = self.ui.lineEdit.text()
        domain = "{0.scheme}://{0.netloc}".format(urlsplit(temp))
        print(domain)
        self.url = domain
        self.thread = Thread(temp)
        self.thread.start()
        self.thread.finished.connect(self.thread.deleteLater)

    def clear(self):
        self.ui.plainTextEdit.setPlainText("")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    apply_stylesheet(app, 'light_pink.xml', extra=extral)
    window.show()
    app.exec()
