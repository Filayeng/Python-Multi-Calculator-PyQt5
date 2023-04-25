from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextCursor


class Calculator_Class():

    def __init__(self):
        self.result = None

    def calculate(self,operation):
        operation = eval(operation)
        self.result = operation
        return self.result

    def factoriyel_op(self,number):
        multiplication = 1
        for i in range(1,number+1):
            multiplication *= i
        self.result = multiplication
        return self.result

    def foctoriyel_check(self,operation):
        operation_name = operation
        operation_name = list(operation_name)
        number = []
        min = []

        try:
            for i in range(0,len(operation_name)):
                if operation_name[i] == "!":
                    last = i-1
                    while 0<i+1:
                        if operation_name[i] == "(":
                            previous = i
                            break
                        i-=1

            for i in range(previous+1,last):
                number.append(operation_name[i])

            for i in range(previous,last+2):
                min.append(operation_name[i])

            x = len(min)
            while x>0:
                operation_name.pop(previous)
                x -=1 
                    
            number = int("".join(number))
            number = self.factoriyel_op(number)
            operation_name.insert(previous,str(number))
            operation_name = "".join(operation_name)
            self.result = self.calculate(operation_name)
            return self.result
        
        except:
            self.result = self.calculate(operation)
            return self.result
        

    def calculate_percent(self,operation):
        operation_name = operation
        operation_name = list(operation_name)
        number = []
        rate = []
        for i in range(0,len(operation_name)):
            if operation_name[i] == "%":
                for x in range(i+1,len(operation_name)):
                    rate.append(operation_name[x])
                break
                
            else:
                number.append(operation_name[i])

        number = int("".join(number))
        rate = int("".join(rate))
        self.result = (number*rate)/100
        return self.result


#//////////////////////////////////////////////////////////////////////


calculator = Calculator_Class()


