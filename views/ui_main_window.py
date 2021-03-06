# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui_main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1175, 826)
        self.mainFrame = QtWidgets.QWidget(MainWindow)
        self.mainFrame.setObjectName("mainFrame")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.mainFrame)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.groupBox_17 = QtWidgets.QGroupBox(self.mainFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_17.sizePolicy().hasHeightForWidth())
        self.groupBox_17.setSizePolicy(sizePolicy)
        self.groupBox_17.setStyleSheet("background-color: rgba(0, 0, 0,100);\n"
"color:rgb(255,255,255);\n"
"border: transparent")
        self.groupBox_17.setTitle("")
        self.groupBox_17.setObjectName("groupBox_17")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_17)
        self.horizontalLayout_3.setContentsMargins(-1, 5, -1, 5)
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.power_btn = QtWidgets.QPushButton(self.groupBox_17)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.power_btn.sizePolicy().hasHeightForWidth())
        self.power_btn.setSizePolicy(sizePolicy)
        self.power_btn.setStyleSheet("\n"
"QPushButton{\n"
"font-weight:bold;\n"
"border-radius:15px;\n"
"background-color: Transparent;\n"
"color: rgb(255,255,255);\n"
"color: rgb(255,255,255);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"\n"
"    background-color: rgba(132, 132, 132,0.3);\n"
"}")
        self.power_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/icons/pwr.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.power_btn.setIcon(icon)
        self.power_btn.setIconSize(QtCore.QSize(50, 50))
        self.power_btn.setCheckable(True)
        self.power_btn.setObjectName("power_btn")
        self.horizontalLayout_3.addWidget(self.power_btn)
        self.landtakeoff_btn = QtWidgets.QPushButton(self.groupBox_17)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.landtakeoff_btn.sizePolicy().hasHeightForWidth())
        self.landtakeoff_btn.setSizePolicy(sizePolicy)
        self.landtakeoff_btn.setStyleSheet("\n"
"QPushButton{\n"
"font-weight:bold;\n"
"border-radius:25px;\n"
"background-color: Transparent;\n"
"color: rgb(255,255,255);\n"
"color: rgb(255,255,255);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"\n"
"    background-color: rgba(132, 132, 132,0.3);\n"
"}")
        self.landtakeoff_btn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("assets/icons/takeoff.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.landtakeoff_btn.setIcon(icon1)
        self.landtakeoff_btn.setIconSize(QtCore.QSize(50, 50))
        self.landtakeoff_btn.setObjectName("landtakeoff_btn")
        self.horizontalLayout_3.addWidget(self.landtakeoff_btn)
        self.mission_btn = QtWidgets.QPushButton(self.groupBox_17)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mission_btn.sizePolicy().hasHeightForWidth())
        self.mission_btn.setSizePolicy(sizePolicy)
        self.mission_btn.setStyleSheet("\n"
"QPushButton{\n"
"font-weight:bold;\n"
"border-radius:25px;\n"
"background-color: Transparent;\n"
"color: rgb(255,255,255);\n"
"color: rgb(255,255,255);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"\n"
"    background-color: rgba(132, 132, 132,0.3);\n"
"}")
        self.mission_btn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("assets/icons/auto.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mission_btn.setIcon(icon2)
        self.mission_btn.setIconSize(QtCore.QSize(50, 50))
        self.mission_btn.setObjectName("mission_btn")
        self.horizontalLayout_3.addWidget(self.mission_btn)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.telemetry_label = QtWidgets.QLabel(self.groupBox_17)
        self.telemetry_label.setStyleSheet("\n"
"QLabel{\n"
"font-weight:bold;\n"
"background-color: Transparent;\n"
"\n"
"}")
        self.telemetry_label.setObjectName("telemetry_label")
        self.horizontalLayout_3.addWidget(self.telemetry_label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.pushButton = QtWidgets.QPushButton(self.groupBox_17)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("\n"
"QPushButton{\n"
"font-weight:bold;\n"
"border-radius:15px;\n"
"background-color: Transparent;\n"
"color: rgb(255,255,255);\n"
"color: rgb(255,255,255);\n"
"}")
        self.pushButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("assets/icons/battery.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon3)
        self.pushButton.setIconSize(QtCore.QSize(35, 35))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.battery_label = QtWidgets.QLabel(self.groupBox_17)
        self.battery_label.setStyleSheet("\n"
"QLabel{\n"
"font-weight:bold;\n"
"background-color: Transparent;\n"
"\n"
"}")
        self.battery_label.setObjectName("battery_label")
        self.horizontalLayout_3.addWidget(self.battery_label)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.settings_btn = QtWidgets.QPushButton(self.groupBox_17)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.settings_btn.sizePolicy().hasHeightForWidth())
        self.settings_btn.setSizePolicy(sizePolicy)
        self.settings_btn.setStyleSheet("\n"
"QPushButton{\n"
"font-weight:bold;\n"
"border-radius:25px;\n"
"background-color: Transparent;\n"
"color: rgb(255,255,255);\n"
"color: rgb(255,255,255);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"\n"
"    background-color: rgba(132, 132, 132,0.3);\n"
"}")
        self.settings_btn.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("assets/icons/settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settings_btn.setIcon(icon4)
        self.settings_btn.setIconSize(QtCore.QSize(50, 50))
        self.settings_btn.setObjectName("settings_btn")
        self.horizontalLayout_3.addWidget(self.settings_btn)
        self.photo_btn = QtWidgets.QPushButton(self.groupBox_17)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.photo_btn.sizePolicy().hasHeightForWidth())
        self.photo_btn.setSizePolicy(sizePolicy)
        self.photo_btn.setStyleSheet("\n"
"QPushButton{\n"
"font-weight:bold;\n"
"border-radius:25px;\n"
"background-color: Transparent;\n"
"color: rgb(255,255,255);\n"
"color: rgb(255,255,255);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"\n"
"    background-color: rgba(132, 132, 132,0.3);\n"
"}")
        self.photo_btn.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("assets/icons/photo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.photo_btn.setIcon(icon5)
        self.photo_btn.setIconSize(QtCore.QSize(50, 50))
        self.photo_btn.setObjectName("photo_btn")
        self.horizontalLayout_3.addWidget(self.photo_btn)
        self.video_btn = QtWidgets.QPushButton(self.groupBox_17)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.video_btn.sizePolicy().hasHeightForWidth())
        self.video_btn.setSizePolicy(sizePolicy)
        self.video_btn.setStyleSheet("\n"
"QPushButton{\n"
"font-weight:bold;\n"
"border-radius:25px;\n"
"background-color: Transparent;\n"
"color: rgb(255,255,255);\n"
"color: rgb(255,255,255);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"\n"
"    background-color: rgba(132, 132, 132,0.3);\n"
"}")
        self.video_btn.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("assets/icons/videoOff.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.video_btn.setIcon(icon6)
        self.video_btn.setIconSize(QtCore.QSize(50, 50))
        self.video_btn.setObjectName("video_btn")
        self.horizontalLayout_3.addWidget(self.video_btn)
        self.verticalLayout_7.addWidget(self.groupBox_17)
        self.frame = QtWidgets.QFrame(self.mainFrame)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(25, -1, 25, 25)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.up_btn = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.up_btn.sizePolicy().hasHeightForWidth())
        self.up_btn.setSizePolicy(sizePolicy)
        self.up_btn.setStyleSheet("\n"
"QPushButton{\n"
"font-weight:bold;\n"
"border-radius:5px;\n"
"background-color: Transparent;\n"
"color: rgb(255,255,255);\n"
"color: rgb(255,255,255);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"\n"
"    background-color: rgba(132, 132, 132,0.3);\n"
"}")
        self.up_btn.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("assets/icons/up.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.up_btn.setIcon(icon7)
        self.up_btn.setIconSize(QtCore.QSize(60, 60))
        self.up_btn.setObjectName("up_btn")
        self.verticalLayout_3.addWidget(self.up_btn, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.rotate_left_btn = QtWidgets.QPushButton(self.frame)
        self.rotate_left_btn.setStyleSheet("\n"
"QPushButton{\n"
"font-weight:bold;\n"
"border-radius:5px;\n"
"background-color: Transparent;\n"
"color: rgb(255,255,255);\n"
"color: rgb(255,255,255);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"\n"
"    background-color: rgba(132, 132, 132,0.3);\n"
"}")
        self.rotate_left_btn.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("assets/icons/rotate_left.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rotate_left_btn.setIcon(icon8)
        self.rotate_left_btn.setIconSize(QtCore.QSize(60, 60))
        self.rotate_left_btn.setObjectName("rotate_left_btn")
        self.horizontalLayout_2.addWidget(self.rotate_left_btn)
        self.ui_left = QtWidgets.QPushButton(self.frame)
        self.ui_left.setStyleSheet("\n"
"QPushButton{\n"
"font-weight:bold;\n"
"border-radius:5px;\n"
"background-color: Transparent;\n"
"color: rgb(255,255,255);\n"
"color: rgb(255,255,255);\n"
"\n"
"}\n"
"")
        self.ui_left.setText("")
        self.ui_left.setIconSize(QtCore.QSize(40, 40))
        self.ui_left.setObjectName("ui_left")
        self.horizontalLayout_2.addWidget(self.ui_left)
        self.rotate_right_btn = QtWidgets.QPushButton(self.frame)
        self.rotate_right_btn.setStyleSheet("\n"
"QPushButton{\n"
"font-weight:bold;\n"
"border-radius:5px;\n"
"background-color: Transparent;\n"
"color: rgb(255,255,255);\n"
"color: rgb(255,255,255);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"\n"
"    background-color: rgba(132, 132, 132,0.3);\n"
"}")
        self.rotate_right_btn.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("assets/icons/rotate_right.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rotate_right_btn.setIcon(icon9)
        self.rotate_right_btn.setIconSize(QtCore.QSize(60, 60))
        self.rotate_right_btn.setObjectName("rotate_right_btn")
        self.horizontalLayout_2.addWidget(self.rotate_right_btn)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.down_btn = QtWidgets.QPushButton(self.frame)
        self.down_btn.setStyleSheet("\n"
"QPushButton{\n"
"font-weight:bold;\n"
"border-radius:5px;\n"
"background-color: Transparent;\n"
"color: rgb(255,255,255);\n"
"color: rgb(255,255,255);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"\n"
"    background-color: rgba(132, 132, 132,0.3);\n"
"}")
        self.down_btn.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("assets/icons/down.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.down_btn.setIcon(icon10)
        self.down_btn.setIconSize(QtCore.QSize(60, 60))
        self.down_btn.setObjectName("down_btn")
        self.verticalLayout_3.addWidget(self.down_btn, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.forward_btn = QtWidgets.QPushButton(self.frame)
        self.forward_btn.setStyleSheet("\n"
"QPushButton{\n"
"font-weight:bold;\n"
"border-radius:5px;\n"
"background-color: Transparent;\n"
"color: rgb(255,255,255);\n"
"color: rgb(255,255,255);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"\n"
"    background-color: rgba(132, 132, 132,0.3);\n"
"}")
        self.forward_btn.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("assets/icons/forward.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.forward_btn.setIcon(icon11)
        self.forward_btn.setIconSize(QtCore.QSize(60, 60))
        self.forward_btn.setObjectName("forward_btn")
        self.verticalLayout_2.addWidget(self.forward_btn, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.left_btn = QtWidgets.QPushButton(self.frame)
        self.left_btn.setStyleSheet("\n"
"QPushButton{\n"
"font-weight:bold;\n"
"border-radius:5px;\n"
"background-color: Transparent;\n"
"color: rgb(255,255,255);\n"
"color: rgb(255,255,255);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"\n"
"    background-color: rgba(132, 132, 132,0.3);\n"
"}")
        self.left_btn.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("assets/icons/left.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.left_btn.setIcon(icon12)
        self.left_btn.setIconSize(QtCore.QSize(60, 60))
        self.left_btn.setObjectName("left_btn")
        self.horizontalLayout_4.addWidget(self.left_btn)
        self.ignore = QtWidgets.QPushButton(self.frame)
        self.ignore.setStyleSheet("\n"
"QPushButton{\n"
"font-weight:bold;\n"
"border-radius:5px;\n"
"background-color: Transparent;\n"
"color: rgb(255,255,255);\n"
"color: rgb(255,255,255);\n"
"\n"
"}")
        self.ignore.setText("")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("assets/icons/circle.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ignore.setIcon(icon13)
        self.ignore.setIconSize(QtCore.QSize(40, 40))
        self.ignore.setObjectName("ignore")
        self.horizontalLayout_4.addWidget(self.ignore)
        self.right_btn = QtWidgets.QPushButton(self.frame)
        self.right_btn.setStyleSheet("\n"
"QPushButton{\n"
"font-weight:bold;\n"
"border-radius:5px;\n"
"background-color: Transparent;\n"
"color: rgb(255,255,255);\n"
"color: rgb(255,255,255);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"\n"
"    background-color: rgba(132, 132, 132,0.3);\n"
"}")
        self.right_btn.setText("")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap("assets/icons/right.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.right_btn.setIcon(icon14)
        self.right_btn.setIconSize(QtCore.QSize(60, 60))
        self.right_btn.setObjectName("right_btn")
        self.horizontalLayout_4.addWidget(self.right_btn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.back_btn = QtWidgets.QPushButton(self.frame)
        self.back_btn.setStyleSheet("\n"
"QPushButton{\n"
"font-weight:bold;\n"
"border-radius:5px;\n"
"background-color: Transparent;\n"
"color: rgb(255,255,255);\n"
"color: rgb(255,255,255);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"\n"
"    background-color: rgba(132, 132, 132,0.3);\n"
"}")
        self.back_btn.setText("")
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap("assets/icons/back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.back_btn.setIcon(icon15)
        self.back_btn.setIconSize(QtCore.QSize(60, 60))
        self.back_btn.setObjectName("back_btn")
        self.verticalLayout_2.addWidget(self.back_btn, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_7.addWidget(self.frame)
        MainWindow.setCentralWidget(self.mainFrame)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Dunas Drone Controller"))
        self.telemetry_label.setText(_translate("MainWindow", "H: 90"))
        self.battery_label.setText(_translate("MainWindow", "100%"))
