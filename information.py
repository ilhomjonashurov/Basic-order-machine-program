from PyQt5.QtWidgets import * # type: ignore
from PyQt5.Qt import Qt
import json

class info(QWidget):
    def __init__(self, menu:QWidget,info:dict):
        super().__init__()
        self.menu_win=menu
        self.i=info
        self.setWindowTitle("User Information")
        
        self.name_lab=QLabel(f"""Name: {self.i["name"]}""")
        self.surname_lab=QLabel(f"""Surname: {self.i["surname"]}""")
        self.age_lab=QLabel(f"""Age: {self.i["age"]}""")
        self.gender_lab=QLabel(f"""Gender: {self.i["gender"]}""")
        self.language_lab=QLabel(f"""Language: {self.i["language"]}""")
        self.region_lab=QLabel(f"""Region: {self.i["region"]}""")
        self.district_lab=QLabel(f"""District: {self.i["district"]}""")
        self.email_lab=QLabel(f"""Email: {self.i["email"]}""")
        self.password_lab=QLabel(f"""Password: {self.i["password"]}""")
        self.labels=[self.name_lab, self.surname_lab, self.age_lab, self.gender_lab, self.language_lab, self.region_lab, self.district_lab, self.email_lab, self.password_lab,]

        self.back_but=QPushButton("Back")
        self.back_but.clicked.connect(self.back)
        self.V_main=QVBoxLayout()
        for i in self.labels:
            self.V_main.addWidget(i)
        self.V_main.addWidget(self.back_but)
        self.setLayout(self.V_main)

        # CSS WIHT AI
        self.setStyleSheet("""
    QWidget {
        background-color: #f5e0c7;
        font-family: 'Segoe UI', sans-serif;
    }
    QLabel {
        font-size: 18px;
        color: #4e342e;
        padding: 4px;
    }
    QPushButton {
        font-size: 16px;
        font-weight: bold;
        background-color: #d2691e;
        color: #ffffff;
        padding: 8px 16px;
        border-radius: 8px;
    }
    QPushButton:hover {
        background-color: #a0522d;
    }
    QPushButton:pressed {
        background-color: #7b3f00;
    }
""")

    def back(self):
        self.hide()
        self.menu_win.show()