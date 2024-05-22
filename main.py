import sys
import numpy as np
import pyqtgraph as pg
import random
from PyQt5 import QtCore, QtGui, QtWidgets
import design
import EigenFreqCalculator as nf
import workfiles as rf

class App(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.exit.triggered.connect(sys.exit)
        self.connectSignals()
        self.initUI()

    def initUI(self):
        # Инициализация с загрузкой файлов
        self.loadFile(self.plainTextEdit, 'data/squant.init')
        self.loadFile(self.plainTextEdit_2, 'data/Layer.str')
        self.lineEdit_3.setText('data/squant.init')
        self.lineEdit_4.setText('data/Layer.str')

    def connectSignals(self):
        self.toolButton_3.clicked.connect(lambda: self.browseFile(self.plainTextEdit, self.lineEdit_3))
        self.lineEdit_3.editingFinished.connect(lambda: self.loadFile(self.plainTextEdit, self.lineEdit_3.text()))
        self.toolButton_savei.clicked.connect(lambda: self.saveFile(self.plainTextEdit, self.lineEdit_3.text()))

        self.toolButton_4.clicked.connect(lambda: self.browseFile(self.plainTextEdit_2, self.lineEdit_4))
        self.lineEdit_4.editingFinished.connect(lambda: self.loadFile(self.plainTextEdit_2, self.lineEdit_4.text()))
        self.toolButton_savel.clicked.connect(lambda: self.saveFile(self.plainTextEdit_2, self.lineEdit_4.text()))

        self.pushButton_click.clicked.connect(self.saveData)
        self.pushButton.clicked.connect(self.calculateEigen)
        self.pushButton_3.clicked.connect(self.calculateSpectra)
        self.pushButton_2.clicked.connect(self.plotResults)

    def browseFile(self, textEdit, lineEdit):
        file, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Select file", filter="All Files (*)")
        if file:
            lineEdit.setText(file)
            self.loadFile(textEdit, file)

    def loadFile(self, textEdit, filePath):
        try:
            with open(filePath, 'r') as file:
                textEdit.setText(file.read())
        except Exception as e:
            textEdit.setText(f"Error: {e}")

    def saveFile(self, textEdit, filePath):
        file, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Save file", filePath, filter="All Files (*)")
        if file:
            with open(file, 'w') as f:
                f.write(textEdit.toPlainText())

    def saveData(self):
        self.writeToFile(self.plainTextEdit.toPlainText(), "source/temp.init")
        self.writeToFile(self.plainTextEdit_2.toPlainText(), "source/temp.str")

    def writeToFile(self, content, path):
        try:
            with open(path, 'w') as file:
                file.write(content)
        except Exception as e:
            self.statusBar().showMessage(f"Failed to write file: {e}")

    def calculateSpectra(self):
        self.enableButtons(False)
        try:
            rall, tall, rsall, tsall, eigenfreq = nf.R(self.progressBar)
            self.updatePlot(self.graphicsView2, eigenfreq, rall, 'R', 'Energy', 'hw')
            self.updatePlot(self.graphicsView3, eigenfreq, tall, 'T', 'Energy', 'hw')
        finally:
            self.enableButtons(True)

    def calculateEigen(self):
        self.enableButtons(False)
        try:
            E0, El, r1, t1, rs1, ts1, Neigenfreq = nf.Ertef(self.progressBar)
            self.E1 = nf.profile(E0, El, r1, t1, rs1, ts1, Neigenfreq)
            self.Neigenfreq = Neigenfreq
            self.r1 = r1
            self.t1 = t1
            self.updateEigenList(E0, El, r1, t1, rs1, ts1, Neigenfreq)
        finally:
            self.enableButtons(True)

    def updatePlot(self, view, eigenfreq, values, ylabel, xlabel, units):
        view.clear()
        view.plot(eigenfreq, np.real(values)**2 + np.imag(values)**2, pen=pg.mkPen('r', width=2))
        view.setLabel('left', ylabel)
        view.setLabel('bottom', xlabel, units=units)
        view.showGrid(True, True)

    def updateEigenList(self, E0, El, r1, t1, rs1, ts1, Neigenfreq):
        self.plainTextEdit_3.clear()
        for i, freq in enumerate(Neigenfreq, start=1):
            item = QtGui.QListWidgetItem(f"({np.round(np.real(freq), 7)} , {np.round(np.imag(freq), 7)})")
            item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
            item.setCheckState(QtCore.Qt.Unchecked)
            self.plainTextEdit_3.addItem(item)

    def plotResults(self):
        self.graphicsView.clear()
        try:
            layer, friqrt, profile, inangle, hw0, hw1, hws, h_nm = rf.readin()
            NL, L, n = rf.readlayer(layer)
            for i in range(1, NL + 2):
                line = pg.InfiniteLine(sum(L[:i]), pen=pg.mkPen(color='b', width=1))
                self.graphicsView.addItem(line)
            for eg in range(self.plainTextEdit_3.count()):
                item = self.plainTextEdit_3.item(eg)
                if item.checkState() != QtCore.Qt.Unchecked:
                    color = QtGui.QColor(random.randint(20, 255), random.randint(20, 255), random.randint(20, 255))
                    name = item.text()
                    self.graphicsView.plot(self.E1[:, 0], self.E1[:, eg + 1], pen=pg.mkPen(color=color, width=2), name=name)
            self.graphicsView2.plot(np.real(self.Neigenfreq), np.real(self.r1)**2 + np.imag(self.r1)**2, pen=None, symbol='o')
            self.graphicsView3.plot(np.real(self.Neigenfreq), np.real(self.t1)**2 + np.imag(self.t1)**2, pen=None, symbol='o')
            self.graphicsView.setLabel('left', 'E')
            self.graphicsView.setLabel('bottom', 'Coordinates', units='nm')
            self.graphicsView.addLegend()
            self.graphicsView.showGrid(True, True)
        except Exception as e:
            self.statusBar().showMessage(f"Error plotting results: {e}")

    def enableButtons(self, enable):
        self.pushButton.setEnabled(enable)
        self.pushButton_2.setEnabled(enable)
        self.pushButton_3.setEnabled(enable)

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
