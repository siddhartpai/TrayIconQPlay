#!/bin/python
import sys
from PyQt4 import QtGui, Qt, QtCore
from PyQt4.QtGui import QApplication, QCursor, QWidget
import subprocess

class widget(QtGui.QWidget):
    p1x=-1
    p1y=-1
    p2x=-1
    p2y=-1

    def __init__(self):
        super(widget, self).__init__()
        self.initUI()
        
    def initUI(self):              
        #self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
        #self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.showMaximized()
        self.show()
        
    def mousePressEvent(self, QMouseEvent):
		self.p1x=QMouseEvent.pos().x()
		self.p1y=QMouseEvent.pos().y()
		print "Point 1 x : "+str(self.p1x)+"\nPoint 1 y : "+str(self.p1y)

    def mouseReleaseEvent(self, QMouseEvent):
		self.p2x=QMouseEvent.pos().x()
		self.p2y=QMouseEvent.pos().y()
		print "Point 2 x : "+str(self.p2x)+"\nPoint 2 y : "+str(self.p2y)
		self.setGeometry(self.p1x,self.p1y,self.p2x-self.p1x,self.p2y-self.p1y)
		#self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
		self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
		#tempW.setWindowFlags(QtCore.Qt.FramelessWindowHint)
		self.setWindowOpacity(0.5)
	


class MouseChange(QWidget):
	
	def __init__(self,parent=None):
		QWidget.__init__(self,parent)
                
	def changeCursor(self,parent):
		print parent
		parent.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))


class SystemTrayIcon(QtGui.QSystemTrayIcon):
	
	pid=-1
	parent1=None
	
	def changeCursor(self):
		self.parent1.show()
		changeMouse=MouseChange(self.parent1)
		changeMouse.changeCursor(self.parent1)
		
	def firstAction(self):
		print "Running ffmpeg"
		Process=subprocess.Popen("ffmpeg -re -f x11grab -s 1366x768 -r 30 -i 0:0 -vcodec libx264 -crf 22.5 -preset medium -s 1024x576 -r 200 -g 10 -q:v 1 -f rtsp rtsp://127.0.0.1:7070/live.sdp",shell=True)
		self.pid=Process.pid +1
		print self.pid
		print "Successfull"
		
	def secondAction(self):
		print "Second"
		
	def exitAction(self):
		print "exit"
		subprocess.call("kill "+str(self.pid),shell=True)
		sys.exit()	
		
	def fourthAction(self):
		print "Fourth"
		
	def thirdAction(self):
		print "Third"
		
	def __init__(self, icon, parent=None):
		print self.parent1
		self.parent1=parent
		print self.parent1
		QtGui.QSystemTrayIcon.__init__(self, icon, parent)
		menu = QtGui.QMenu(parent)
		menu.addAction("Start Streaming",self.firstAction)
		menu.addAction("Second",self.secondAction)
		subMenu=QtGui.QMenu("Third",menu)
		subMenu.addAction("Fourth",self.changeCursor)
		menu.addMenu(subMenu)
		menu.addAction("Exit",self.exitAction)
		self.setContextMenu(menu)
        

		
def main():
    app = QtGui.QApplication(sys.argv)
    w=widget();
    trayIcon = SystemTrayIcon(QtGui.QIcon("/home/sid/python/screenShare/favicon.ico"), w)
    trayIcon.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
