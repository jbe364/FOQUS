# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'flowsheet\dataBrowserFrame_UI.ui'
#
# Created: Fri May 20 13:18:30 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_dataBrowserWidget(object):
    def setupUi(self, dataBrowserWidget):
        dataBrowserWidget.setObjectName("dataBrowserWidget")
        dataBrowserWidget.resize(728, 551)
        self.verticalLayout_2 = QtGui.QVBoxLayout(dataBrowserWidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox_4 = QtGui.QGroupBox(dataBrowserWidget)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox_4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.menuButton = QtGui.QPushButton(self.groupBox_4)
        self.menuButton.setObjectName("menuButton")
        self.horizontalLayout.addWidget(self.menuButton)
        self.label = QtGui.QLabel(self.groupBox_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.filterSelectBox = QtGui.QComboBox(self.groupBox_4)
        self.filterSelectBox.setMinimumSize(QtCore.QSize(150, 0))
        self.filterSelectBox.setObjectName("filterSelectBox")
        self.filterSelectBox.addItem("")
        self.horizontalLayout.addWidget(self.filterSelectBox)
        self.editFiltersButton = QtGui.QPushButton(self.groupBox_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editFiltersButton.sizePolicy().hasHeightForWidth())
        self.editFiltersButton.setSizePolicy(sizePolicy)
        self.editFiltersButton.setObjectName("editFiltersButton")
        self.horizontalLayout.addWidget(self.editFiltersButton)
        self.columnsButton = QtGui.QPushButton(self.groupBox_4)
        self.columnsButton.setObjectName("columnsButton")
        self.horizontalLayout.addWidget(self.columnsButton)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_2 = QtGui.QLabel(self.groupBox_4)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.numRowsBox = QtGui.QLineEdit(self.groupBox_4)
        self.numRowsBox.setEnabled(True)
        self.numRowsBox.setMaximumSize(QtCore.QSize(100, 16777215))
        self.numRowsBox.setFrame(False)
        self.numRowsBox.setReadOnly(True)
        self.numRowsBox.setObjectName("numRowsBox")
        self.horizontalLayout.addWidget(self.numRowsBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tableView = QtGui.QTableView(self.groupBox_4)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(220, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        self.tableView.setPalette(palette)
        self.tableView.setObjectName("tableView")
        self.verticalLayout.addWidget(self.tableView)
        self.verticalLayout_2.addWidget(self.groupBox_4)
        self.label.setBuddy(self.filterSelectBox)
        self.label_2.setBuddy(self.numRowsBox)

        self.retranslateUi(dataBrowserWidget)
        QtCore.QMetaObject.connectSlotsByName(dataBrowserWidget)

    def retranslateUi(self, dataBrowserWidget):
        dataBrowserWidget.setWindowTitle(QtGui.QApplication.translate("dataBrowserWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_4.setTitle(QtGui.QApplication.translate("dataBrowserWidget", "Flowsheet Results", None, QtGui.QApplication.UnicodeUTF8))
        self.menuButton.setText(QtGui.QApplication.translate("dataBrowserWidget", "Menu", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("dataBrowserWidget", "Current Filter:", None, QtGui.QApplication.UnicodeUTF8))
        self.filterSelectBox.setItemText(0, QtGui.QApplication.translate("dataBrowserWidget", "None", None, QtGui.QApplication.UnicodeUTF8))
        self.editFiltersButton.setText(QtGui.QApplication.translate("dataBrowserWidget", "Edit Filters", None, QtGui.QApplication.UnicodeUTF8))
        self.columnsButton.setText(QtGui.QApplication.translate("dataBrowserWidget", "Columns", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("dataBrowserWidget", "Number of Rows:", None, QtGui.QApplication.UnicodeUTF8))

