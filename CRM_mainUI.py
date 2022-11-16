from img.img import *
import sys
from PySide2.QtGui import QFont
from PySide2.QtWidgets import QApplication, QMainWindow, QFrame, QPushButton, QRadioButton, QGraphicsDropShadowEffect, QButtonGroup
from PySide2.QtCore import Qt, QSize

class MainUI(QMainWindow) : 
    def __init__(self) : 
        super().__init__()

        self.mainUI()

    def mainUI(self) : 
        # basic_part
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setFixedSize(1215, 678)
        self.setWindowTitle("Class_Registration_Master_v1.0")


        # body_part
        self.body_frm = QFrame(self)
        self.body_frm.setGeometry(4, 10, 1205, 644)
        self.body_frm.setStyleSheet("QFrame{\n"
                                        "background-color : #131514;\n"
                                        "border : 4px solid #8a2c2c;\n"
                                    "}")

        self.rightLine = QFrame(self.body_frm)
        self.rightLine.setGeometry(429, 0, 3, 640)

        self.topLine = QFrame(self.body_frm)
        self.topLine.setGeometry(1, 34, 431, 3)

        self.pattern_frm = QFrame(self.body_frm)
        self.pattern_frm.setGeometry(421, 4, 791, 637)
        self.pattern_frm.setStyleSheet("QFrame{\n"
                                            "image : url(:/img/tile.png);\n"
                                            "border : 0px;\n"
                                            "background-color : transparent;\n"
                                        "}")


        # menu_part
        self.info_rb = QRadioButton(self.body_frm)
        self.info_rb.setGeometry(1, 2, 147, 34)
        self.info_rb.setStyleSheet("QRadioButton::indicator{\n"
                                        "width : 147px;\n"
                                        "height : 34px;\n"
                                    "}\n"
                                    "QRadioButton::indicator::unchecked{\n"
                                        "image : url(:/img/info_rb_normal.png);\n"
                                    "}\n"
                                    "QRadioButton::indicator::hover{\n"
                                        "image : url(:/img/info_rb_hover.png);\n"
                                    "}\n"
                                    "QRadioButton::indicator::checked{\n"
                                        "image : url(:/img/info_rb_checked.png);\n"
                                    "}")

        self.prepare_rb = QRadioButton(self.body_frm)
        self.prepare_rb.setGeometry(143, 2, 147, 34)
        self.prepare_rb.setStyleSheet("QRadioButton::indicator{\n"
                                            "width : 147px;\n"
                                            "height : 34px;\n"
                                        "}\n"
                                        "QRadioButton::indicator::unchecked{\n"
                                            "image : url(:/img/prepare_rb_normal.png);\n"
                                        "}\n"
                                        "QRadioButton::indicator::hover{\n"
                                            "image : url(:/img/prepare_rb_hover.png);\n"
                                        "}\n"
                                        "QRadioButton::indicator::checked{\n"
                                            "image : url(:/img/prepare_rb_checked.png);\n"
                                        "}")

        self.finale_rb = QRadioButton(self.body_frm)
        self.finale_rb.setGeometry(285, 2, 147, 34)
        self.finale_rb.setStyleSheet("QRadioButton::indicator{\n"
                                        "width : 147px;\n"
                                        "height : 34px;\n"
                                    "}\n"
                                    "QRadioButton::indicator::unchecked{\n"
                                        "image : url(:/img/finale_rb_normal.png);\n"
                                    "}\n"
                                    "QRadioButton::indicator::hover{\n"
                                        "image : url(:/img/finale_rb_hover.png);\n"
                                    "}\n"
                                    "QRadioButton::indicator::checked{\n"
                                        "image : url(:/img/finale_rb_checked.png);\n"
                                    "}")

        self.menuGroup = QButtonGroup(self)
        self.menuGroup.addButton(self.info_rb)
        self.menuGroup.addButton(self.prepare_rb)
        self.menuGroup.addButton(self.finale_rb)





if __name__ == "__main__" : 
    app = QApplication(sys.argv)
    main = MainUI()
    main.show()
    sys.exit(app.exec_())