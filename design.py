# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rbot.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph as pg

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1051, 673)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("source/icons8_open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("source/diskette.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        
        
        self.splitter_all = QtWidgets.QSplitter(self.splitter)
        self.splitter_all.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_all.setObjectName("splitter_all")
        
        
        self.splitter_data = QtWidgets.QSplitter(self.splitter_all)
        self.splitter_data.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_data.setObjectName("splitter_data")
        
        
        self.splitter_in = QtWidgets.QSplitter(self.splitter_data)
        self.splitter_in.setOrientation(QtCore.Qt.Vertical)
        self.splitter_in.setObjectName("splitter_in")
        

        self.gp_init = QtWidgets.QGroupBox(self.splitter_in)
        self.gp_init.setObjectName("gp_init")
        self.verticalLayout_init = QtWidgets.QVBoxLayout(self.gp_init)
        self.verticalLayout_init.setObjectName("verticalLayout_init")
        self.label_2 = QtWidgets.QLabel(self.gp_init)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_init.addWidget(self.label_2)
        
        # window init
        self.plainTextEdit = QtWidgets.QTextEdit(self.gp_init)
        self.plainTextEdit.setObjectName("plainTextEdit")
        
        self.verticalLayout_init.addWidget(self.plainTextEdit)
        
        
        self.splitter_open_init = QtWidgets.QSplitter(self.gp_init)
        self.splitter_open_init.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_open_init.setObjectName("splitter_open_init")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.splitter_open_init)
        self.lineEdit_3.setObjectName("lineEdit_3")
        
        self.toolButton_3 = QtWidgets.QToolButton(self.splitter_open_init)
        self.toolButton_3.setIcon(icon)
        self.toolButton_3.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolButton_3.setObjectName("toolButton_3")
        
        self.toolButton_savei = QtWidgets.QToolButton(self.splitter_open_init)
        self.toolButton_savei.setIcon(icon2)
        self.toolButton_savei.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolButton_savei.setObjectName("toolButton_savei")
        
        self.verticalLayout_init.addWidget(self.splitter_open_init)

        self.gp_layer = QtWidgets.QGroupBox(self.splitter_in)
        self.gp_layer.setObjectName("gp_layer")
        self.verticalLayout_layer = QtWidgets.QVBoxLayout(self.gp_layer)
        self.verticalLayout_layer.setObjectName("verticalLayout_layer")
        self.label = QtWidgets.QLabel(self.gp_layer)
        self.label.setObjectName("label")
        self.verticalLayout_layer.addWidget(self.label)
        
        # layer window
        self.plainTextEdit_2 = QtWidgets.QTextEdit(self.gp_layer)
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.verticalLayout_layer.addWidget(self.plainTextEdit_2)
        

        self.splitter_open_layer = QtWidgets.QSplitter(self.gp_layer)
        self.splitter_open_layer.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_open_layer.setObjectName("splitter_open_layer")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.splitter_open_layer)
        self.lineEdit_4.setObjectName("lineEdit_4")
        
        self.toolButton_4 = QtWidgets.QToolButton(self.splitter_open_layer)
        self.toolButton_4.setIcon(icon)
        self.toolButton_4.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolButton_4.setObjectName("toolButton_4")
        
        self.toolButton_savel = QtWidgets.QToolButton(self.splitter_open_layer)
        self.toolButton_savel.setIcon(icon2)
        self.toolButton_savel.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolButton_savel.setObjectName("toolButton_savel")
        self.verticalLayout_layer.addWidget(self.splitter_open_layer)
        
        self.bp_out = QtWidgets.QGroupBox(self.splitter_data)
        self.bp_out.setObjectName("bp_out")
        
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.bp_out)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        
        
        self.pushButton_click = QtWidgets.QPushButton(self.bp_out)
        self.pushButton_click.setObjectName("pushButton_click")
        self.verticalLayout.addWidget(self.pushButton_click)
        
        # eigen freq
        self.pushButton = QtWidgets.QPushButton(self.bp_out)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        
        # spectra
        self.pushButton_3 = QtWidgets.QPushButton(self.bp_out)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        
        self.verticalLayout_4.addLayout(self.verticalLayout)
        
        self.splitter_set = QtWidgets.QSplitter(self.bp_out)
        self.splitter_set.setOrientation(QtCore.Qt.Vertical)
        self.splitter_set.setObjectName("splitter_set")
        
        # set 1        
        self.bp_set1 = QtWidgets.QGroupBox(self.splitter_set)
        self.bp_set1.setObjectName("bp_set1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.bp_set1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.bp_set1)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        

        self.plainTextEdit_3 = QtWidgets.QListWidget(self.bp_set1)
        self.plainTextEdit_3.setObjectName("plainTextEdit_3")
        self.verticalLayout_3.addWidget(self.plainTextEdit_3)

        # set 2        
        self.bp_set2 = QtWidgets.QGroupBox(self.splitter_set)
        self.bp_set2.setObjectName("bp_set2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.bp_set2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.bp_set2)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        

        self.plainTextEdit_4 = QtWidgets.QListWidget(self.bp_set2)
        self.plainTextEdit_4.setObjectName("plainTextEdit_4")
        self.verticalLayout_2.addWidget(self.plainTextEdit_4)
        
        self.verticalLayout_4.addWidget(self.splitter_set)
        
        self.verticalLayout_plot = QtWidgets.QVBoxLayout()
        self.verticalLayout_plot.setObjectName("verticalLayout_plot")
        
        self.pushButton_2 = QtWidgets.QPushButton(self.bp_out)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_plot.addWidget(self.pushButton_2)
        
        self.verticalLayout_4.addLayout(self.verticalLayout_plot)  
        
        
        # visual           
        self.widget = QtWidgets.QWidget(self.splitter)
        self.widget.setObjectName("widget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        

        self.tabWidget_data_vis = QtWidgets.QTabWidget(self.widget)
        self.tabWidget_data_vis.setObjectName("tabWidget_data_vis")


        # profiles
        self.Graph = QtWidgets.QWidget()
        self.Graph.setObjectName("Graph")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.Graph)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.graphicsView = pg.PlotWidget(self.Graph, background='w')
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout_5.addWidget(self.graphicsView)
        self.tabWidget_data_vis.addTab(self.Graph, "")
        
        # reflection 1
        self.reflection1 = QtWidgets.QWidget()
        self.reflection1.setObjectName("reflection1")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.reflection1)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.graphicsView2 = pg.PlotWidget(self.reflection1, background='w')
        self.graphicsView2.setObjectName("graphicsView2")
        self.verticalLayout_7.addWidget(self.graphicsView2)
        self.tabWidget_data_vis.addTab(self.reflection1, "")
        
        # Transmission 1
        self.Transmission1 = QtWidgets.QWidget()
        self.Transmission1.setObjectName("Transmission1")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.Transmission1)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.graphicsView3 = pg.PlotWidget(self.Transmission1, background='w')
        self.graphicsView3.setObjectName("graphicsView3")
        self.verticalLayout_8.addWidget(self.graphicsView3)
        self.tabWidget_data_vis.addTab(self.Transmission1, "")
        

        
        self.verticalLayout_6.addWidget(self.tabWidget_data_vis)
        self.progressBar = QtWidgets.QProgressBar(self.widget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_6.addWidget(self.progressBar)
        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)
        
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1051, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.exit = QtWidgets.QAction(MainWindow)
        self.exit.setObjectName("exit")
        self.action_Rbot_Optimizer = QtWidgets.QAction(MainWindow)
        self.action_Rbot_Optimizer.setObjectName("action_Rbot_Optimizer")
        self.menu.addAction(self.exit)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget_data_vis.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "init"))
        self.toolButton_3.setText(_translate("MainWindow", "Open"))
        self.toolButton_savei.setText(_translate("MainWindow", "Save"))        
        self.label.setText(_translate("MainWindow", "Layers"))
        self.toolButton_4.setText(_translate("MainWindow", " Open"))
        self.toolButton_savel.setText(_translate("MainWindow", "Save"))
        self.pushButton_click.setText(_translate("MainWindow", "Apply changes"))
        self.pushButton.setText(_translate("MainWindow", "Calculate Eigenenergies"))
        self.pushButton_3.setText(_translate("MainWindow", "Calculate Reflection and Transmission"))
        self.label_3.setText(_translate("MainWindow", "Eigenenergies set 1"))
        self.label_4.setText(_translate("MainWindow", "Eigenenergies set 2"))
        self.pushButton_2.setText(_translate("MainWindow", "Plot profile"))
        
        self.tabWidget_data_vis.setTabText(self.tabWidget_data_vis.indexOf(self.Graph), _translate("MainWindow", "Profiles"))
        self.tabWidget_data_vis.setTabText(self.tabWidget_data_vis.indexOf(self.reflection1), _translate("MainWindow", "Reflection"))
        self.tabWidget_data_vis.setTabText(self.tabWidget_data_vis.indexOf(self.Transmission1), _translate("MainWindow", "Transmission"))

        
        self.menu.setTitle(_translate("MainWindow", "Menu"))
        self.exit.setText(_translate("MainWindow", "Exit"))
        

from pyqtgraph import GraphicsLayoutWidget

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

