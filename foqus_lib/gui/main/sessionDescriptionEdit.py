from foqus_lib.gui.main.sessionDescriptionEdit_UI import *
from PySide import QtGui, QtCore

class sessionDescriptionDialog(QtGui.QDialog, Ui_sessionDescriptionDialog):
	def __init__(self, parent=None, text = ""):
		QtGui.QDialog.__init__(self, parent)
		self.setupUi(self)
		self.textEdit.setHtml(text)
		self.underlineButton.clicked.connect( self.underline )
		self.overlineButton.clicked.connect( self.overline )
		self.boldButton.clicked.connect( self.bold )
		self.superscriptButton.clicked.connect( self.superscript )
		self.subscriptButton.clicked.connect( self.subscript )
		self.fontButton.clicked.connect( self.font )
		self.colorButton.clicked.connect( self.color )
		self.textEdit.currentCharFormatChanged.connect( self.getFormat )
		self.getFormat()
		
	def getFormat(self):
		self.format = self.textEdit.currentCharFormat()
		self.underlineButton.setChecked( self.format.fontUnderline() )
		self.overlineButton.setChecked( self.format.fontOverline() )
		if self.format.fontWeight() == QtGui.QFont.Bold:
			self.boldButton.setChecked( True )
		else:
			self.boldButton.setChecked( False )
		if self.format.verticalAlignment() == QtGui.QTextCharFormat.AlignSuperScript:
			self.superscriptButton.setChecked( True )
			self.subscriptButton.setChecked( False )
		elif  self.format.verticalAlignment() == QtGui.QTextCharFormat.AlignSubScript:
			self.superscriptButton.setChecked( False )
			self.subscriptButton.setChecked( True )
		else:
			self.superscriptButton.setChecked( False )
			self.subscriptButton.setChecked( False )
	
	def color(self):
		color = QtGui.QColorDialog.getColor(self.textEdit.textColor(), self)
		self.textEdit.setTextColor(color)
		self.textEdit.setFocus()
	
	def font(self):
		font, ok = QtGui.QFontDialog.getFont(self.format.font(), self)
		if ok:
			self.format.setFont(font)
			self.textEdit.setCurrentCharFormat( self.format )
			self.textEdit.setFocus()
		
	def superscript(self):
		if self.superscriptButton.isChecked():
			self.subscriptButton.setChecked(False)
			self.format.setVerticalAlignment(QtGui.QTextCharFormat.AlignSuperScript)
		else:
			self.format.setVerticalAlignment(QtGui.QTextCharFormat.AlignNormal)
		self.textEdit.setCurrentCharFormat( self.format )
		self.textEdit.setFocus()
		
				
	def subscript(self):
		if self.subscriptButton.isChecked():
			self.superscriptButton.setChecked(False)
			self.format.setVerticalAlignment(QtGui.QTextCharFormat.AlignSubScript)
		else:
			self.format.setVerticalAlignment(QtGui.QTextCharFormat.AlignNormal)
		self.textEdit.setCurrentCharFormat( self.format )
		self.textEdit.setFocus()
		
	def bold(self):
		if self.boldButton.isChecked():
			self.format.setFontWeight( QtGui.QFont.Bold )
		else:
			self.format.setFontWeight( QtGui.QFont.Normal )			
		self.textEdit.setCurrentCharFormat( self.format )
		self.textEdit.setFocus()
		
	def underline(self):
		self.format.setFontUnderline( self.underlineButton.isChecked() )
		self.textEdit.setCurrentCharFormat( self.format )
		self.textEdit.setFocus()
		
	def overline(self):
		self.format.setFontOverline( self.overlineButton.isChecked() )
		self.textEdit.setCurrentCharFormat( self.format )
		self.textEdit.setFocus()
	
	def reject(self):
		self.done( QtGui.QDialog.Rejected )
		
	def accept(self):
		self.done( QtGui.QDialog.Accepted )
	
	def html(self):
		return self.textEdit.toHtml() 