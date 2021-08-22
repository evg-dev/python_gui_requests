#! /usr/bin/python3
import json
import sys

import requests as r
from PyQt5.QtGui import QFont, QIntValidator
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QLabel, QApplication, QAction, QSlider, QFileDialog, QMainWindow, QPushButton, qApp, \
    QInputDialog, QLineEdit, QComboBox, QTextEdit


# from PyQt5.QtCore import QThread, Qt, pyqtSignal, pyqtSlot
# from PyQt5.QtGui import QPixmap, QImage

def on_changed(text):
    print(text)


class MainWindow(QMainWindow):
    default_url = 'http://example.com/'

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setWindowTitle('Python Gui Requests')
        self.setGeometry(300, 300, 640, 1100)
        self.setFixedSize(640, 1100)
        # self.setFixedSize(self.sizeHint())
        # create a labels
        self.label_headers = QLabel('Response Headers', self)
        self.label_headers.setGeometry(0, 100, 640, 70)
        self.label_headers.setAlignment(QtCore.Qt.AlignCenter)

        self.label_body = QLabel('Body response', self)
        self.label_body.setGeometry(0, 100, 640, 950)
        self.label_body.setAlignment(QtCore.Qt.AlignCenter)

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
        self.method.activated[str].connect(on_changed)

        self.url = QLineEdit(self)
        self.url.move(150, 50)
        self.url.resize(400, 30)
        self.url.setText(self.default_url)

        self.output_headers = QTextEdit(self)
        self.output_headers.setReadOnly(True)
        self.output_headers.setLineWrapMode(QTextEdit.NoWrap)
        self.output_headers.move(0, 150)
        self.output_headers.resize(640, 400)

        self.output_body = QTextEdit(self)
        self.output_body.setReadOnly(True)
        self.output_body.setLineWrapMode(QTextEdit.NoWrap)
        self.output_body.move(0, 600)
        self.output_body.resize(640, 400)

        self.output_status_code = QLabel('Status code : ', self)
        self.output_status_code.move(0, 70)
        self.output_status_code.setGeometry(0, 70, 640, 70)
        self.output_status_code.setAlignment(QtCore.Qt.AlignCenter)

        self.send_request_btn = QPushButton('Send Request', self)
        self.send_request_btn.move(500, 50)
        self.send_request_btn.resize(90, 30)
        self.send_request_btn.clicked.connect(self.send_request)

        self.show()

    def send_request(self):

        method = self.method.currentText()
        url = self.url.text()
        # TODO: set headers, and post params
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

        self.get_response(response)

    def get_response(self, response):
        h = json.dumps(dict(response.headers), sort_keys=True, indent=4)
        self.output_status_code.setText(
            'Status code : ' + '<span style="font-weight:600;">' + str(response.status_code) + '</span>')
        self.output_headers.setPlainText(h)
        self.output_body.setPlainText(response.text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    display_image_widget = MainWindow()
    display_image_widget.show()
    sys.exit(app.exec_())
