# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'flowsheet\flowsheetSettingsDialog_UI.ui'
#
# Created: Mon Apr 14 15:52:42 2014
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_flowsheetSettingsDialog(object):
    def setupUi(self, flowsheetSettingsDialog):
        flowsheetSettingsDialog.setObjectName("flowsheetSettingsDialog")
        flowsheetSettingsDialog.resize(548, 319)
        self.verticalLayout_5 = QtGui.QVBoxLayout(flowsheetSettingsDialog)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.tabWidget = QtGui.QTabWidget(flowsheetSettingsDialog)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtGui.QLabel(self.tab)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.tearSolverBox = QtGui.QComboBox(self.tab)
        self.tearSolverBox.setObjectName("tearSolverBox")
        self.tearSolverBox.addItem("")
        self.tearSolverBox.addItem("")
        self.horizontalLayout_3.addWidget(self.tearSolverBox)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.tearFracTolRadioButton = QtGui.QRadioButton(self.tab)
        self.tearFracTolRadioButton.setObjectName("tearFracTolRadioButton")
        self.gridLayout.addWidget(self.tearFracTolRadioButton, 1, 3, 1, 1)
        self.tearItLimitEdit = QtGui.QLineEdit(self.tab)
        self.tearItLimitEdit.setMaximumSize(QtCore.QSize(100, 16777215))
        self.tearItLimitEdit.setObjectName("tearItLimitEdit")
        self.gridLayout.addWidget(self.tearItLimitEdit, 2, 1, 1, 1)
        self.tearTolEdit = QtGui.QLineEdit(self.tab)
        self.tearTolEdit.setMaximumSize(QtCore.QSize(100, 16777215))
        self.tearTolEdit.setObjectName("tearTolEdit")
        self.gridLayout.addWidget(self.tearTolEdit, 1, 1, 1, 1)
        self.tearAbsTolRadioButton = QtGui.QRadioButton(self.tab)
        self.tearAbsTolRadioButton.setChecked(True)
        self.tearAbsTolRadioButton.setObjectName("tearAbsTolRadioButton")
        self.gridLayout.addWidget(self.tearAbsTolRadioButton, 1, 2, 1, 1)
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.label = QtGui.QLabel(self.tab)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 4, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.groupBox_2 = QtGui.QGroupBox(self.tab)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtGui.QLabel(self.groupBox_2)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        spacerItem2 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.label_6 = QtGui.QLabel(self.groupBox_2)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.wegAccMinEdit = QtGui.QLineEdit(self.groupBox_2)
        self.wegAccMinEdit.setMaximumSize(QtCore.QSize(75, 16777215))
        self.wegAccMinEdit.setObjectName("wegAccMinEdit")
        self.horizontalLayout_5.addWidget(self.wegAccMinEdit)
        spacerItem3 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.label_7 = QtGui.QLabel(self.groupBox_2)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_5.addWidget(self.label_7)
        self.wegAccMaxEdit = QtGui.QLineEdit(self.groupBox_2)
        self.wegAccMaxEdit.setMaximumSize(QtCore.QSize(75, 16777215))
        self.wegAccMaxEdit.setObjectName("wegAccMaxEdit")
        self.horizontalLayout_5.addWidget(self.wegAccMaxEdit)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.verticalLayout.addWidget(self.groupBox_2)
        spacerItem5 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_4 = QtGui.QLabel(self.tab_2)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.staggerTimeEdit = QtGui.QLineEdit(self.tab_2)
        self.staggerTimeEdit.setObjectName("staggerTimeEdit")
        self.horizontalLayout.addWidget(self.staggerTimeEdit)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        spacerItem7 = QtGui.QSpacerItem(20, 194, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem7)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout_5.addWidget(self.tabWidget)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.okayButton = QtGui.QPushButton(flowsheetSettingsDialog)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/check.svg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.okayButton.setIcon(icon)
        self.okayButton.setObjectName("okayButton")
        self.horizontalLayout_6.addWidget(self.okayButton)
        self.cancelButton = QtGui.QPushButton(flowsheetSettingsDialog)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/delete.svg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.cancelButton.setIcon(icon1)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout_6.addWidget(self.cancelButton)
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem8)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        self.label_3.setBuddy(self.tearSolverBox)
        self.label_2.setBuddy(self.tearItLimitEdit)
        self.label.setBuddy(self.tearTolEdit)
        self.label_6.setBuddy(self.wegAccMinEdit)
        self.label_7.setBuddy(self.wegAccMaxEdit)
        self.label_4.setBuddy(self.staggerTimeEdit)

        self.retranslateUi(flowsheetSettingsDialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(flowsheetSettingsDialog)

    def retranslateUi(self, flowsheetSettingsDialog):
        flowsheetSettingsDialog.setWindowTitle(QtGui.QApplication.translate("flowsheetSettingsDialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("flowsheetSettingsDialog", "Default Solver:", None, QtGui.QApplication.UnicodeUTF8))
        self.tearSolverBox.setItemText(0, QtGui.QApplication.translate("flowsheetSettingsDialog", "Wegstein", None, QtGui.QApplication.UnicodeUTF8))
        self.tearSolverBox.setItemText(1, QtGui.QApplication.translate("flowsheetSettingsDialog", "Direct", None, QtGui.QApplication.UnicodeUTF8))
        self.tearFracTolRadioButton.setText(QtGui.QApplication.translate("flowsheetSettingsDialog", "Fraction of Range", None, QtGui.QApplication.UnicodeUTF8))
        self.tearAbsTolRadioButton.setText(QtGui.QApplication.translate("flowsheetSettingsDialog", "Absolute", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("flowsheetSettingsDialog", "Iteration Limit:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("flowsheetSettingsDialog", "Tolerance:", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("flowsheetSettingsDialog", "Wegstein", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("flowsheetSettingsDialog", "Acceleration Parameter", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("flowsheetSettingsDialog", "Min:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("flowsheetSettingsDialog", "Max:", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("flowsheetSettingsDialog", "Tear Solvers", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("flowsheetSettingsDialog", "Maximum Stagger Start Time: ", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("flowsheetSettingsDialog", "Turbine", None, QtGui.QApplication.UnicodeUTF8))
        self.okayButton.setText(QtGui.QApplication.translate("flowsheetSettingsDialog", "Okay", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelButton.setText(QtGui.QApplication.translate("flowsheetSettingsDialog", "Cancel", None, QtGui.QApplication.UnicodeUTF8))

import foqus_lib.gui.icons_rc as icons_rc