class PlainTextEdit(QtWidgets.QPlainTextEdit):
    def keyPressEvent(self, event):
        if event.key() in (Qt.Key_Return, Qt.Key_Enter):
            return


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Calculator")
        Form.resize(358, 368)

        self.entered_operation = QtWidgets.QPlainTextEdit(Form)
        self.entered_operation.setGeometry(QtCore.QRect(20, 50, 321, 41))
        self.entered_operation.setStyleSheet("font: 15pt \"MS Reference Sans Serif\";")
        self.entered_operation.setObjectName("entered_operation")


        self.btn_0 = QtWidgets.QPushButton(Form)
        self.btn_0.setGeometry(QtCore.QRect(100, 310, 81, 51))
        self.btn_0.setStyleSheet("font: 20pt \"Arial\";")
        self.btn_0.setObjectName("btn_0")
        self.btn_0.clicked.connect(self.num_0)

        self.btn_1 = QtWidgets.QPushButton(Form)
        self.btn_1.setGeometry(QtCore.QRect(20, 160, 81, 51))
        self.btn_1.setStyleSheet("font: 20pt \"Arial\";")
        self.btn_1.setObjectName("btn_1")
        self.btn_1.clicked.connect(self.num_1)

        self.btn_2 = QtWidgets.QPushButton(Form)
        self.btn_2.setGeometry(QtCore.QRect(100, 160, 81, 51))
        self.btn_2.setStyleSheet("font: 20pt \"Arial\";")
        self.btn_2.setObjectName("btn_2")
        self.btn_2.clicked.connect(self.num_2)

        self.btn_3 = QtWidgets.QPushButton(Form)
        self.btn_3.setGeometry(QtCore.QRect(180, 160, 81, 51))
        self.btn_3.setStyleSheet("font: 20pt \"Arial\";")
        self.btn_3.setObjectName("btn_3")
        self.btn_3.clicked.connect(self.num_3)

        self.btn_4 = QtWidgets.QPushButton(Form)
        self.btn_4.setGeometry(QtCore.QRect(20, 210, 81, 51))
        self.btn_4.setStyleSheet("font: 20pt \"Arial\";")
        self.btn_4.setObjectName("btn_4")
        self.btn_4.clicked.connect(self.num_4)

        self.btn_5 = QtWidgets.QPushButton(Form)
        self.btn_5.setGeometry(QtCore.QRect(100, 210, 81, 51))
        self.btn_5.setStyleSheet("font: 20pt \"Arial\";")
        self.btn_5.setObjectName("btn_5")
        self.btn_5.clicked.connect(self.num_5)

        self.btn_6 = QtWidgets.QPushButton(Form)
        self.btn_6.setGeometry(QtCore.QRect(180, 210, 81, 51))
        self.btn_6.setStyleSheet("font: 20pt \"Arial\";")
        self.btn_6.setObjectName("btn_6")
        self.btn_6.clicked.connect(self.num_6)

        self.btn_7 = QtWidgets.QPushButton(Form)
        self.btn_7.setGeometry(QtCore.QRect(20, 260, 81, 51))
        self.btn_7.setStyleSheet("font: 20pt \"Arial\";")
        self.btn_7.setObjectName("btn_7")
        self.btn_7.clicked.connect(self.num_7)

        self.btn_8 = QtWidgets.QPushButton(Form)
        self.btn_8.setGeometry(QtCore.QRect(100, 260, 81, 51))
        self.btn_8.setStyleSheet("font: 20pt \"Arial\";")
        self.btn_8.setObjectName("btn_8")
        self.btn_8.clicked.connect(self.num_8)

        self.btn_9 = QtWidgets.QPushButton(Form)
        self.btn_9.setGeometry(QtCore.QRect(180, 260, 81, 51))
        self.btn_9.setStyleSheet("font: 20pt \"Arial\";")
        self.btn_9.setObjectName("btn_9")
        self.btn_9.clicked.connect(self.num_9)


        self.addition_btn = QtWidgets.QPushButton(Form)
        self.addition_btn.setGeometry(QtCore.QRect(260, 160, 41, 51))
        self.addition_btn.setStyleSheet("font: 20pt \"Arial\";")
        self.addition_btn.setObjectName("addition_btn")
        self.addition_btn.clicked.connect(self.additionBtn)

        self.subtraction_btn = QtWidgets.QPushButton(Form)
        self.subtraction_btn.setGeometry(QtCore.QRect(300, 160, 41, 51))
        self.subtraction_btn.setStyleSheet("font: 20pt \"Arial\";")
        self.subtraction_btn.setObjectName("subtraction_btn")
        self.subtraction_btn.clicked.connect(self.subtractionBtn)

        self.division_btn = QtWidgets.QPushButton(Form)
        self.division_btn.setGeometry(QtCore.QRect(300, 210, 41, 51))
        self.division_btn.setStyleSheet("font: 20pt \"Arial\";")
        self.division_btn.setObjectName("division_btn")
        self.division_btn.clicked.connect(self.divisionBtn)

        self.multiplication_btn = QtWidgets.QPushButton(Form)
        self.multiplication_btn.setGeometry(QtCore.QRect(260, 210, 41, 51))
        self.multiplication_btn.setStyleSheet("font: 20pt \"Arial\";")
        self.multiplication_btn.setObjectName("multiplication_btn")
        self.multiplication_btn.clicked.connect(self.multiplicationBtn)


        self.exponentiation_btn = QtWidgets.QPushButton(Form)
        self.exponentiation_btn.setGeometry(QtCore.QRect(100, 110, 81, 51))
        self.exponentiation_btn.setStyleSheet("font: 20pt \"Arial\";")
        self.exponentiation_btn.setObjectName("exponentiation_btn")
        self.exponentiation_btn.clicked.connect(self.exponentiationBtn)

        self.sqrt_btn = QtWidgets.QPushButton(Form)
        self.sqrt_btn.setGeometry(QtCore.QRect(180, 110, 81, 51))
        self.sqrt_btn.setStyleSheet("font: 15pt \"Arial\";")
        self.sqrt_btn.setObjectName("sqrt_btn")
        self.sqrt_btn.clicked.connect(self.sqrtBtn)

        self.factoriyel_btn = QtWidgets.QPushButton(Form)
        self.factoriyel_btn.setGeometry(QtCore.QRect(260, 260, 41, 51))
        self.factoriyel_btn.setStyleSheet("font: 20pt \"Arial\";")
        self.factoriyel_btn.setObjectName("factoriyel_btn")
        self.factoriyel_btn.clicked.connect(self.fktBtn)        

        self.percent_btn = QtWidgets.QPushButton(Form)
        self.percent_btn.setGeometry(QtCore.QRect(20, 310, 81, 51))
        self.percent_btn.setStyleSheet("font: 20pt \"Arial\";")
        self.percent_btn.setObjectName("percent_btn")
        self.percent_btn.clicked.connect(self.pencentageBtn)

        self.point_btn = QtWidgets.QPushButton(Form)
        self.point_btn.setGeometry(QtCore.QRect(180, 310, 81, 51))
        self.point_btn.setStyleSheet("font: 20pt \"Arial\";")
        self.point_btn.setObjectName("point_btn")
        self.point_btn.clicked.connect(self.pointBtn)

        
        self.clear_btn = QtWidgets.QPushButton(Form)
        self.clear_btn.setGeometry(QtCore.QRect(20, 110, 81, 51))
        self.clear_btn.setStyleSheet("font: 20pt \"Arial\";")
        self.clear_btn.setObjectName("clear_btn")
        self.clear_btn.clicked.connect(self.clear_Operation)

        self.delete_btn = QtWidgets.QPushButton(Form)
        self.delete_btn.setGeometry(QtCore.QRect(260, 110, 81, 51))
        self.delete_btn.setStyleSheet("font: 20pt \"Arial\";")
        self.delete_btn.setObjectName("delete_btn")
        self.delete_btn.clicked.connect(self.OBO_delete)

        self.equals_btn = QtWidgets.QPushButton(Form)
        self.equals_btn.setGeometry(QtCore.QRect(300, 260, 41, 101))
        self.equals_btn.setStyleSheet("font: 20pt \"Arial\";")
        self.equals_btn.setObjectName("equals_btn")
        self.equals_btn.setShortcut("Enter")
        self.equals_btn.clicked.connect(self.complete_Operation)

        self.free_btn = QtWidgets.QPushButton(Form)
        self.free_btn.setGeometry(QtCore.QRect(260, 310, 41, 51))
        self.free_btn.setStyleSheet("font: 20pt \"Arial\";")
        self.free_btn.setText("")
        self.free_btn.setObjectName("free_btn")

        self.last_operation = QtWidgets.QLineEdit(Form)
        self.last_operation.setEnabled(False)
        self.last_operation.setGeometry(QtCore.QRect(20, 20, 321, 22))
        self.last_operation.setObjectName("lineEdit")


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

        self.btn_0.setText(_translate("Form", "0"))
        self.btn_1.setText(_translate("Form", "1"))
        self.btn_2.setText(_translate("Form", "2"))
        self.btn_3.setText(_translate("Form", "3"))
        self.btn_5.setText(_translate("Form", "5"))
        self.btn_4.setText(_translate("Form", "4"))
        self.btn_6.setText(_translate("Form", "6"))
        self.btn_7.setText(_translate("Form", "7"))
        self.btn_8.setText(_translate("Form", "8"))
        self.btn_9.setText(_translate("Form", "9"))

        self.addition_btn.setText(_translate("Form", "+"))
        self.subtraction_btn.setText(_translate("Form", "-"))
        self.multiplication_btn.setText(_translate("Form", "*"))
        self.division_btn.setText(_translate("Form", "/"))

        self.exponentiation_btn.setText(_translate("Form", "x²"))
        self.sqrt_btn.setText(_translate("Form", "√x"))
        self.factoriyel_btn.setText(_translate("Form", "()!"))
        self.percent_btn.setText(_translate("Form", "%"))
        self.point_btn.setText(_translate("Form", "."))

        self.clear_btn.setText(_translate("Form", "C"))
        self.delete_btn.setText(_translate("Form", "<--"))
        
        self.equals_btn.setText(_translate("Form", "="))





    def num_1(self):
        self.entered_operation.insertPlainText("1")

    def num_2(self):
        self.entered_operation.insertPlainText("2")

    def num_3(self):
        self.entered_operation.insertPlainText("3")

    def num_4(self):
        self.entered_operation.insertPlainText("4")

    def num_5(self):
        self.entered_operation.insertPlainText("5")

    def num_6(self):
        self.entered_operation.insertPlainText("6")

    def num_7(self):
        self.entered_operation.insertPlainText("7")

    def num_8(self):
        self.entered_operation.insertPlainText("8")

    def num_9(self):
        self.entered_operation.insertPlainText("9")

    def num_0(self):
        self.entered_operation.insertPlainText("0")

    def exponentiationBtn(self):
        self.entered_operation.insertPlainText("**2")
    
    def sqrtBtn(self):
        self.entered_operation.insertPlainText("**0.5")

    def pencentageBtn(self):
        self.entered_operation.insertPlainText("%")
        self.exponentiation_btn.setEnabled(False)
        self.sqrt_btn.setEnabled(False)
        self.addition_btn.setEnabled(False)
        self.subtraction_btn.setEnabled(False)
        self.multiplication_btn.setEnabled(False)
        self.division_btn.setEnabled(False)
        self.factoriyel_btn.setEnabled(False)
        self.point_btn.setEnabled(False)
        self.percent_btn.setEnabled(False)

    
    def additionBtn(self):
        self.entered_operation.insertPlainText("+")

    def subtractionBtn(self):
        self.entered_operation.insertPlainText("-")

    def multiplicationBtn(self):
        self.entered_operation.insertPlainText("*")

    def divisionBtn(self):
        self.entered_operation.insertPlainText("/")

    def pointBtn(self):
        self.entered_operation.insertPlainText(".")

    def fktBtn(self):
        self.entered_operation.insertPlainText("()!")


    def clear_Operation(self):
        self.exponentiation_btn.setEnabled(True)
        self.multiplication_btn.setEnabled(True)
        self.subtraction_btn.setEnabled(True)
        self.factoriyel_btn.setEnabled(True)
        self.division_btn.setEnabled(True)
        self.addition_btn.setEnabled(True)
        self.percent_btn.setEnabled(True)
        self.point_btn.setEnabled(True)
        self.sqrt_btn.setEnabled(True)
        self.entered_operation.clear()


    def OBO_delete(self):
        operation = self.entered_operation.toPlainText()
        operation = list(operation)
        if len(operation) > 0:
            operation.pop(-1)
            operation = "".join(operation)
            self.entered_operation.clear()
            self.entered_operation.setPlainText(operation)
            self.entered_operation.textCursor().setPosition(len(operation))
    
        

    def complete_Operation(self):

        operation = self.entered_operation.toPlainText()

        for i in list(operation):
            if i == "%":
                rslt = str(calculator.calculate_percent(operation))
                self.last_operation.setText(operation)
                self.entered_operation.setPlainText(rslt)
                break

            elif i == "!":
                rslt = str(calculator.foctoriyel_check(operation))
                self.last_operation.setText(operation)
                self.entered_operation.setPlainText(rslt)

            else:
                rslt = str(calculator.foctoriyel_check(operation))
                self.last_operation.setText(operation)
                self.entered_operation.setPlainText(rslt)

        self.exponentiation_btn.setEnabled(True)
        self.multiplication_btn.setEnabled(True)
        self.subtraction_btn.setEnabled(True)
        self.factoriyel_btn.setEnabled(True)
        self.division_btn.setEnabled(True)
        self.addition_btn.setEnabled(True)
        self.percent_btn.setEnabled(True)
        self.point_btn.setEnabled(True)
        self.sqrt_btn.setEnabled(True)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())