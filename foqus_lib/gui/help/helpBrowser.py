from helpBrowser_UI import *
import os
import time
import logging
from PySide import QtGui, QtCore
from foqus_lib.help.helpPath import *
from foqus_lib.gui.pysyntax_hl.pysyntax_hl import *     
try:
    import PySide.QtWebKit
    webkit = True
except:
    webkit = False

class helpBrowserDock(QtGui.QDockWidget, Ui_helpBrowser):
    #showHelpTopic = QtCore.Signal([types.StringType])
    showAbout = QtCore.Signal()
    hideHelp = QtCore.Signal()
    
    def __init__(self, parent=None, dat=None):
        '''
            Node view/edit dock widget constructor
        '''
        QtGui.QDockWidget.__init__(self, parent)
        self.setupUi(self)
        self.dat = dat
        self.mw = parent
        self.aboutButton.clicked.connect(self.showAbout.emit)
        self.contentsButton.clicked.connect(self.showContents)
        if webkit:
            self.textBrowser = PySide.QtWebKit.QWebView(self.tabWidget.widget(0))
            self.webviewLayout.addWidget(self.textBrowser)
            self.backButton.clicked.connect(self.textBrowser.back)
            self.forwardButton.clicked.connect(self.textBrowser.forward)
        self.helpPath = os.path.join(helpPath(), 'html')
        self.showContents()
        self.execButton.clicked.connect(self.runDebugCode)
        self.stopButton.clicked.connect(self.setStopTrue)
        self.loadButton.clicked.connect(self.loadDbgCode)
        self.saveButton.clicked.connect(self.saveDbgCode)
        self.ccButton.clicked.connect(self.clearCode)
        self.crButton.clicked.connect(self.clearRes)
        self.clearLogButton.clicked.connect(self.clearLogView)
        self.synhi = PythonHighlighter(self.pycodeEdit.document())
        self.stop = False
        self.timer = None
        
    def getWidget(self):
        w = self.mw.app.focusWidget()
        return w
        
    def getPopupWidget(self):
        w = self.mw.app.activePopupWidget()
        return w
        
    def getWindow(self):
        w = self.mw.app.activeWindow()
        return w
        
    def getButton(self, w, label):
        blist = w.buttons()
        #print [b.text() for b in blist]
        for b in blist:
            if b.text().replace("&", "") == label:
                return b
        return None
        
    def closeMessageBox(self):
        w = self.getWindow()
        if isinstance(w, QtGui.QMessageBox):
            w.close()
    
    def pressButton(self, w, label):
        b = self.getButton(w, label)
        if b is not None:
            b.click()
        else:
            print '{0} has no button {1}'.format(w, label)
    
    def msgBoxOK(self):
        w = self.getWindow()
        #print w
        if isinstance(w, QtGui.QMessageBox):
            self.pressButton(w, 'OK')
            
    def msgBoxYes(self):
        w = self.getWindow()
        print w
        if isinstance(w, QtGui.QMessageBox):
            self.pressButton(w, 'Yes')
            
    def msgBoxNo(self):
        w = self.getWindow()
        if isinstance(w, QtGui.QMessageBox):
            self.pressButton(w, 'No')
            
    def msgBoxCancel(self):
        w = self.getWindow()
        if isinstance(w, QtGui.QMessageBox):
            self.pressButton(w, 'Cancel')
            
    def dailogNotModal(self):
        w = self.getWindow()
        if isinstance(w, QtGui.QDialog):
            w.setModal(False)
            
    def setStopTrue(self):
        self.stop = True
        print "Stopping dbg"
        
    def loadDbgCode(self, fileName=None):
        if fileName is None:
            fileName, filtr = QtGui.QFileDialog.getOpenFileName(
                self,
                "Open File",
                "",
                "Python files (*.py);;All Files (*)")
        if fileName:
            self.clearCode()
            with open(fileName, 'r') as f:
                code = f.read()
            self.pycodeEdit.setPlainText(code)
        
    def saveDbgCode(self):
        fileName, filtr = QtGui.QFileDialog.getOpenFileName(
            self,
            "Save File",
            "",
            "Python files (*.py);;All Files (*)")
        if fileName:
            s = self.pycodeEdit.plainText()
            with open(fileName, 'r') as f:
                f.write(s)
        
    def showContents(self):
        self.setPage("{0}\content.html".format(self.helpPath))

    def setPage(self, page):
        #self.textBrowser.setSource(page)
        if webkit:
            self.textBrowser.load(PySide.QtCore.QUrl.fromLocalFile(page))
        #self.textBrowser.show()
        
    def clearCode(self):
        self.pycodeEdit.clear()
        
    def clearRes(self):
        self.resEdit.clear()
    
    def runDebugCode(self):
        self.stop = False
        pycode = self.pycodeEdit.toPlainText()
        r = self.dat.runDebugCode(pycode, self.mw)
        self.resEdit.appendPlainText(str(r))
        self.stop = False
    
    def showHelp(self):
        if webkit:
            self.updateLogView()
            self.startTimer()
        
    def closeEvent(self, ev):
        self.stopTimer()
        self.hideHelp.emit()
    
    def startTimer(self):
        '''
            Start the timer to update the log file viewer
        '''
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.updateLogView)
        self.timer.start(1000)
        
    def stopTimer(self):
        '''
            Stop the timer to update the log file viewer
        '''
        try:
            self.timer.stop()
            del self.timer
            self.timer = None
        except Exception as e:
            print "error stopping timer: {0}".format(e)
    
    def clearLogView(self):
        '''
            Clear the log text
        '''
        self.logView.clear()
        
    def timerCB(self):
        '''
            Function called by the timer to ubdate log display.
        '''
        if self.logView.isVisible():
            self.updateLogView()
        
    def updateLogView(self, maxRead=1000, delay=1000):
        '''
            Update the log viewer text box
            maxRead = the maximum number of lines to read from the log 
                at one time
        '''
        lr = 0
        if self.timer is not None:
            self.timer.stop()
        try:
            done = False
            with open(self.dat.currentLog, 'r') as f:
                f.seek(0,2)
                if self.dat.logSeek > f.tell():
                    self.dat.logSeek = 0
                f.seek(self.dat.logSeek)
                while(lr < maxRead):
                    line = f.readline()
                    self.dat.logSeek = f.tell()
                    if not line:
                        done = True
                        break
                    else:
                        lr += 1
                        self.logView.append(line.strip())
            if self.timer is not None:
                if done:
                    self.timer.start(delay) # no more to read wait a sec
                else:
                    self.timer.start(10) # more to read don't wait long
        except:
            logging.getLogger("foqus." + __name__).exception(
                "Error opening log file for log viewer, "
                "stopping the update timer")

