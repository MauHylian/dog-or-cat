from MainWindow import *
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QPixmap

import os
from model.predict import predict

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        self.buttonCargar.clicked.connect(self.load)
        self.buttonPredecir.clicked.connect(self.predict)

        self.labelPath.setText('Imagen')
        self.labelPrediccion.setText('')
        self.progressBar.setRange(0, 100)
        self.progressBar.setValue(0)

        self.lastDirectory = None

    def load(self):
        directory = os.path.abspath(__file__)
        if self.lastDirectory:
            directory = self.lastDirectory

        fname = QFileDialog.getOpenFileName(self, 'Abrir imagen', directory, 'Image files (*.jpg *.png)')

        path = fname[0]
        self.currentImagePath = path
        self.lastDirectory = os.path.dirname(path)
        self.labelPath.setText(path)

        view = self.view

        scene = QtWidgets.QGraphicsScene()
        image = QPixmap(path)

        scene.addItem(QtWidgets.QGraphicsPixmapItem(image))

        view.setRenderHint(QtGui.QPainter.Antialiasing) 
        view.setScene(scene)

        self.progressBar.setValue(0)
        self.labelPrediccion.setText('')

    def predict(self):
        result = predict(self.currentImagePath)
        for i in range(101):
            self.progressBar.setValue(i)

        if not result:
            result = 'Error'
        self.labelPrediccion.setText(result)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
