import sys
from Design.design import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.QtGui import QPixmap


class Resize(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.btnChooseFile.clicked.connect(self.openImage)
        self.btnResize.clicked.connect(self.resizing)
        self.btnSave.clicked.connect(self.save)

    def openImage(self):
        image, _ = QFileDialog.getOpenFileName(
            self.centralwidget,
            'Open Image',
            '/Users/pebracard/Documents/Carreira/PyCharm/Curso Python 3/Design',
            options=QFileDialog.DontUseNativeDialog
        )
        self.inputFilePath.setText(image)
        self.originalImg = QPixmap(image)
        self.labelImg.setPixmap(self.originalImg)
        self.inputWidth.setText(str(self.originalImg.width()))
        self.inputHeight.setText(str(self.originalImg.height()))

    def resizing(self):
        width = int(self.inputWidth.text())
        self.newImage = self.originalImg.scaledToWidth(width)
        self.labelImg.setPixmap(self.newImage)
        self.inputWidth.setText(str(self.newImage.width()))
        self.inputHeight.setText(str(self.newImage.height()))

    def save(self):
        image, _ = QFileDialog.getSaveFileName(
            self.centralwidget,
            'Save Image',
            '/Users/pebracard/Desktop',
            options=QFileDialog.DontUseNativeDialog
        )
        self.newImage.save(image, 'PNG')




if __name__ == '__main__':
    qt = QApplication(sys.argv)
    resize = Resize()
    resize.show()
    qt.exec()