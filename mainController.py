#Import PyQt related libraries
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget, QInputDialog
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer, QThread, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QMessageBox

#Import ui of main window
from views.ui_main_window import *

#Import python libraries
import sys
from time import sleep
import numpy
import cv2
import os

#Import library to control Tello drone
from djitellopy import Tello

#Import image helper
from helpers.imageHelper import *


#Thread used to receive video from drone
class VideoReceicer(QThread):
    displayVideo = pyqtSignal(numpy.ndarray)

    def __init__(self, _tello):
        super().__init__()
        #Initialize variables
        self.running = True
        self.tello = _tello
       

    def run(self):
        #In case streaming is on (error at disconnection) we close it
        self.tello.streamoff()
        #Init video streaming
        self.tello.streamon()
        sleep(3)
        self.frameRead = self.tello.get_frame_read()
        while self.running:
            sleep(1/10)
            currentFrame = self.frameRead.frame
            if currentFrame is not None:
                self.displayVideo.emit(currentFrame)

    def close(self):
        #Stop receiving data
        self.running = False


class Main(QtWidgets.QMainWindow):
   
    def __init__(self, parent=None):
        #Deploy window
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # No video background image
        self.ui.mainFrame.setStyleSheet("#mainFrame{border-image:url(assets/icons/noVideoimg.png);}")

        #Define timer to ask for telemetry every X seconds
        self.teleTimer = QTimer()
        self.teleTimer.timeout.connect(self.updateTelemetry)

        #Define timer to send RC signal to tello
        self.rcTimer = QTimer()
        self.rcTimer.timeout.connect(self.sendRcSignal)

        #Initialize tello variables
        self.tello = None
        self.telloIsFlying = False
        self.telloVelocity = 30
        self.telloUpVelocity = 0
        self.telloYawVelocity = 0
        self.telloForwardVelocity = 0
        self.telloRightVelocity = 0
        self.telloRcTime = 100


    #Reimplement KeyPressed Event to be able to control tello with keys
    def keyPressEvent(self, event):
        if self.tello is not None:
            if event.key() == QtCore.Qt.Key_W and not event.isAutoRepeat():
                self.on_up_btn_pressed()
            elif event.key() == QtCore.Qt.Key_S and not event.isAutoRepeat():
                self.on_down_btn_pressed()
            elif event.key() == QtCore.Qt.Key_A and not event.isAutoRepeat():
                self.on_rotate_left_btn_pressed()
            elif event.key() == QtCore.Qt.Key_D and not event.isAutoRepeat():
                self.on_rotate_right_btn_pressed()
            elif event.key() == QtCore.Qt.Key_Up and not event.isAutoRepeat():
                self.on_forward_btn_pressed()
            elif event.key() == QtCore.Qt.Key_Down and not event.isAutoRepeat():
                self.on_back_btn_pressed()
            elif event.key() == QtCore.Qt.Key_Right and not event.isAutoRepeat():
                self.on_right_btn_pressed()
            elif event.key() == QtCore.Qt.Key_Left and not event.isAutoRepeat():
                self.on_left_btn_pressed()
        event.accept()
    #Reimplement KeyRelease Event to be able to control tello with keys
    def keyReleaseEvent(self, event):
        if self.tello is not None:
            if event.key() == QtCore.Qt.Key_W and not event.isAutoRepeat():
                self.on_up_btn_released()
            elif event.key() == QtCore.Qt.Key_S and not event.isAutoRepeat():
                self.on_down_btn_released()
            elif event.key() == QtCore.Qt.Key_A and not event.isAutoRepeat():
                self.on_rotate_left_btn_released()
            elif event.key() == QtCore.Qt.Key_D and not event.isAutoRepeat():
                self.on_rotate_right_btn_released()
            elif event.key() == QtCore.Qt.Key_Up and not event.isAutoRepeat():
                self.on_forward_btn_released()
            elif event.key() == QtCore.Qt.Key_Down and not event.isAutoRepeat():
                self.on_back_btn_released()
            elif event.key() == QtCore.Qt.Key_Right and not event.isAutoRepeat():
                self.on_right_btn_released()
            elif event.key() == QtCore.Qt.Key_Left and not event.isAutoRepeat():
                self.on_left_btn_released()
        event.accept()


    #On Up button pressed
    def on_up_btn_pressed(self):
        self.telloUpVelocity = self.telloVelocity
        self.rcTimer.start(self.telloRcTime)
    #On Up button released
    def on_up_btn_released(self):
        self.telloUpVelocity = 0
        self.rcTimer.stop()
        self.sendRcSignal()

    #On Down button pressed
    def on_down_btn_pressed(self):
        self.telloUpVelocity = -self.telloVelocity
        self.rcTimer.start(self.telloRcTime)
    #On Down button released
    def on_down_btn_released(self):
        self.telloUpVelocity = 0
        self.rcTimer.stop()
        self.sendRcSignal()

    #On Rotate right button pressed
    def on_rotate_right_btn_pressed(self):
        self.telloYawVelocity = self.telloVelocity
        self.rcTimer.start(self.telloRcTime)
    #On Rotate right button released
    def on_rotate_right_btn_released(self):
        self.telloYawVelocity = 0
        self.rcTimer.stop()
        self.sendRcSignal()
    
    #On Rotate left button pressed
    def on_rotate_left_btn_pressed(self):
        self.telloYawVelocity = -self.telloVelocity
        self.rcTimer.start(self.telloRcTime)
    #On Rotate left button released
    def on_rotate_left_btn_released(self):
        self.telloYawVelocity = 0
        self.rcTimer.stop()
        self.sendRcSignal()

    #On Forward button pressed
    def on_forward_btn_pressed(self):
        self.telloForwardVelocity = self.telloVelocity
        self.rcTimer.start(self.telloRcTime)
    #On Forward left button released
    def on_forward_btn_released(self):
        self.telloForwardVelocity = 0
        self.rcTimer.stop()
        self.sendRcSignal()
    
    #On Back button pressed
    def on_back_btn_pressed(self):
        self.telloForwardVelocity = -self.telloVelocity
        self.rcTimer.start(self.telloRcTime)
    #On Back left button released
    def on_back_btn_released(self):
        self.telloForwardVelocity = 0
        self.rcTimer.stop()
        self.sendRcSignal()

    #On Right button pressed
    def on_right_btn_pressed(self):
        self.telloRightVelocity = self.telloVelocity
        self.rcTimer.start(self.telloRcTime)
    #On Right left button released
    def on_right_btn_released(self):
        self.telloRightVelocity = 0
        self.rcTimer.stop()
        self.sendRcSignal()

    #On Left button pressed
    def on_left_btn_pressed(self):
        self.telloRightVelocity = -self.telloVelocity
        self.rcTimer.start(self.telloRcTime)
    #On Left left button released
    def on_left_btn_released(self):
        self.telloRightVelocity = 0
        self.rcTimer.stop()
        self.sendRcSignal()

    #Function called when land/takeoff button is clicked
    @pyqtSlot()
    def on_landtakeoff_btn_clicked(self):
        if self.tello is not None:
            if not self.telloIsFlying:
                try:
                    self.tello.takeoff()
                    self.telloIsFlying = True
                    self.ui.landtakeoff_btn.setIcon(QtGui.QIcon('assets/icons/land.png'))
                except Exception as e:
                    print(e)
            else:
                try:
                    self.tello.land()
                    self.telloIsFlying = False
                    self.ui.landtakeoff_btn.setIcon(QtGui.QIcon('assets/icons/takeoff.png'))
                except Exception as e:
                    print(e)
            

    #Function called when power button is clicked
    @pyqtSlot()
    def on_power_btn_clicked(self):
        print("POWER_BTN")
        if self.tello is None:
            self.connectDrone()
        else:
            self.disconnectDrone()
      
    #Function used to connect drone
    def connectDrone(self): 
        print("CONNECT")
        #Init connection to tello
        try:
            self.tello = Tello()
            self.tello.connect()
            self.telloIsFlying = False
        except Exception as e:
            self.tello = None

        if self.tello is not None:
            #Start thread to receive video
            self.droneVideo = VideoReceicer(self.tello)
            self.droneVideo.displayVideo.connect(self.setImage)
            self.droneVideo.start()
            #Start timer for telemetry
            self.teleTimer.start(5000)
            #Update interface
            self.ui.power_btn.setIcon(QtGui.QIcon('assets/icons/pwrOn.png'))

    #Function used to disconnect drone
    def disconnectDrone(self):
        PRINT("DISCONNECT")
        #Disconnect tello drone
        self.tello.streamoff()
        self.tello.end()
        self.tello = None

        #Stop video streaming
        self.droneVideo.close()

        #Stop timers
        self.teleTimer.stop()

        #Update interface
        self.ui.mainFrame.setStyleSheet("#mainFrame{border-image:url(assets/icons/noVideoimg.png);}")
        self.ui.power_btn.setIcon(QtGui.QIcon('assets/icons/pwr.png'))

    #Send RC Signal to tello
    def sendRcSignal(self):
        if self.tello is not None:
            self.tello.send_rc_control(self.telloRightVelocity, self.telloForwardVelocity, self.telloUpVelocity, self.telloYawVelocity)

    #Function called every X seconds to update telemetry
    def updateTelemetry(self):
        self.ui.battery_label.setText(f'{self.tello.get_battery()}%')

    #Function called from the videoThread used to display image
    @pyqtSlot(numpy.ndarray)
    def setImage(self, frame):
        try:
            #If frame is empty do nothing
            if frame is None:
                pass
            else:
                #Proccess and display image
                decodedObjects = decodeQR(frame)
                finalImg = showQrImage(frame, decodedObjects)
                cv2.imwrite('tmpimg.jpg', finalImg)

                self.ui.mainFrame.setStyleSheet("#mainFrame{border-image:url(tmpimg.jpg);}")

            #Remove image
            os.remove('tmpimg.jpg')
        except Exception as e:
            print(e)

def main_window():  # Run application
    app = QApplication(sys.argv)

    # create and show mainWindow
    mainWindow = Main()
    mainWindow.showMaximized()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main_window()
