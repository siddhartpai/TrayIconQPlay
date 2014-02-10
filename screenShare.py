import sys
from PyQt4 import QtGui

class SystemTrayIcon(QtGui.QSystemTrayIcon):

	def firstAction(self):
		print "First"
	def secondAction(self):
		print "Second"
	def exitAction(self):
		print "exit"
		exit()	
	def fourthAction(self):
		print "Fourth"
	def thirdAction(self):
		print "Third"
	def __init__(self, icon, parent=None):
		QtGui.QSystemTrayIcon.__init__(self, icon, parent)
		menu = QtGui.QMenu(parent)
		menu.addAction("First",self.firstAction)
		menu.addAction("Second",self.secondAction)
		subMenu=QtGui.QMenu("Third",menu)
		subMenu.addAction("Fourth",self.fourthAction)
		menu.addMenu(subMenu)
		menu.addAction("Exit",self.exitAction)
		self.setContextMenu(menu)
        

		
def main():
    app = QtGui.QApplication(sys.argv)

    w = QtGui.QWidget()
    trayIcon = SystemTrayIcon(QtGui.QIcon("favicon.ico"), w)

    trayIcon.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
