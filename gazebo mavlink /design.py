# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 547)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.run_simulation_button = QtWidgets.QPushButton(self.centralwidget)
        self.run_simulation_button.setObjectName("run_simulation_button")
        self.verticalLayout.addWidget(self.run_simulation_button, 0, QtCore.Qt.AlignHCenter)
        self.start_multisitl_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_multisitl_button.setObjectName("start_multisitl_button")
        self.verticalLayout.addWidget(self.start_multisitl_button, 0, QtCore.Qt.AlignHCenter)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.arm_button = QtWidgets.QPushButton(self.centralwidget)
        self.arm_button.setObjectName("arm_button")
        self.verticalLayout_5.addWidget(self.arm_button, 0, QtCore.Qt.AlignHCenter)
        self.disarm_button = QtWidgets.QPushButton(self.centralwidget)
        self.disarm_button.setObjectName("disarm_button")
        self.verticalLayout_5.addWidget(self.disarm_button, 0, QtCore.Qt.AlignHCenter)
        self.emergency_button = QtWidgets.QPushButton(self.centralwidget)
        self.emergency_button.setObjectName("emergency_button")
        self.verticalLayout_5.addWidget(self.emergency_button, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.takeoff_altitude_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.takeoff_altitude_lineEdit.setText("")
        self.takeoff_altitude_lineEdit.setObjectName("takeoff_altitude_lineEdit")
        self.verticalLayout_6.addWidget(self.takeoff_altitude_lineEdit, 0, QtCore.Qt.AlignHCenter)
        self.takeoff_button = QtWidgets.QPushButton(self.centralwidget)
        self.takeoff_button.setObjectName("takeoff_button")
        self.verticalLayout_6.addWidget(self.takeoff_button, 0, QtCore.Qt.AlignHCenter)
        self.land_button = QtWidgets.QPushButton(self.centralwidget)
        self.land_button.setObjectName("land_button")
        self.verticalLayout_6.addWidget(self.land_button, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_2.addLayout(self.verticalLayout_6)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.move_position_x_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.move_position_x_lineEdit.setObjectName("move_position_x_lineEdit")
        self.horizontalLayout_3.addWidget(self.move_position_x_lineEdit, 0, QtCore.Qt.AlignHCenter)
        self.move_position_y_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.move_position_y_lineEdit.setObjectName("move_position_y_lineEdit")
        self.horizontalLayout_3.addWidget(self.move_position_y_lineEdit, 0, QtCore.Qt.AlignHCenter)
        self.move_position_z_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.move_position_z_lineEdit.setObjectName("move_position_z_lineEdit")
        self.horizontalLayout_3.addWidget(self.move_position_z_lineEdit, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_7.addLayout(self.horizontalLayout_3)
        self.move_velocity_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.move_velocity_lineEdit.setObjectName("move_velocity_lineEdit")
        self.verticalLayout_7.addWidget(self.move_velocity_lineEdit, 0, QtCore.Qt.AlignHCenter)
        self.swarm_move_button = QtWidgets.QPushButton(self.centralwidget)
        self.swarm_move_button.setObjectName("swarm_move_button")
        self.verticalLayout_7.addWidget(self.swarm_move_button, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_2.addLayout(self.verticalLayout_7)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.drone1_position_label = QtWidgets.QLabel(self.frame)
        self.drone1_position_label.setObjectName("drone1_position_label")
        self.verticalLayout_2.addWidget(self.drone1_position_label)
        self.drone2_position_label = QtWidgets.QLabel(self.frame)
        self.drone2_position_label.setObjectName("drone2_position_label")
        self.verticalLayout_2.addWidget(self.drone2_position_label)
        self.drone3_position_label = QtWidgets.QLabel(self.frame)
        self.drone3_position_label.setObjectName("drone3_position_label")
        self.verticalLayout_2.addWidget(self.drone3_position_label)
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.drone1_velocity_label = QtWidgets.QLabel(self.frame)
        self.drone1_velocity_label.setObjectName("drone1_velocity_label")
        self.verticalLayout_8.addWidget(self.drone1_velocity_label)
        self.drone2_velocity_label = QtWidgets.QLabel(self.frame)
        self.drone2_velocity_label.setObjectName("drone2_velocity_label")
        self.verticalLayout_8.addWidget(self.drone2_velocity_label)
        self.drone3_velocity_label = QtWidgets.QLabel(self.frame)
        self.drone3_velocity_label.setObjectName("drone3_velocity_label")
        self.verticalLayout_8.addWidget(self.drone3_velocity_label)
        self.horizontalLayout_5.addLayout(self.verticalLayout_8)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout_4.addWidget(self.comboBox, 0, QtCore.Qt.AlignHCenter)
        self.command_window_button = QtWidgets.QPushButton(self.frame)
        self.command_window_button.setObjectName("command_window_button")
        self.verticalLayout_4.addWidget(self.command_window_button, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_3.addLayout(self.verticalLayout_4)
        self.horizontalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Drone Control Interface"))
        self.run_simulation_button.setText(_translate("MainWindow", "Run Simulation"))
        self.start_multisitl_button.setText(_translate("MainWindow", "Start Multisitl"))
        self.arm_button.setText(_translate("MainWindow", "Arm"))
        self.disarm_button.setText(_translate("MainWindow", "Disarm"))
        self.emergency_button.setText(_translate("MainWindow", "Emergency"))
        self.takeoff_altitude_lineEdit.setPlaceholderText(_translate("MainWindow", "Altitude"))
        self.takeoff_button.setText(_translate("MainWindow", "Takeoff"))
        self.land_button.setText(_translate("MainWindow", "Land"))
        self.move_position_x_lineEdit.setPlaceholderText(_translate("MainWindow", "X"))
        self.move_position_y_lineEdit.setPlaceholderText(_translate("MainWindow", "Y"))
        self.move_position_z_lineEdit.setPlaceholderText(_translate("MainWindow", "Z"))
        self.move_velocity_lineEdit.setPlaceholderText(_translate("MainWindow", "Velocity"))
        self.swarm_move_button.setText(_translate("MainWindow", "Swarm Move"))
        self.drone1_position_label.setText(_translate("MainWindow", " 1. Drone Pozisyonu: Bilinmiyor  "))
        self.drone2_position_label.setText(_translate("MainWindow", " 2. Drone Pozisyonu: Bilinmiyor  "))
        self.drone3_position_label.setText(_translate("MainWindow", " 3. Drone Pozisyonu: Bilinmiyor  "))
        self.drone1_velocity_label.setText(_translate("MainWindow", "  1.Drone Hızı  "))
        self.drone2_velocity_label.setText(_translate("MainWindow", "  2.Drone Hızı  "))
        self.drone3_velocity_label.setText(_translate("MainWindow", "  3.Drone Hızı  "))
        self.comboBox.setItemText(0, _translate("MainWindow", "Drone1"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Drone2"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Drone3"))
        self.command_window_button.setText(_translate("MainWindow", "Open Command Window"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
