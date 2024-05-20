import time
from tokenize import String
from pytube import YouTube
from sys import argv
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout, QLineEdit, QProgressBar
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor
import validators

# Dowload function

def download():
    textboxValue = textbox.text()
    yt = YouTube(textboxValue)
    yd = yt.streams.get_highest_resolution()
    yd.download("D:\python projects\youtube downloader")
    textbox.setText('')


def on_dowload():
    response = validators.url(textbox.text())
    if response == True :
       error.setText('')
       time.sleep(10)
       if error.text() == '' :
          download()
    else:
        error.setText('Not a valid url. Please try another!')


def complete_function(stream, file):
    lBytes.setText('Downloaded')
    print(file)


app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("YouTube Downloader")
window.setFixedWidth(1200)
window.setFixedHeight(500)
window.move(2300, 200)
grid = QGridLayout()

# Set text
label = QLabel("Please paste your link below...")
label.resize(10, 10)
label.setAlignment(QtCore.Qt.AlignCenter)
label.setStyleSheet(
    "color: black;" +
    "font-size: 18px;"
)

# Set the textbox
textbox = QLineEdit()
textbox.move(20, 20)
textbox.setFixedWidth(500)
textbox.setStyleSheet(
    "margin:50px, 0;"
)

# Bytes label
lBytes = QLabel()
lBytes.resize(10, 10)
lBytes.setAlignment(QtCore.Qt.AlignCenter)
lBytes.setStyleSheet(
    "color: black;" +
    "font-size: 18px;"
)

# error label
error = QLabel()
error.resize(10, 10)
error.setAlignment(QtCore.Qt.AlignCenter)
error.setStyleSheet(
    "color: black;" +
    "font-size: 18px;"
)

# Set the button
dButton = QPushButton("DOWNLOAD")
dButton.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
dButton.setStyleSheet(
    "*{font-size: 25px;" +
    "color: 'black';" +
    "padding: 15px 0;" +
    "margin: 10px 20px;" +
    "border: 2px solid black;" +
    "border-radius: 20px;}"
    "*:hover{background:'blue'; color: white;}"
)

# Trigger the function
dButton.clicked.connect(on_dowload)

grid.addWidget(label, 0, 1)
grid.addWidget(textbox, 0, 1)
grid.addWidget(error, 1, 1)
grid.addWidget(dButton, 2, 1)

window.setLayout(grid)
window.show()
sys.exit(app.exec())


# # Set progress bar
# pBar = QProgressBar()
# pBar.move(20, 20)
# pBar.setFixedWidth(500)
