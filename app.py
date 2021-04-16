# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyPDF2 import PdfFileWriter, PdfFileReader

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(338, 374)
        Form.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 0, 311, 131))
        self.label.setPixmap(QtGui.QPixmap("headimg2.png"))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(100, 150, 231, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(20, 150, 71, 31))
        self.pushButton.setStyleSheet("background-color: rgb(218, 218, 218);")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 200, 231, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(30, 210, 61, 20))
        self.label_2.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(60, 270, 221, 31))
        self.pushButton_2.setStyleSheet("background-color: rgb(239, 63, 50);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(120, 340, 101, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(0, 240, 341, 16))
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Select PDF"))
        self.pushButton.clicked.connect(self.get_file)
        self.label_2.setText(_translate("Form", "Password :"))
        self.pushButton_2.setText(_translate("Form", "Encrypt PDF File"))
        self.pushButton_2.clicked.connect(self.encrypt)
        self.label_3.setText(_translate("Form", "@dynamic.coding"))
        self.label_4.setText(_translate("Form", "________________________________________________________"))
        
    def encrypt(self):
        input_pdf = self.lineEdit.text()
        print(input_pdf)
        output_pdf = "Encrypt.pdf"
        password = self.lineEdit_2.text()
        
        pdf_writer = PdfFileWriter()
        pdf_reader = PdfFileReader(input_pdf)
        for page in range(pdf_reader.getNumPages()):
            pdf_writer.addPage(pdf_reader.getPage(page))
        # pass the encrypt command ..
        pdf_writer.encrypt(user_pwd=password, owner_pwd=None, 
                       use_128bit=True)
        # create New pdf file and write the content into it ...
        with open(output_pdf, 'wb') as fh:
            pdf_writer.write(fh)
            
        # message box ..
        msg = QMessageBox(Form)
        msg.setWindowTitle("PDF Encrypt")
        msg.setIcon(QMessageBox.Information)
        msg.setText("Password is Added To Your Pdf")
        x = msg.exec_()
 
    
    def get_file(self):
        file , check = QFileDialog.getOpenFileName(None, "Select PDF File",
                                               "","PDF Files (*.pdf)")
        if check:
            self.lineEdit.setText(file)
        
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
