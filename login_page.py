from PyQt5.QtWidgets import * # type: ignore
from registration_page_hw import registration
from menu import restoran_menu
from PyQt5.Qt import Qt
import json

class Login(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Login")

        self.main_lay=QVBoxLayout()
        self.login_lay=QHBoxLayout()
        self.passw_lay=QHBoxLayout()

        self.rest_lab=QLabel("WELCOME TO OUR SERVICE")
        self.main_lay.addWidget(self.rest_lab, alignment=Qt.AlignCenter)

        self.login_lab=QLabel("Login:")
        self.login_edit=QLineEdit()
        self.login_lay.addWidget(self.login_lab)
        self.login_lay.addWidget(self.login_edit)

        self.passw_lab=QLabel("Password:")
        self.passw_edit=QLineEdit()
        self.passw_lay.addWidget(self.passw_lab)
        self.passw_lay.addWidget(self.passw_edit)

        self.main_lay.addLayout(self.login_lay)
        self.main_lay.addLayout(self.passw_lay)

        self.submit_but=QPushButton("Submit")
        self.submit_but.clicked.connect(self.submit)
        self.main_lay.addWidget(self.submit_but)

        self.registr_but=QPushButton("SIGN UP")
        self.registr_but.clicked.connect(self.sign_up)
        self.main_lay.addWidget(self.registr_but)

        # CSS with AI
        self.resize(600, 400)

        self.setStyleSheet("""
    QWidget {
        background-color: #fff3e0; 
        font-family: 'Segoe UI', sans-serif;
    }

    QLabel {
        font-size: 18px;
        color: #6d4c41;  
        font-weight: bold;
    }

    QLineEdit {
        font-size: 18px;
        padding: 8px;
        border: 2px solid #d7ccc8; 
        border-radius: 8px;
        background-color: #fbe9e7;  
        color: #4e342e;
    }

    QPushButton {
        font-size: 18px;
        font-weight: bold;
        background-color: #ff7043;  
        color: #ffffff;
        padding: 10px 20px;
        border-radius: 10px;
    }

    QPushButton:hover {
        background-color: #f4511e;  
    }

    QPushButton:pressed {
        background-color: #bf360c;   
    }

    QMessageBox {
        background-color: #fff8e1;
        font-size: 18px;
        color: #6d4c41;
    }
""")
        
        self.main_lay.setSpacing(20)
        self.main_lay.setContentsMargins(60, 40, 60, 40)

        self.setLayout(self.main_lay)

    def submit(self):
        email=self.login_edit.text()
        password= self.passw_edit.text()
        if password and email:
            emails={}
            for i in json.load(open("users.json")):
                emails[i["email"]]=i["password"]
            if email in emails:
                if password==emails[email]:
                    self.login_edit.clear()
                    self.passw_edit.clear()
                    self.icon=QMessageBox.Information
                    self.xabar="Xush kelibsiz"
                    self.menu_win=restoran_menu(self, email)
                    self.menu_win.show()
                    self.hide()
                else:
                    self.xabar="Parol noto'g'ri. Qaytadan kiriting!"
                    self.passw_edit.clear()
            else:
                self.xabar="Bunday login ro'yhatdan o'tmagan ro'yhatdan o'ting!!!"
                self.icon=QMessageBox.Warning

        else:
            self.xabar="To'liq malumotlarni kiriting!"
            self.icon=QMessageBox.Warning
        
        self.msg=QMessageBox()
        self.msg.setWindowTitle("Login")
        self.msg.setText(self.xabar)
        self.msg.setIcon(self.icon)
        self.msg.setStyleSheet("""
    QMessageBox {
        background-color: #fff3e0;  
        font-family: 'Segoe UI', sans-serif;
        font-size: 18px;            
        color: #6d4c41;            
    }

    QMessageBox QLabel {
        font-size: 18px;
        color: #6d4c41;
        font-weight: bold;
    }

    QMessageBox QPushButton {
        font-size: 16px;
        font-weight: bold;
        background-color: #ff7043;   
        color: #ffffff;
        padding: 8px 16px;
        border-radius: 8px;
    }

    QMessageBox QPushButton:hover {
        background-color: #f4511e;  
    }

    QMessageBox QPushButton:pressed {
        background-color: #bf360c; 
    }
""")

        self.msg.show()
        self.msg.exec_()

    def sign_up(self):
        self.login_edit.clear()
        self.passw_edit.clear()
        self.hide()
        self.regist_win=registration(self)
        self.regist_win.show()





app=QApplication([])
win=Login()
win.show()
app.exec_()
