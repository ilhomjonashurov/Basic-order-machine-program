from PyQt5.QtWidgets import * # type: ignore
from PyQt5.Qt import Qt
import json
from information import info

class restoran_menu(QWidget):
    def __init__(self, login_win:QWidget, user):
        super().__init__()
        self.login_win=login_win
        self.user=user
        for i in json.load(open("users.json")):
            if self.user==i["email"]:
                self.info=i

        self.setWindowTitle("RESTORANT")
        self.V_main=QVBoxLayout()
        self.italian=QHBoxLayout()
        self.french=QHBoxLayout()
        self.juice=QHBoxLayout()
        self.dessert=QHBoxLayout()
        self.profile=QHBoxLayout()

        self.menu_lab=QLabel("Menu")
        self.menu_lab.setAlignment(Qt.AlignCenter)


        self.italian_lab=QLabel("Italian food🥨")
        self.french_lab=QLabel("French food🥐")
        self.juice_lab=QLabel("Juices🍹")
        self.dessert_lab=QLabel("Desserts🍰")
        
        self.labs=[self.italian_lab, self.french_lab, self.juice_lab, self.dessert_lab,]
        for i in self.labs:
            i.setAlignment(Qt.AlignCenter)


        self.Lasagna=QCheckBox("Lasagna $12")
        self.Risotto=QCheckBox("Risotto $15")
        self.Margherita_Pizza=QCheckBox("Margherita Pizza $10")
        self.Osso_Buco=QCheckBox("Osso Buco $18")
        self.Carbonara=QCheckBox("Carbonara $11")
        
        self.italian_menu=[self.Lasagna, self.Risotto, self.Margherita_Pizza, self.Osso_Buco, self.Carbonara]
        for i in self.italian_menu:
            self.italian.addWidget(i)

        self.Coq_au_Vin=QCheckBox("Coq au Vin $16")
        self.Bouillabaisse=QCheckBox("Bouillabaisse $20")
        self.Ratatouille=QCheckBox("Ratatouille $10")
        self.DuckConfit=QCheckBox("Duck Confit $18")
        self.Quiche_Lorraine=QCheckBox("Quiche Lorraine $16")

        self.french_menu=[self.Coq_au_Vin, self.Bouillabaisse, self.Ratatouille, self.DuckConfit, self.Quiche_Lorraine]
        for i in self.french_menu:
            self.french.addWidget(i)

        self.Orange_juice=QCheckBox("Orange juice $2")
        self.Pomegranate_juice=QCheckBox("Pomegranate juice $3")
        self.Carrot_juice=QCheckBox("Carrot juice $2")
        self.Apple_juice=QCheckBox("Apple juice $2")
        self.Mango_juice=QCheckBox("Mango juice $3")

        self.juice_menu=[self.Orange_juice, self.Pomegranate_juice, self.Carrot_juice, self.Apple_juice, self.Mango_juice]
        for i in self.juice_menu:
            self.juice.addWidget(i)
        
        self.Tiramisu=QCheckBox("Tiramisu $5")
        self.Crème_brûlée=QCheckBox("Crème brûlée $6")
        self.Baklava=QCheckBox("Baklava $4")
        self.Cheesecake=QCheckBox("Cheesecake $5")
        self.Gelato=QCheckBox("Gelato $3")

        self.dessert_menu=[self.Tiramisu, self.Crème_brûlée, self.Baklava, self.Cheesecake, self.Gelato]
        for i in self.dessert_menu:
            self.dessert.addWidget(i)

        self.order_but=QPushButton("Order")
        self.order_but.clicked.connect(self.order)
        self.back_but=QPushButton("Back")
        self.back_but.clicked.connect(self.back)
        self.exit_but=QPushButton("OK")
        self.exit_but.clicked.connect(exit)
        self.back_but.hide()
        self.exit_but.hide()

        self.profile_com=QComboBox()
        self.profile_com.addItems(["Profile", "Log Out"])
        self.profile_com.activated[str].connect(self.act)
        self.profile.addWidget(self.profile_com, alignment=Qt.AlignRight)


        buttons=[self.order_but, self.back_but, self.exit_but]

        self.V_main.addLayout(self.profile)
        self.V_main.addWidget(self.menu_lab)
        self.V_main.addWidget(self.italian_lab)
        self.V_main.addLayout(self.italian)
        self.V_main.addWidget(self.french_lab)
        self.V_main.addLayout(self.french)
        self.V_main.addWidget(self.juice_lab)
        self.V_main.addLayout(self.juice)
        self.V_main.addWidget(self.dessert_lab)
        self.V_main.addLayout(self.dessert)
        self.V_main.addWidget(self.order_but)
        self.V_main.addWidget(self.exit_but)
        self.V_main.addWidget(self.back_but)

        # CSS WITH AI
        self.profile_com.setFixedSize(160, 40)
        self.profile_com.setStyleSheet("""
    QComboBox {
        background-color: #ff7043;
        color: #ffffff;
        font-size: 16px;
        font-weight: bold;
        border-radius: 20px;
        padding: 4px 12px;
        border: none;
    }
    QComboBox::drop-down {
        border: none;
        width: 20px;
    }
    QComboBox QAbstractItemView {
        background-color: #fff3e0;
        selection-background-color: #ff8a65;
        border-radius: 6px;
        font-size: 14px;
        color: #4e342e;
    }
""")
        self.setStyleSheet("""
    QWidget {
        background-color: #f5e0c7;
        font-family: 'Segoe UI', sans-serif;
    }

    QLabel#menuTitle {
        font-size: 28px;
        font-weight: bold;
        color: #4e342e;
        padding: 12px;
        border-bottom: 2px solid #d2691e;
    }

    QLabel#juiceLabel {
        font-size: 20px;
        font-weight: bold;
        color: #ffffff;
        background-color: #ff9800;
        padding: 6px;
        border-radius: 8px;
    }

    QLabel#dessertLabel {
        font-size: 20px;
        font-weight: bold;
        color: #ffffff;
        background-color: #d2691e;
        padding: 6px;
        border-radius: 8px;
    }

    QCheckBox {
        font-size: 16px;
        color: #5d4037;
        spacing: 10px;
        padding: 4px;
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

    QComboBox {
        background-color: #ff7043;
        color: #ffffff;
        font-size: 16px;
        font-weight: bold;
        border-radius: 20px;
        padding: 4px 12px;
        border: none;
    }

    QComboBox::drop-down {
        border: none;
        width: 20px;
    }

    QComboBox QAbstractItemView {
        background-color: #fff3e0;
        selection-background-color: #ff8a65;
        border-radius: 6px;
        font-size: 14px;
        color: #4e342e;
    }
""")
        self.italian_lab.setStyleSheet("""
    QLabel {
        font-size: 22px;
        font-weight: bold;
        color: #ffffff;
        background-color: qlineargradient(
            spread:pad, x1:0, y1:0, x2:1, y2:0,
            stop:0 #008000, stop:0.5 #e0d7c3, stop:1 #c62828
        );
        padding: 6px;
        border-radius: 8px;
    }
""")

        self.french_lab.setStyleSheet("""
    QLabel {
        font-size: 22px;
        font-weight: bold;
        color: #ffffff;
        background-color: qlineargradient(
            spread:pad, x1:0, y1:0, x2:1, y2:0,
            stop:0 #1e3a8a, stop:0.5 #e0d7c3, stop:1 #c62828
        );
        padding: 6px;
        border-radius: 8px;
    }
""")
        for cb in self.italian_menu:
            cb.setStyleSheet("""
                QCheckBox {
                    color: #388e3c;        
                    font-size: 16px;
                    font-weight: bold;
                }
            """)

        for cb in self.french_menu:
            cb.setStyleSheet("""
                QCheckBox {
                    color: #1e3a8a;
                    font-size: 16px;
                    font-weight: bold;
                }
            """)

            for cb in self.juice_menu:
                cb.setStyleSheet("""
                    QCheckBox {
                        color: #f57c00;
                        font-size: 16px;
                        font-weight: bold;
                    }
                """)

            for cb in self.dessert_menu:
                cb.setStyleSheet("""
                    QCheckBox {
                        color: #6d4c41;
                        font-size: 16px;
                        font-weight: bold;
                    }
                """)

        self.menu_lab.setObjectName("menuTitle")
        self.italian_lab.setObjectName("italianLabel")
        self.french_lab.setObjectName("frenchLabel")
        self.juice_lab.setObjectName("juiceLabel")
        self.dessert_lab.setObjectName("dessertLabel")


        self.setLayout(self.V_main)

    
    def order(self):
        self.order_but.hide()
        self.exit_but.show()
        self.back_but.show()
        for i in self.labs:
            i.hide()
        
        for i in self.french_menu+self.italian_menu+self.juice_menu+self.dessert_menu:
            if not i.isChecked():
                i.hide()
            else:
                i.setEnabled(False)
        self.menu_lab.setText("Kamputeringdan turdani harakatdi boshlab o'zing obke🗿")

    def back(self):
        self.menu_lab.setText("RESTORANT")
        self.exit_but.hide()
        self.back_but.hide()
        self.order_but.show()
        for i in self.labs:
            i.show()
        for i in self.french_menu+self.italian_menu+self.juice_menu+self.dessert_menu:
            i.show()
            i.setEnabled(True)
    
    def act(self,but):
        if but=="Log Out":
            self.hide()
            self.login_win.show()
        else:
            self.hide()
            self.info_win=info(self, self.info)
            self.info_win.show()