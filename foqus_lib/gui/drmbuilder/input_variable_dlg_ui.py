# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'input_variable_dlg_move.ui'
#
# Created: Fri Oct 09 13:52:03 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_inputVariableDlg(object):
    def setupUi(self, inputVariableDlg):
        inputVariableDlg.setObjectName("inputVariableDlg")
        inputVariableDlg.resize(645, 462)
        self.gridLayout_2 = QtGui.QGridLayout(inputVariableDlg)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_InputList = QtGui.QLabel(inputVariableDlg)
        self.label_InputList.setObjectName("label_InputList")
        self.verticalLayout.addWidget(self.label_InputList)
        self.listWidget_InputList = QtGui.QListWidget(inputVariableDlg)
        self.listWidget_InputList.setObjectName("listWidget_InputList")
        self.verticalLayout.addWidget(self.listWidget_InputList)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_SamplingTime = QtGui.QLabel(inputVariableDlg)
        self.label_SamplingTime.setObjectName("label_SamplingTime")
        self.gridLayout.addWidget(self.label_SamplingTime, 0, 0, 1, 1)
        self.lineEdit_SamplingTime = QtGui.QLineEdit(inputVariableDlg)
        self.lineEdit_SamplingTime.setObjectName("lineEdit_SamplingTime")
        self.gridLayout.addWidget(self.lineEdit_SamplingTime, 0, 1, 1, 1)
        self.lineEdit_UnitSamplingTime = QtGui.QLineEdit(inputVariableDlg)
        self.lineEdit_UnitSamplingTime.setEnabled(False)
        self.lineEdit_UnitSamplingTime.setReadOnly(True)
        self.lineEdit_UnitSamplingTime.setObjectName("lineEdit_UnitSamplingTime")
        self.gridLayout.addWidget(self.lineEdit_UnitSamplingTime, 0, 2, 1, 1)
        self.label_RampTime = QtGui.QLabel(inputVariableDlg)
        self.label_RampTime.setObjectName("label_RampTime")
        self.gridLayout.addWidget(self.label_RampTime, 1, 0, 1, 1)
        self.lineEdit_RampTime = QtGui.QLineEdit(inputVariableDlg)
        self.lineEdit_RampTime.setEnabled(True)
        self.lineEdit_RampTime.setObjectName("lineEdit_RampTime")
        self.gridLayout.addWidget(self.lineEdit_RampTime, 1, 1, 1, 1)
        self.lineEdit_UnitRampTime = QtGui.QLineEdit(inputVariableDlg)
        self.lineEdit_UnitRampTime.setEnabled(False)
        self.lineEdit_UnitRampTime.setReadOnly(True)
        self.lineEdit_UnitRampTime.setObjectName("lineEdit_UnitRampTime")
        self.gridLayout.addWidget(self.lineEdit_UnitRampTime, 1, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton_Up = QtGui.QPushButton(inputVariableDlg)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_Up.sizePolicy().hasHeightForWidth())
        self.pushButton_Up.setSizePolicy(sizePolicy)
        self.pushButton_Up.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_Up.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_Up.setObjectName("pushButton_Up")
        self.verticalLayout_3.addWidget(self.pushButton_Up)
        self.pushButton_Down = QtGui.QPushButton(inputVariableDlg)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_Down.sizePolicy().hasHeightForWidth())
        self.pushButton_Down.setSizePolicy(sizePolicy)
        self.pushButton_Down.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_Down.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_Down.setObjectName("pushButton_Down")
        self.verticalLayout_3.addWidget(self.pushButton_Down)
        self.gridLayout_2.addLayout(self.verticalLayout_3, 0, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(13, 17, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 2, 1, 1)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.formLayout_3 = QtGui.QFormLayout()
        self.formLayout_3.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_3.setObjectName("formLayout_3")
        self.lineEdit_NumberOfVariedVariables = QtGui.QLineEdit(inputVariableDlg)
        self.lineEdit_NumberOfVariedVariables.setEnabled(False)
        self.lineEdit_NumberOfVariedVariables.setReadOnly(False)
        self.lineEdit_NumberOfVariedVariables.setObjectName("lineEdit_NumberOfVariedVariables")
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEdit_NumberOfVariedVariables)
        self.label_NumberOfVariedVariables = QtGui.QLabel(inputVariableDlg)
        self.label_NumberOfVariedVariables.setObjectName("label_NumberOfVariedVariables")
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_NumberOfVariedVariables)
        self.groupBox_ForSelected = QtGui.QGroupBox(inputVariableDlg)
        self.groupBox_ForSelected.setObjectName("groupBox_ForSelected")
        self.formLayout = QtGui.QFormLayout(self.groupBox_ForSelected)
        self.formLayout.setObjectName("formLayout")
        self.label_Name = QtGui.QLabel(self.groupBox_ForSelected)
        self.label_Name.setObjectName("label_Name")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_Name)
        self.lineEdit_Name = QtGui.QLineEdit(self.groupBox_ForSelected)
        self.lineEdit_Name.setEnabled(False)
        self.lineEdit_Name.setObjectName("lineEdit_Name")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEdit_Name)
        self.label_Unit = QtGui.QLabel(self.groupBox_ForSelected)
        self.label_Unit.setObjectName("label_Unit")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_Unit)
        self.lineEdit_Unit = QtGui.QLineEdit(self.groupBox_ForSelected)
        self.lineEdit_Unit.setEnabled(False)
        self.lineEdit_Unit.setObjectName("lineEdit_Unit")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEdit_Unit)
        self.label_Description = QtGui.QLabel(self.groupBox_ForSelected)
        self.label_Description.setObjectName("label_Description")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_Description)
        self.lineEdit_Description = QtGui.QLineEdit(self.groupBox_ForSelected)
        self.lineEdit_Description.setObjectName("lineEdit_Description")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.lineEdit_Description)
        self.label_Default = QtGui.QLabel(self.groupBox_ForSelected)
        self.label_Default.setObjectName("label_Default")
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_Default)
        self.lineEdit_Default = QtGui.QLineEdit(self.groupBox_ForSelected)
        self.lineEdit_Default.setObjectName("lineEdit_Default")
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.lineEdit_Default)
        self.label_Lower = QtGui.QLabel(self.groupBox_ForSelected)
        self.label_Lower.setObjectName("label_Lower")
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_Lower)
        self.lineEdit_Lower = QtGui.QLineEdit(self.groupBox_ForSelected)
        self.lineEdit_Lower.setObjectName("lineEdit_Lower")
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.lineEdit_Lower)
        self.label_Upper = QtGui.QLabel(self.groupBox_ForSelected)
        self.label_Upper.setObjectName("label_Upper")
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_Upper)
        self.lineEdit_Upper = QtGui.QLineEdit(self.groupBox_ForSelected)
        self.lineEdit_Upper.setObjectName("lineEdit_Upper")
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.lineEdit_Upper)
        self.label_RampRate = QtGui.QLabel(self.groupBox_ForSelected)
        self.label_RampRate.setObjectName("label_RampRate")
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_RampRate)
        self.lineEdit_RampRate = QtGui.QLineEdit(self.groupBox_ForSelected)
        self.lineEdit_RampRate.setObjectName("lineEdit_RampRate")
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.lineEdit_RampRate)
        self.checkBox_UseRamp = QtGui.QCheckBox(self.groupBox_ForSelected)
        self.checkBox_UseRamp.setObjectName("checkBox_UseRamp")
        self.formLayout.setWidget(8, QtGui.QFormLayout.SpanningRole, self.checkBox_UseRamp)
        self.checkBox_VariesWithTime = QtGui.QCheckBox(self.groupBox_ForSelected)
        self.checkBox_VariesWithTime.setObjectName("checkBox_VariesWithTime")
        self.formLayout.setWidget(9, QtGui.QFormLayout.SpanningRole, self.checkBox_VariesWithTime)
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.SpanningRole, self.groupBox_ForSelected)
        self.label_SolverMinTimeStep = QtGui.QLabel(inputVariableDlg)
        self.label_SolverMinTimeStep.setObjectName("label_SolverMinTimeStep")
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.SpanningRole, self.label_SolverMinTimeStep)
        self.verticalLayout_2.addLayout(self.formLayout_3)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 3, 1, 1)
        self.pushButton_Cancel = QtGui.QPushButton(inputVariableDlg)
        self.pushButton_Cancel.setAutoDefault(False)
        self.pushButton_Cancel.setObjectName("pushButton_Cancel")
        self.gridLayout_2.addWidget(self.pushButton_Cancel, 1, 0, 1, 1)
        self.pushButton_OK = QtGui.QPushButton(inputVariableDlg)
        self.pushButton_OK.setAutoDefault(False)
        self.pushButton_OK.setObjectName("pushButton_OK")
        self.gridLayout_2.addWidget(self.pushButton_OK, 1, 3, 1, 1)

        self.retranslateUi(inputVariableDlg)
        QtCore.QMetaObject.connectSlotsByName(inputVariableDlg)
        inputVariableDlg.setTabOrder(self.listWidget_InputList, self.lineEdit_SamplingTime)
        inputVariableDlg.setTabOrder(self.lineEdit_SamplingTime, self.lineEdit_RampTime)
        inputVariableDlg.setTabOrder(self.lineEdit_RampTime, self.lineEdit_Name)
        inputVariableDlg.setTabOrder(self.lineEdit_Name, self.lineEdit_Unit)
        inputVariableDlg.setTabOrder(self.lineEdit_Unit, self.lineEdit_Description)
        inputVariableDlg.setTabOrder(self.lineEdit_Description, self.lineEdit_Default)
        inputVariableDlg.setTabOrder(self.lineEdit_Default, self.lineEdit_Lower)
        inputVariableDlg.setTabOrder(self.lineEdit_Lower, self.lineEdit_Upper)
        inputVariableDlg.setTabOrder(self.lineEdit_Upper, self.lineEdit_RampRate)
        inputVariableDlg.setTabOrder(self.lineEdit_RampRate, self.checkBox_UseRamp)
        inputVariableDlg.setTabOrder(self.checkBox_UseRamp, self.checkBox_VariesWithTime)
        inputVariableDlg.setTabOrder(self.checkBox_VariesWithTime, self.lineEdit_UnitSamplingTime)
        inputVariableDlg.setTabOrder(self.lineEdit_UnitSamplingTime, self.lineEdit_UnitRampTime)
        inputVariableDlg.setTabOrder(self.lineEdit_UnitRampTime, self.lineEdit_NumberOfVariedVariables)

    def retranslateUi(self, inputVariableDlg):
        inputVariableDlg.setWindowTitle(QtGui.QApplication.translate("inputVariableDlg", "Input Variable Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label_InputList.setText(QtGui.QApplication.translate("inputVariableDlg", "Input Variable List", None, QtGui.QApplication.UnicodeUTF8))
        self.label_SamplingTime.setText(QtGui.QApplication.translate("inputVariableDlg", "Sampling Time Interval", None, QtGui.QApplication.UnicodeUTF8))
        self.label_RampTime.setText(QtGui.QApplication.translate("inputVariableDlg", "Time Step During Ramp", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_Up.setText(QtGui.QApplication.translate("inputVariableDlg", "˄", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_Down.setText(QtGui.QApplication.translate("inputVariableDlg", "˅", None, QtGui.QApplication.UnicodeUTF8))
        self.label_NumberOfVariedVariables.setText(QtGui.QApplication.translate("inputVariableDlg", "Number of Time Dependent Variables", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_ForSelected.setTitle(QtGui.QApplication.translate("inputVariableDlg", "For Selected Input Variable", None, QtGui.QApplication.UnicodeUTF8))
        self.label_Name.setText(QtGui.QApplication.translate("inputVariableDlg", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_Unit.setText(QtGui.QApplication.translate("inputVariableDlg", "Unit", None, QtGui.QApplication.UnicodeUTF8))
        self.label_Description.setText(QtGui.QApplication.translate("inputVariableDlg", "Description", None, QtGui.QApplication.UnicodeUTF8))
        self.label_Default.setText(QtGui.QApplication.translate("inputVariableDlg", "Default", None, QtGui.QApplication.UnicodeUTF8))
        self.label_Lower.setText(QtGui.QApplication.translate("inputVariableDlg", "Lower", None, QtGui.QApplication.UnicodeUTF8))
        self.label_Upper.setText(QtGui.QApplication.translate("inputVariableDlg", "Upper", None, QtGui.QApplication.UnicodeUTF8))
        self.label_RampRate.setText(QtGui.QApplication.translate("inputVariableDlg", "Ramp Rate", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_UseRamp.setText(QtGui.QApplication.translate("inputVariableDlg", "Use Ramp to Replace Step Change", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_VariesWithTime.setText(QtGui.QApplication.translate("inputVariableDlg", "Varies With Time", None, QtGui.QApplication.UnicodeUTF8))
        self.label_SolverMinTimeStep.setText(QtGui.QApplication.translate("inputVariableDlg", "Solver Minimum Time Step is", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_Cancel.setText(QtGui.QApplication.translate("inputVariableDlg", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_OK.setText(QtGui.QApplication.translate("inputVariableDlg", "OK", None, QtGui.QApplication.UnicodeUTF8))

