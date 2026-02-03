from PyQt5.QtWidgets import * # type: ignore
from PyQt5.Qt import Qt
import json

class registration(QWidget):
    def __init__(self, win:QWidget):
        super().__init__()
        self.login_win=win

        self.setWindowTitle("Registration")

        self.V_main=QVBoxLayout()
        self.h_name=QHBoxLayout()
        self.h_surname=QHBoxLayout()
        self.h_age=QHBoxLayout()
        self.h_gender=QHBoxLayout()
        self.h_language=QHBoxLayout()
        self.h_region=QHBoxLayout()
        self.h_district=QHBoxLayout()
        self.h_email=QHBoxLayout()
        self.h_passw=QHBoxLayout()
        
        self.regist_lab=QLabel("Registration")


        self.name_lab=QLabel("Name:")
        self.name_edit=QLineEdit()
        self.name_edit.setPlaceholderText("Eric")
        self.h_name.addWidget(self.name_lab)
        self.h_name.addWidget(self.name_edit)

        self.surname_lab=QLabel("Surname:")
        self.surname_edit=QLineEdit()
        self.surname_edit.setPlaceholderText("Richard")
        self.h_surname.addWidget(self.surname_lab)
        self.h_surname.addWidget(self.surname_edit)

        self.age_lab=QLabel("Age:")
        self.age_edit=QLineEdit()
        self.age_edit.setPlaceholderText("18")
        self.h_age.addWidget(self.age_lab)
        self.h_age.addWidget(self.age_edit)

        self.gender_m=QRadioButton("Male")
        self.gender_f=QRadioButton("Female")
        self.h_gender.addWidget(self.gender_f)
        self.h_gender.addWidget(self.gender_m)

        self.language_lab=QLabel("Language:")
        self.uzb_lab=QCheckBox("UZB")
        self.eng_lab=QCheckBox("ENG")
        self.rus_lab=QCheckBox("RUS")
        self.h_language.addWidget(self.language_lab)
        self.h_language.addWidget(self.uzb_lab)
        self.h_language.addWidget(self.eng_lab)
        self.h_language.addWidget(self.rus_lab)

        self.regions=["Andijon", "Buxoro", "Farg'ona", "Jizzax", "Namangan", "Navoiy", 
                    "Qashqadaryo","Samarqand", "Sirdaryo", "Surxondaryo", "Toshkent viloyati", "Xorazm", "Toshkent shahar"]

        self.region_lab=QLabel("Region:")
        self.region_com=QComboBox()
        self.region_com.addItem("Select region")
        self.region_com.addItems(self.regions)
        self.region_com.model().item(0).setEnabled(False) # type: ignore
        self.region_com.activated[str].connect(self.tumanlar)
        self.h_region.addWidget(self.region_lab)
        self.h_region.addWidget(self.region_com)

        self.district_lab=QLabel("District:")
        self.district_com=QComboBox()
        self.h_district.addWidget(self.district_lab)
        self.h_district.addWidget(self.district_com)

        self.email_lab=QLabel("Email:")
        self.email_edit=QLineEdit()
        self.h_email.addWidget(self.email_lab)
        self.h_email.addWidget(self.email_edit)

        self.passw_lab=QLabel("Password:")
        self.passw_edit=QLineEdit()
        self.h_passw.addWidget(self.passw_lab)
        self.h_passw.addWidget(self.passw_edit)

        self.back_but=QPushButton("Back")
        self.back_but.clicked.connect(self.back)

        self.submit_but=QPushButton("Submit")
        self.submit_but.clicked.connect(self.user)

        self.labels=[self.name_lab, self.surname_lab, self.age_lab, self.region_lab, self.district_lab, self.email_lab, self.passw_lab]

        self.layouts=[self.h_name, self.h_surname, self.h_age, self.h_gender, self.h_language, self.h_region, self.h_district, self.h_email, self.h_passw]

        self.editors=[self.name_edit, self.surname_edit, self.age_edit, self.email_edit, self.passw_edit]
        self.V_main.addWidget(self.regist_lab)
        for i in self.layouts:
            self.V_main.addLayout(i)


        self.V_main.addWidget(self.submit_but)

        self.V_main.addWidget(self.back_but)

        #CSS WITH AI
        self.resize(180, 150)

        self.setStyleSheet("""
    QWidget {
        background-color: #f5e0c7;
        font-family: 'Segoe UI', sans-serif;
    }

    QLabel {
        font-size: 20px;
        color: #5d4037;   
        font-weight: bold;
    }

    QLineEdit {
        font-size: 18px;
        padding: 10px;
        border: 2px solid #a1887f;
        border-radius: 8px;
        background-color: #f0d9b5; 
        color: #3e2723;
        min-width: 250px;
    }

    QComboBox {
        font-size: 18px;
        padding: 8px;
        border: 2px solid #a1887f;
        border-radius: 8px;
        background-color: #f0d9b5;
        color: #3e2723;
        min-width: 150px;
    }

    QRadioButton, QCheckBox {
        font-size: 16px;
        color: #5d4037;
    }

    QPushButton {
        font-size: 18px;
        font-weight: bold;
        background-color: #d2691e; 
        color: #ffffff;
        padding: 12px 24px;
        border-radius: 10px;
    }

    QPushButton:hover {
        background-color: #a0522d;   
    }

    QPushButton:pressed {
        background-color: #7b3f00;  
    }

    QMessageBox {
        background-color: #f5e0c7;
        font-size: 18px;
        color: #5d4037;
    }
""")

        self.setLayout(self.V_main)

    def tumanlar(self, obj):
        self.district_com.clear()
        self.stricts={
    "Andijon": ["Asaka","Baliqchi","Bo'z","Buloqboshi","Izboskan","Jalaquduq","Marhamat","Oltinko'l","Paxtaobod","Qo'rg'ontepa","Shahrixon","Ulug'nor","Xo'jaobod"],
    "Buxoro": ["Buxoro","G'ijduvon","Jondor","Kogon","Olot","Peshku","Qorako'l","Qorovulbozor","Romitan","Shofirkon","Vobkent"],
    "Farg'ona": ["Oltiariq","Bag'dod","Beshariq","Dang'ara","Furqat","Qo'qon","Quva","Quvasoy","Rishton","So'x","Toshloq","Uchko'prik","Yozyovon"],
    "Jizzax": ["Arnasoy","Baxmal","Do'stlik","Forish","G'allaorol","Mirzacho'l","Paxtakor","Yangiobod","Zafarobod","Zarbdor"],
    "Namangan": ["Chortoq","Chust","Kosonsoy","Mingbuloq","Norin","Pop","To'raqo'rg'on","Uchqo'rg'on","Yangiqo'rg'on"],
    "Navoiy": ["Konimex","Karmana","Navbahor","Nurota","Qiziltepa","Tomdi","Uchquduq","Xatirchi"],
    "Qashqadaryo": ["Chiroqchi","Dehqonobod","G'uzor","Kasbi","Kitob","Koson","Mirishkor","Muborak","Nishon","Qamashi","Shahrisabz","Yakkabog'"],
    "Samarqand": ["Bulung'ur","Ishtixon","Jomboy","Kattaqo'rg'on","Narpay","Nurobod","Oqdaryo","Paxtachi","Payariq","Pastdarg'om","Qo'shrabot","Tayloq","Urgut"],
    "Sirdaryo": ["Boyovut","Hovos","Mirzaobod","Oqoltin","Sardoba","Sayxunobod","Shirin","Sirdaryo","Yangiyer"],
    "Surxondaryo": ["Angor","Bandixon","Boysun","Denov","Jarqo'rg'on","Qiziriq","Qumqo'rg'on","Muzrabot","Oltinsoy","Sariosiyo","Sherobod","Sho'rchi"],
    "Toshkent viloyati": ["Bekobod","Bo'stonliq","Chinoz","Qibray","Oqqo'rg'on","Ohangaron","Parkent","Piskent","Quyi Chirchiq","Toshkent tumani","Yangiyo'l","Yuqori Chirchiq","Zangiota"],
    "Xorazm": ["Bog'ot","Gurlan","Hazorasp","Xiva","Qo'shko'pir","Shovot","Xonqa","Yangiariq","Yangibozor"],
    "Toshkent shahar": ["Bektemir","Chilonzor","Mirzo Ulug'bek","Mirobod","Olmazor","Shayxontohur","Sirg'ali","Uchtepa","Yakkasaroy","Yashnobod","Yunusobod"]
}
        self.district_com.addItems(self.stricts[obj])

    def user(self):
        name=self.name_edit.text()
        surname=self.surname_edit.text()
        age=self.age_edit.text()
        gender=""
        email=self.email_edit.text()
        passw=self.passw_edit.text()
        if self.gender_f.isChecked() or self.gender_m.isChecked():
            gender="Male" if self.gender_m.isChecked() else "Female"
        uzb=''
        rus=''
        eng=''
        if self.uzb_lab.isChecked():
            uzb="UZB"
        if self.eng_lab.isChecked():
            eng="ENG"
        if self.rus_lab.isChecked():
            rus="RUS"
        language=uzb+" "+rus+" "+eng
        region=self.region_com.currentText()
        district=self.district_com.currentText()


        if name and surname and age and gender and language.strip() and region and district and email and passw:
            if not email[-9:] == "gmail.com":
                self.xabar="Gmailni to'g'ri kiriting!"
                self.icon=QMessageBox.Critical
            elif not len(passw)>=8:
                self.xabar="Password 8ta simboldan iborat bo'lishi kerak!"
                self.icon=QMessageBox.Warning
            else:
                with open("users.json", "r+") as f:
                    users=json.load(f)
                    f.seek(0)
                    users.append({
                        "name":name,
                        "surname":surname,
                        "age":age,
                        "gender":gender,
                        "language":language.split(),
                        "region":region,
                        "district":district,
                        "email": email,
                        "password": passw
                    })
                    json.dump(users, f, indent=4)
                    f.close()
                self.xabar="Siz ro'yhatdan o'tdingiz!"
                self.icon=QMessageBox.Information
                self.hide()
                self.login_win.show()
                self.login_win.login_edit.setText(email)
                self.login_win.passw_edit.setText(passw)

        else:
            self.xabar="Hamma malumotlarni to'ldiring!"
            self.icon=QMessageBox.Warning
        
        self.msg=QMessageBox()
        self.msg.setWindowTitle("Registration")
        self.msg.setText(self.xabar)
        self.msg.setIcon(self.icon)
        self.msg.setStyleSheet("""
    QMessageBox {
        background-color: #f5e0c7;
        font-family: 'Segoe UI', sans-serif;
    }
    QMessageBox QLabel {
        font-size: 18px;
        color: #5d4037;
        font-weight: bold;
    }
    QMessageBox QPushButton {
        font-size: 16px;
        font-weight: bold;
        background-color: #d2691e;
        color: #ffffff;
        padding: 8px 16px;
        border-radius: 8px;
    }
    QMessageBox QPushButton:hover {
        background-color: #a0522d;
    }
    QMessageBox QPushButton:pressed {
        background-color: #7b3f00;
    }
""")
        self.msg.setText(self.xabar)
        self.msg.setIcon(self.icon)
        self.msg.exec_()

    def back(self):
        self.hide()
        self.login_win.show()