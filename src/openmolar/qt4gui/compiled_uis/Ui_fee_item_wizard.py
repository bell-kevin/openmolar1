# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/neil/openmolar/openmolar/src/openmolar/qt-designer/fee_item_wizard.ui'
#
# Created: Wed Mar 10 00:12:09 2010
#      by: PyQt4 UI code generator 4.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(500, 564)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(-1, 10, -1, 10)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_6.addWidget(self.label_2)
        self.itemcode_label = QtGui.QLabel(Dialog)
        self.itemcode_label.setObjectName("itemcode_label")
        self.horizontalLayout_6.addWidget(self.itemcode_label)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(30, -1, 30, -1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        self.category_comboBox = QtGui.QComboBox(Dialog)
        self.category_comboBox.setObjectName("category_comboBox")
        self.horizontalLayout_5.addWidget(self.category_comboBox)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(30, -1, 30, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.pl_cmp_comboBox = QtGui.QComboBox(Dialog)
        self.pl_cmp_comboBox.setObjectName("pl_cmp_comboBox")
        self.horizontalLayout_4.addWidget(self.pl_cmp_comboBox)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        self.uc_radioButton = QtGui.QRadioButton(Dialog)
        self.uc_radioButton.setObjectName("uc_radioButton")
        self.gridLayout_2.addWidget(self.uc_radioButton, 0, 1, 1, 1)
        self.uc_reg_radioButton = QtGui.QRadioButton(Dialog)
        self.uc_reg_radioButton.setObjectName("uc_reg_radioButton")
        self.gridLayout_2.addWidget(self.uc_reg_radioButton, 0, 2, 1, 1)
        self.uc_multireg_radioButton = QtGui.QRadioButton(Dialog)
        self.uc_multireg_radioButton.setObjectName("uc_multireg_radioButton")
        self.gridLayout_2.addWidget(self.uc_multireg_radioButton, 0, 3, 1, 1)
        self.usercode_lineEdit = QtGui.QLineEdit(Dialog)
        self.usercode_lineEdit.setObjectName("usercode_lineEdit")
        self.gridLayout_2.addWidget(self.usercode_lineEdit, 1, 0, 1, 4)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.regulations_lineEdit = QtGui.QLineEdit(Dialog)
        self.regulations_lineEdit.setObjectName("regulations_lineEdit")
        self.horizontalLayout.addWidget(self.regulations_lineEdit)
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.description_lineEdit = QtGui.QLineEdit(Dialog)
        self.description_lineEdit.setObjectName("description_lineEdit")
        self.horizontalLayout_2.addWidget(self.description_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_9 = QtGui.QLabel(Dialog)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_3.addWidget(self.label_9)
        self.descriptions_listWidget = QtGui.QListWidget(Dialog)
        self.descriptions_listWidget.setMaximumSize(QtCore.QSize(16777215, 80))
        self.descriptions_listWidget.setObjectName("descriptions_listWidget")
        self.horizontalLayout_3.addWidget(self.descriptions_listWidget)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_7 = QtGui.QLabel(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 0, 1, 1)
        self.doubleSpinBox = QtGui.QDoubleSpinBox(Dialog)
        self.doubleSpinBox.setMaximum(20000.0)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.gridLayout.addWidget(self.doubleSpinBox, 0, 3, 1, 1)
        self.doubleSpinBox_4 = QtGui.QDoubleSpinBox(Dialog)
        self.doubleSpinBox_4.setMaximum(20000.0)
        self.doubleSpinBox_4.setObjectName("doubleSpinBox_4")
        self.gridLayout.addWidget(self.doubleSpinBox_4, 0, 9, 1, 1)
        self.label_8 = QtGui.QLabel(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 1, 0, 1, 1)
        self.doubleSpinBox_7 = QtGui.QDoubleSpinBox(Dialog)
        self.doubleSpinBox_7.setMaximum(20000.0)
        self.doubleSpinBox_7.setObjectName("doubleSpinBox_7")
        self.gridLayout.addWidget(self.doubleSpinBox_7, 1, 7, 1, 1)
        self.doubleSpinBox_5 = QtGui.QDoubleSpinBox(Dialog)
        self.doubleSpinBox_5.setMaximum(20000.0)
        self.doubleSpinBox_5.setObjectName("doubleSpinBox_5")
        self.gridLayout.addWidget(self.doubleSpinBox_5, 1, 9, 1, 1)
        self.doubleSpinBox_6 = QtGui.QDoubleSpinBox(Dialog)
        self.doubleSpinBox_6.setMaximum(20000.0)
        self.doubleSpinBox_6.setObjectName("doubleSpinBox_6")
        self.gridLayout.addWidget(self.doubleSpinBox_6, 1, 6, 1, 1)
        self.doubleSpinBox_2 = QtGui.QDoubleSpinBox(Dialog)
        self.doubleSpinBox_2.setMaximum(20000.0)
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.gridLayout.addWidget(self.doubleSpinBox_2, 0, 6, 1, 1)
        self.doubleSpinBox_8 = QtGui.QDoubleSpinBox(Dialog)
        self.doubleSpinBox_8.setMaximum(20000.0)
        self.doubleSpinBox_8.setObjectName("doubleSpinBox_8")
        self.gridLayout.addWidget(self.doubleSpinBox_8, 1, 3, 1, 1)
        self.doubleSpinBox_3 = QtGui.QDoubleSpinBox(Dialog)
        self.doubleSpinBox_3.setMaximum(20000.0)
        self.doubleSpinBox_3.setObjectName("doubleSpinBox_3")
        self.gridLayout.addWidget(self.doubleSpinBox_3, 0, 7, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_( u"Dialog"))
        self.label_2.setText(_( u"Item Code"))
        self.itemcode_label.setText(_( u"TextLabel"))
        self.label.setText(_( u"Category"))
        self.label_4.setText(_( u"Category for treatment Planning"))
        self.label_3.setText(_( u"UserCode"))
        self.uc_radioButton.setText(_( u"Standard"))
        self.uc_reg_radioButton.setText(_( u"Regex"))
        self.uc_multireg_radioButton.setText(_( u"Multiple Regex"))
        self.label_6.setText(_( u"Regulations"))
        self.pushButton.setText(_( u"Wizard"))
        self.label_5.setText(_( u"Patient\'s Description"))
        self.label_9.setText(_( u"Clinical Descriptions"))
        self.label_7.setText(_( u"Gross Fees"))
        self.label_8.setText(_( u"Net Fees"))
