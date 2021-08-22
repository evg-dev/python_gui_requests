#! /usr/bin/python3
import json
import sys

import requests as r
from PyQt5.QtGui import QFont, QIntValidator
from PyQt5.QtWidgets import QLabel, QApplication, QAction, QSlider, QFileDialog, QMainWindow, QPushButton, qApp, \
    QInputDialog, QLineEdit, QComboBox, QTextEdit


# from PyQt5.QtCore import QThread, Qt, pyqtSignal, pyqtSlot
# from PyQt5.QtGui import QPixmap, QImage

class MainWindow(QMainWindow):
    default_url = 'https://evg-dev.github.io/'

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setWindowTitle('Python Gui Requests')
        self.setGeometry(300, 300, 640, 900)
        self.setFixedSize(640, 900)
        # create a label
        self.label = QLabel(self)
        # self.label.move(0, 20)
        # self.label.resize(640, 480)

        self.method = QComboBox(self)

        self.method.addItem("GET")
        self.method.addItem("POST")
        self.method.addItem("PUT")
        self.method.addItem("DELETE")
        self.method.addItem("PATCH")
        self.method.addItem("HEAD")
        self.method.addItem("OPTIONS")

        self.method.move(50, 50)
        self.method.resize(100, 30)
        self.method.activated[str].connect(self.on_changed)

        self.url = QLineEdit(self)
        self.url.move(150, 50)
        self.url.resize(400, 30)
        self.url.setText(self.default_url)
        # self.method.setMaxLength(40)

        # self.method.setAlignment(Qt.AlignRight)
        # self.method.setFont(QFont("Arial", 20))

        self.output_headers = QTextEdit(self)
        self.output_headers.setReadOnly(True)
        self.output_headers.setLineWrapMode(QTextEdit.NoWrap)
        self.output_headers.move(0, 100)
        self.output_headers.resize(640, 400)

        self.output_body = QTextEdit(self)
        self.output_body.setReadOnly(True)
        self.output_body.setLineWrapMode(QTextEdit.NoWrap)
        self.output_body.move(0, 500)
        self.output_body.resize(640, 400)

        self.send_request_btn = QPushButton('Send Request', self)
        self.send_request_btn.move(500, 50)
        self.send_request_btn.resize(90, 30)
        self.send_request_btn.clicked.connect(self.send_request)

        self.show()

    def send_request(self):

        method = self.method.currentText()
        url = self.url.text()

        headers = {}
        # params.url = url
        response = ''

        if method == 'GET':
            response = r.get(url)

        if method == 'POST':
            response = r.post(url)

        if method == 'PUT':
            response = r.put(url)

        if method == 'DELETE':
            response = r.delete(url)

        if method == 'PATCH':
            response = r.patch(url)

        if method == 'HEAD':
            response = r.head(url)

        if method == 'OPTIONS':
            response = r.options(url)

        # h = response.headers
        # h = str(h)
        # h = json.loads(h)
        # h = {"name": "Gilbert", "wins": [["straight", "7"], ["one pair", "10"]]}
        # j = json.dumps(h, sort_keys=True, indent=4)
        # print(h)
        # self.output_headers.setPlainText((str(response.headers)))

        h = json.dumps(dict(response.headers), sort_keys=True, indent=4)
        self.output_headers.setPlainText(h)

        self.output_body.setPlainText(response.text)

    def on_changed(self, text):
        print(text)
        # self.qlabel.setText(text)
        # self.qlabel.adjustSize()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    display_image_widget = MainWindow()
    display_image_widget.show()
    sys.exit(app.exec_())
