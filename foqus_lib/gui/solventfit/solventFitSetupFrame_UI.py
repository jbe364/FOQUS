# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'solventFitSetupFrame.ui'
#
# Created: Thu Apr 21 17:22:38 2016
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(995, 969)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setWeight(50)
        font.setBold(False)
        Frame.setFont(font)
        Frame.setFrameShape(QtGui.QFrame.StyledPanel)
        Frame.setFrameShadow(QtGui.QFrame.Raised)
        self.gridLayout_8 = QtGui.QGridLayout(Frame)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.groupBox_4 = QtGui.QGroupBox(Frame)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_4 = QtGui.QGridLayout(self.groupBox_4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.loadTrainingData_button = QtGui.QPushButton(self.groupBox_4)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.loadTrainingData_button.setFont(font)
        self.loadTrainingData_button.setObjectName("loadTrainingData_button")
        self.gridLayout_4.addWidget(self.loadTrainingData_button, 1, 0, 1, 1)
        self.trainingFile_edit = QtGui.QLineEdit(self.groupBox_4)
        self.trainingFile_edit.setMinimumSize(QtCore.QSize(500, 0))
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.trainingFile_edit.setFont(font)
        self.trainingFile_edit.setReadOnly(True)
        self.trainingFile_edit.setObjectName("trainingFile_edit")
        self.gridLayout_4.addWidget(self.trainingFile_edit, 1, 1, 1, 2)
        self.newAnalysis_radio = QtGui.QRadioButton(self.groupBox_4)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.newAnalysis_radio.setFont(font)
        self.newAnalysis_radio.setChecked(True)
        self.newAnalysis_radio.setObjectName("newAnalysis_radio")
        self.gridLayout_4.addWidget(self.newAnalysis_radio, 0, 0, 1, 1)
        self.restart_radio = QtGui.QRadioButton(self.groupBox_4)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.restart_radio.setFont(font)
        self.restart_radio.setObjectName("restart_radio")
        self.gridLayout_4.addWidget(self.restart_radio, 0, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem, 1, 3, 1, 1)
        self.gridLayout_8.addWidget(self.groupBox_4, 0, 0, 1, 2)
        self.output_groupBox = QtGui.QGroupBox(Frame)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.output_groupBox.setFont(font)
        self.output_groupBox.setObjectName("output_groupBox")
        self.gridLayout_2 = QtGui.QGridLayout(self.output_groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.outputInstruction = QtGui.QLabel(self.output_groupBox)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.outputInstruction.setFont(font)
        self.outputInstruction.setWordWrap(True)
        self.outputInstruction.setObjectName("outputInstruction")
        self.gridLayout_2.addWidget(self.outputInstruction, 0, 0, 1, 1)
        self.output_table = QtGui.QTableWidget(self.output_groupBox)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.output_table.setFont(font)
        self.output_table.setObjectName("output_table")
        self.output_table.setColumnCount(7)
        self.output_table.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.output_table.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.output_table.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.output_table.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.output_table.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.output_table.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.output_table.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.output_table.setHorizontalHeaderItem(6, item)
        self.gridLayout_2.addWidget(self.output_table, 1, 0, 1, 1)
        self.gridLayout_8.addWidget(self.output_groupBox, 1, 0, 1, 1)
        self.input_groupBox = QtGui.QGroupBox(Frame)
        self.input_groupBox.setMinimumSize(QtCore.QSize(500, 0))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.input_groupBox.setFont(font)
        self.input_groupBox.setObjectName("input_groupBox")
        self.gridLayout = QtGui.QGridLayout(self.input_groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.inputPrior_table = InputPriorTable(self.input_groupBox)
        self.inputPrior_table.setMinimumSize(QtCore.QSize(0, 150))
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.inputPrior_table.setFont(font)
        self.inputPrior_table.setObjectName("inputPrior_table")
        self.inputPrior_table.setColumnCount(9)
        self.inputPrior_table.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.inputPrior_table.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.inputPrior_table.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.inputPrior_table.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.inputPrior_table.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.inputPrior_table.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.inputPrior_table.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.inputPrior_table.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.inputPrior_table.setHorizontalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.inputPrior_table.setHorizontalHeaderItem(8, item)
        self.gridLayout.addWidget(self.inputPrior_table, 1, 0, 1, 1)
        self.inputInstruction = QtGui.QLabel(self.input_groupBox)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.inputInstruction.setFont(font)
        self.inputInstruction.setWordWrap(True)
        self.inputInstruction.setObjectName("inputInstruction")
        self.gridLayout.addWidget(self.inputInstruction, 0, 0, 1, 1)
        self.gridLayout_8.addWidget(self.input_groupBox, 1, 1, 1, 1)
        self.obs_groupBox = QtGui.QGroupBox(Frame)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.obs_groupBox.setFont(font)
        self.obs_groupBox.setObjectName("obs_groupBox")
        self.gridLayout_3 = QtGui.QGridLayout(self.obs_groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.numExperiments_static = QtGui.QLabel(self.obs_groupBox)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.numExperiments_static.setFont(font)
        self.numExperiments_static.setObjectName("numExperiments_static")
        self.horizontalLayout.addWidget(self.numExperiments_static)
        self.numExperiments_spin = QtGui.QSpinBox(self.obs_groupBox)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.numExperiments_spin.setFont(font)
        self.numExperiments_spin.setMinimum(1)
        self.numExperiments_spin.setMaximum(999999999)
        self.numExperiments_spin.setObjectName("numExperiments_spin")
        self.horizontalLayout.addWidget(self.numExperiments_spin)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.loadObs_button = QtGui.QPushButton(self.obs_groupBox)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.loadObs_button.setFont(font)
        self.loadObs_button.setObjectName("loadObs_button")
        self.horizontalLayout.addWidget(self.loadObs_button)
        self.saveObs_button = QtGui.QPushButton(self.obs_groupBox)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.saveObs_button.setFont(font)
        self.saveObs_button.setObjectName("saveObs_button")
        self.horizontalLayout.addWidget(self.saveObs_button)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.gridLayout_3.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.obsInstruction = QtGui.QLabel(self.obs_groupBox)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.obsInstruction.setFont(font)
        self.obsInstruction.setWordWrap(True)
        self.obsInstruction.setObjectName("obsInstruction")
        self.gridLayout_3.addWidget(self.obsInstruction, 1, 0, 1, 1)
        self.obs_table = QtGui.QTableWidget(self.obs_groupBox)
        self.obs_table.setMaximumSize(QtCore.QSize(16777215, 150))
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.obs_table.setFont(font)
        self.obs_table.setObjectName("obs_table")
        self.obs_table.setColumnCount(6)
        self.obs_table.setRowCount(2)
        item = QtGui.QTableWidgetItem()
        self.obs_table.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.obs_table.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.obs_table.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.obs_table.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.obs_table.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.obs_table.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.obs_table.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.obs_table.setHorizontalHeaderItem(5, item)
        self.gridLayout_3.addWidget(self.obs_table, 2, 0, 1, 1)
        self.gridLayout_8.addWidget(self.obs_groupBox, 2, 0, 1, 2)
        self.saveInstruction = QtGui.QLabel(Frame)
        self.saveInstruction.setObjectName("saveInstruction")
        self.gridLayout_8.addWidget(self.saveInstruction, 3, 0, 1, 2)
        self.gridLayout_5 = QtGui.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.horizontalLayout_infSave = QtGui.QHBoxLayout()
        self.horizontalLayout_infSave.setObjectName("horizontalLayout_infSave")
        self.infSave_chkbox = QtGui.QCheckBox(Frame)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.infSave_chkbox.setFont(font)
        self.infSave_chkbox.setMouseTracking(False)
        self.infSave_chkbox.setObjectName("infSave_chkbox")
        self.horizontalLayout_infSave.addWidget(self.infSave_chkbox)
        self.infSave_edit = QtGui.QLineEdit(Frame)
        self.infSave_edit.setReadOnly(True)
        self.infSave_edit.setObjectName("infSave_edit")
        self.horizontalLayout_infSave.addWidget(self.infSave_edit)
        self.infSave_button = QtGui.QPushButton(Frame)
        self.infSave_button.setObjectName("infSave_button")
        self.horizontalLayout_infSave.addWidget(self.infSave_button)
        self.gridLayout_5.addLayout(self.horizontalLayout_infSave, 0, 0, 1, 1)
        self.horizontalLayout_infSave_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_infSave_2.setObjectName("horizontalLayout_infSave_2")
        self.rdsSave_chkbox = QtGui.QCheckBox(Frame)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.rdsSave_chkbox.setFont(font)
        self.rdsSave_chkbox.setMouseTracking(False)
        self.rdsSave_chkbox.setObjectName("rdsSave_chkbox")
        self.horizontalLayout_infSave_2.addWidget(self.rdsSave_chkbox)
        self.rdsSave_edit = QtGui.QLineEdit(Frame)
        self.rdsSave_edit.setReadOnly(True)
        self.rdsSave_edit.setObjectName("rdsSave_edit")
        self.horizontalLayout_infSave_2.addWidget(self.rdsSave_edit)
        self.rdsSave_button = QtGui.QPushButton(Frame)
        self.rdsSave_button.setObjectName("rdsSave_button")
        self.horizontalLayout_infSave_2.addWidget(self.rdsSave_button)
        self.gridLayout_5.addLayout(self.horizontalLayout_infSave_2, 1, 0, 1, 1)
        self.horizontalLayout_discrepancySave = QtGui.QHBoxLayout()
        self.horizontalLayout_discrepancySave.setObjectName("horizontalLayout_discrepancySave")
        self.discrepancy_chkbox = QtGui.QCheckBox(Frame)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setWeight(50)
        font.setBold(False)
        self.discrepancy_chkbox.setFont(font)
        self.discrepancy_chkbox.setObjectName("discrepancy_chkbox")
        self.horizontalLayout_discrepancySave.addWidget(self.discrepancy_chkbox)
        self.discrepancySave_chkbox = QtGui.QCheckBox(Frame)
        self.discrepancySave_chkbox.setMinimumSize(QtCore.QSize(190, 0))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.discrepancySave_chkbox.setFont(font)
        self.discrepancySave_chkbox.setMouseTracking(False)
        self.discrepancySave_chkbox.setObjectName("discrepancySave_chkbox")
        self.horizontalLayout_discrepancySave.addWidget(self.discrepancySave_chkbox)
        self.discrepancySave_edit = QtGui.QLineEdit(Frame)
        self.discrepancySave_edit.setMinimumSize(QtCore.QSize(100, 0))
        self.discrepancySave_edit.setReadOnly(True)
        self.discrepancySave_edit.setObjectName("discrepancySave_edit")
        self.horizontalLayout_discrepancySave.addWidget(self.discrepancySave_edit)
        self.discrepancySave_button = QtGui.QPushButton(Frame)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.discrepancySave_button.setFont(font)
        self.discrepancySave_button.setObjectName("discrepancySave_button")
        self.horizontalLayout_discrepancySave.addWidget(self.discrepancySave_button)
        self.gridLayout_5.addLayout(self.horizontalLayout_discrepancySave, 2, 0, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout_5, 4, 0, 1, 2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.numIterStatic = QtGui.QLabel(Frame)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.numIterStatic.setFont(font)
        self.numIterStatic.setObjectName("numIterStatic")
        self.horizontalLayout_3.addWidget(self.numIterStatic)
        self.gridLayout_6 = QtGui.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.numIterCalibStatic = QtGui.QLabel(Frame)
        self.numIterCalibStatic.setObjectName("numIterCalibStatic")
        self.gridLayout_6.addWidget(self.numIterCalibStatic, 0, 0, 1, 1)
        self.numIterCalibSpin = QtGui.QSpinBox(Frame)
        self.numIterCalibSpin.setMinimum(10)
        self.numIterCalibSpin.setMaximum(1000000000)
        self.numIterCalibSpin.setProperty("value", 50000)
        self.numIterCalibSpin.setObjectName("numIterCalibSpin")
        self.gridLayout_6.addWidget(self.numIterCalibSpin, 0, 1, 1, 1)
        self.numIterEmulStatic = QtGui.QLabel(Frame)
        self.numIterEmulStatic.setObjectName("numIterEmulStatic")
        self.gridLayout_6.addWidget(self.numIterEmulStatic, 1, 0, 1, 1)
        self.numIterEmulSpin = QtGui.QSpinBox(Frame)
        self.numIterEmulSpin.setMinimum(10)
        self.numIterEmulSpin.setMaximum(1000000000)
        self.numIterEmulSpin.setProperty("value", 10000)
        self.numIterEmulSpin.setObjectName("numIterEmulSpin")
        self.gridLayout_6.addWidget(self.numIterEmulSpin, 1, 1, 1, 1)
        self.horizontalLayout_3.addLayout(self.gridLayout_6)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.burnInStatic = QtGui.QLabel(Frame)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.burnInStatic.setFont(font)
        self.burnInStatic.setObjectName("burnInStatic")
        self.horizontalLayout_3.addWidget(self.burnInStatic)
        self.gridLayout_7 = QtGui.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.numBurnInCalibStatic = QtGui.QLabel(Frame)
        self.numBurnInCalibStatic.setObjectName("numBurnInCalibStatic")
        self.gridLayout_7.addWidget(self.numBurnInCalibStatic, 0, 0, 1, 1)
        self.numBurnInCalibSpin = QtGui.QSpinBox(Frame)
        self.numBurnInCalibSpin.setMinimum(0)
        self.numBurnInCalibSpin.setMaximum(1000000000)
        self.numBurnInCalibSpin.setProperty("value", 0)
        self.numBurnInCalibSpin.setObjectName("numBurnInCalibSpin")
        self.gridLayout_7.addWidget(self.numBurnInCalibSpin, 0, 1, 1, 1)
        self.numBurnInEmulStatic = QtGui.QLabel(Frame)
        self.numBurnInEmulStatic.setObjectName("numBurnInEmulStatic")
        self.gridLayout_7.addWidget(self.numBurnInEmulStatic, 1, 0, 1, 1)
        self.numBurnInEmulSpin = QtGui.QSpinBox(Frame)
        self.numBurnInEmulSpin.setMinimum(0)
        self.numBurnInEmulSpin.setMaximum(1000000000)
        self.numBurnInEmulSpin.setProperty("value", 0)
        self.numBurnInEmulSpin.setObjectName("numBurnInEmulSpin")
        self.gridLayout_7.addWidget(self.numBurnInEmulSpin, 1, 1, 1, 1)
        self.horizontalLayout_3.addLayout(self.gridLayout_7)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.gridLayout_8.addLayout(self.horizontalLayout_3, 5, 0, 1, 2)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem6 = QtGui.QSpacerItem(351, 25, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.inferInstruction = QtGui.QLabel(Frame)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.inferInstruction.setFont(font)
        self.inferInstruction.setObjectName("inferInstruction")
        self.horizontalLayout_2.addWidget(self.inferInstruction)
        self.inf_button = QtGui.QPushButton(Frame)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.inf_button.setFont(font)
        self.inf_button.setObjectName("inf_button")
        self.horizontalLayout_2.addWidget(self.inf_button)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        self.replotInstruction = QtGui.QLabel(Frame)
        self.replotInstruction.setMinimumSize(QtCore.QSize(450, 0))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.replotInstruction.setFont(font)
        self.replotInstruction.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.replotInstruction.setWordWrap(True)
        self.replotInstruction.setObjectName("replotInstruction")
        self.horizontalLayout_2.addWidget(self.replotInstruction)
        self.replot_button = QtGui.QPushButton(Frame)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.replot_button.setFont(font)
        self.replot_button.setObjectName("replot_button")
        self.horizontalLayout_2.addWidget(self.replot_button)
        spacerItem8 = QtGui.QSpacerItem(351, 25, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem8)
        self.gridLayout_8.addLayout(self.horizontalLayout_2, 6, 0, 1, 2)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QtGui.QApplication.translate("Frame", "Frame", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_4.setTitle(QtGui.QApplication.translate("Frame", "Start", None, QtGui.QApplication.UnicodeUTF8))
        self.loadTrainingData_button.setText(QtGui.QApplication.translate("Frame", "Load Training Data...", None, QtGui.QApplication.UnicodeUTF8))
        self.newAnalysis_radio.setText(QtGui.QApplication.translate("Frame", "New Analysis", None, QtGui.QApplication.UnicodeUTF8))
        self.restart_radio.setText(QtGui.QApplication.translate("Frame", "Restart", None, QtGui.QApplication.UnicodeUTF8))
        self.output_groupBox.setTitle(QtGui.QApplication.translate("Frame", "Output Settings:", None, QtGui.QApplication.UnicodeUTF8))
        self.outputInstruction.setText(QtGui.QApplication.translate("Frame", "1. Select the outputs that have been observed. (Distribution is assumed to be known through experiment or expert knowledge.) \n"
"2. For the observed outputs, select the response surface type. (Solvent Fit requires Solvent Fit Emulator)", None, QtGui.QApplication.UnicodeUTF8))
        self.output_table.setToolTip(QtGui.QApplication.translate("Frame", "Designate a response surface for each observed output.", None, QtGui.QApplication.UnicodeUTF8))
        self.output_table.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("Frame", "Observed?", None, QtGui.QApplication.UnicodeUTF8))
        self.output_table.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("Frame", "Output Name", None, QtGui.QApplication.UnicodeUTF8))
        self.output_table.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("Frame", "Response Surface", None, QtGui.QApplication.UnicodeUTF8))
        self.output_table.horizontalHeaderItem(3).setText(QtGui.QApplication.translate("Frame", "(cont\'d)", None, QtGui.QApplication.UnicodeUTF8))
        self.output_table.horizontalHeaderItem(4).setText(QtGui.QApplication.translate("Frame", "Legendre Order", None, QtGui.QApplication.UnicodeUTF8))
        self.output_table.horizontalHeaderItem(5).setText(QtGui.QApplication.translate("Frame", "MARS # Basis Func\'s", None, QtGui.QApplication.UnicodeUTF8))
        self.output_table.horizontalHeaderItem(6).setText(QtGui.QApplication.translate("Frame", "MARS Deg. of Interaction", None, QtGui.QApplication.UnicodeUTF8))
        self.input_groupBox.setTitle(QtGui.QApplication.translate("Frame", "Input Settings:", None, QtGui.QApplication.UnicodeUTF8))
        self.inputPrior_table.setToolTip(QtGui.QApplication.translate("Frame", "Designate input type:\n"
"Variable for uncertain inputs\n"
"Fixed for deterministic inputs\n"
"Design for control inputs that can vary from experiments", None, QtGui.QApplication.UnicodeUTF8))
        self.inputPrior_table.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("Frame", "Input Name", None, QtGui.QApplication.UnicodeUTF8))
        self.inputPrior_table.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("Frame", "Type", None, QtGui.QApplication.UnicodeUTF8))
        self.inputPrior_table.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("Frame", "Display?", None, QtGui.QApplication.UnicodeUTF8))
        self.inputPrior_table.horizontalHeaderItem(3).setText(QtGui.QApplication.translate("Frame", "Fixed Value", None, QtGui.QApplication.UnicodeUTF8))
        self.inputPrior_table.horizontalHeaderItem(4).setText(QtGui.QApplication.translate("Frame", "PDF", None, QtGui.QApplication.UnicodeUTF8))
        self.inputPrior_table.horizontalHeaderItem(5).setText(QtGui.QApplication.translate("Frame", "PDF Param1", None, QtGui.QApplication.UnicodeUTF8))
        self.inputPrior_table.horizontalHeaderItem(6).setText(QtGui.QApplication.translate("Frame", "PDF Param2", None, QtGui.QApplication.UnicodeUTF8))
        self.inputPrior_table.horizontalHeaderItem(7).setText(QtGui.QApplication.translate("Frame", "Min", None, QtGui.QApplication.UnicodeUTF8))
        self.inputPrior_table.horizontalHeaderItem(8).setText(QtGui.QApplication.translate("Frame", "Max", None, QtGui.QApplication.UnicodeUTF8))
        self.inputInstruction.setText(QtGui.QApplication.translate("Frame", "3. For each input, specify the type. Variable: change in value within an experiment.  Fixed: Same between all experiments.  Design: Fixed within each experiment, but different between experiments.\n"
"4. Select the variable inputs you want displayed in the final output.  (This only affects what is displayed, not the underlying numerical calculations. You can change this later and replot without redoing the calculations.)", None, QtGui.QApplication.UnicodeUTF8))
        self.obs_groupBox.setTitle(QtGui.QApplication.translate("Frame", "Observations:", None, QtGui.QApplication.UnicodeUTF8))
        self.numExperiments_static.setText(QtGui.QApplication.translate("Frame", "5. Select the number of experiments:", None, QtGui.QApplication.UnicodeUTF8))
        self.loadObs_button.setText(QtGui.QApplication.translate("Frame", "Load Observations File...", None, QtGui.QApplication.UnicodeUTF8))
        self.saveObs_button.setText(QtGui.QApplication.translate("Frame", "Save Observations File...", None, QtGui.QApplication.UnicodeUTF8))
        self.obsInstruction.setText(QtGui.QApplication.translate("Frame", "6. Enter the values of the design inputs for each experiment.\n"
"7. Enter the observed mean and standard devation for each of those outputs.", None, QtGui.QApplication.UnicodeUTF8))
        self.obs_table.setToolTip(QtGui.QApplication.translate("Frame", "Enter the fixed value(s) of the design input(s) and\n"
"the statistics of the (noisy) observed output(s).", None, QtGui.QApplication.UnicodeUTF8))
        self.obs_table.verticalHeaderItem(0).setText(QtGui.QApplication.translate("Frame", "Experiment 1", None, QtGui.QApplication.UnicodeUTF8))
        self.obs_table.verticalHeaderItem(1).setText(QtGui.QApplication.translate("Frame", "Experiment 2", None, QtGui.QApplication.UnicodeUTF8))
        self.obs_table.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("Frame", "Design Variable 1 Value", None, QtGui.QApplication.UnicodeUTF8))
        self.obs_table.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("Frame", "Design Variable 2 Value", None, QtGui.QApplication.UnicodeUTF8))
        self.obs_table.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("Frame", "Output 1 Mean", None, QtGui.QApplication.UnicodeUTF8))
        self.obs_table.horizontalHeaderItem(3).setText(QtGui.QApplication.translate("Frame", "Output 1 Std Dev", None, QtGui.QApplication.UnicodeUTF8))
        self.obs_table.horizontalHeaderItem(4).setText(QtGui.QApplication.translate("Frame", "Output 2 Mean", None, QtGui.QApplication.UnicodeUTF8))
        self.obs_table.horizontalHeaderItem(5).setText(QtGui.QApplication.translate("Frame", "Output 2 Std Dev", None, QtGui.QApplication.UnicodeUTF8))
        self.saveInstruction.setText(QtGui.QApplication.translate("Frame", "8. If it is desired to save the posterior input samples to a file for use later, check the box and set the name and location of the resulting file.", None, QtGui.QApplication.UnicodeUTF8))
        self.infSave_chkbox.setToolTip(QtGui.QApplication.translate("Frame", "Click checkbox to save posterior samples as a PSUADE file.", None, QtGui.QApplication.UnicodeUTF8))
        self.infSave_chkbox.setText(QtGui.QApplication.translate("Frame", "Save Posterior Input Samples to File:", None, QtGui.QApplication.UnicodeUTF8))
        self.infSave_button.setText(QtGui.QApplication.translate("Frame", "Browse...", None, QtGui.QApplication.UnicodeUTF8))
        self.rdsSave_chkbox.setToolTip(QtGui.QApplication.translate("Frame", "Click checkbox to save posterior samples as a PSUADE file.", None, QtGui.QApplication.UnicodeUTF8))
        self.rdsSave_chkbox.setText(QtGui.QApplication.translate("Frame", "Save .rds file for restart:", None, QtGui.QApplication.UnicodeUTF8))
        self.rdsSave_button.setText(QtGui.QApplication.translate("Frame", "Browse...", None, QtGui.QApplication.UnicodeUTF8))
        self.discrepancy_chkbox.setToolTip(QtGui.QApplication.translate("Frame", "Apply discrepancy modeling when building response surface.", None, QtGui.QApplication.UnicodeUTF8))
        self.discrepancy_chkbox.setText(QtGui.QApplication.translate("Frame", "Use Discrepancy", None, QtGui.QApplication.UnicodeUTF8))
        self.discrepancySave_chkbox.setToolTip(QtGui.QApplication.translate("Frame", "Click checkbox to save discrepancy samples as a PSUADE file.", None, QtGui.QApplication.UnicodeUTF8))
        self.discrepancySave_chkbox.setText(QtGui.QApplication.translate("Frame", "Save Discrepancy Input Samples to File:", None, QtGui.QApplication.UnicodeUTF8))
        self.discrepancySave_button.setText(QtGui.QApplication.translate("Frame", "Browse...", None, QtGui.QApplication.UnicodeUTF8))
        self.numIterStatic.setText(QtGui.QApplication.translate("Frame", "Total Number of Iterations", None, QtGui.QApplication.UnicodeUTF8))
        self.numIterCalibStatic.setText(QtGui.QApplication.translate("Frame", "Calibration:", None, QtGui.QApplication.UnicodeUTF8))
        self.numIterEmulStatic.setText(QtGui.QApplication.translate("Frame", "Emulator:", None, QtGui.QApplication.UnicodeUTF8))
        self.burnInStatic.setText(QtGui.QApplication.translate("Frame", "Number of Burn-In Iterations (Discarded from the beginning)", None, QtGui.QApplication.UnicodeUTF8))
        self.numBurnInCalibStatic.setText(QtGui.QApplication.translate("Frame", "Calibration:", None, QtGui.QApplication.UnicodeUTF8))
        self.numBurnInEmulStatic.setText(QtGui.QApplication.translate("Frame", "Emulator:", None, QtGui.QApplication.UnicodeUTF8))
        self.inferInstruction.setText(QtGui.QApplication.translate("Frame", "9. Click here:", None, QtGui.QApplication.UnicodeUTF8))
        self.inf_button.setToolTip(QtGui.QApplication.translate("Frame", "Click this button to start/stop inference.", None, QtGui.QApplication.UnicodeUTF8))
        self.inf_button.setText(QtGui.QApplication.translate("Frame", "Infer", None, QtGui.QApplication.UnicodeUTF8))
        self.replotInstruction.setText(QtGui.QApplication.translate("Frame", "10. To change which inputs are displayed after step 6 without recalculating, select/deselect them as in Step 3.  Then click here:", None, QtGui.QApplication.UnicodeUTF8))
        self.replot_button.setToolTip(QtGui.QApplication.translate("Frame", "You can plot a subset of inputs by designating which ones\n"
"to display in ‘Input Settings”.", None, QtGui.QApplication.UnicodeUTF8))
        self.replot_button.setText(QtGui.QApplication.translate("Frame", "Replot", None, QtGui.QApplication.UnicodeUTF8))

from foqus_lib.gui.uq.InputPriorTable import InputPriorTable
