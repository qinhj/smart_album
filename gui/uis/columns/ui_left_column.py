# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from gui.core.qt_core import *


class Ui_LeftColumn(object):
    def setupUi(self, LeftColumn):
        if not LeftColumn.objectName():
            LeftColumn.setObjectName(u"LeftColumn")
        LeftColumn.resize(240, 600)
        self.main_pages_layout = QVBoxLayout(LeftColumn)
        self.main_pages_layout.setSpacing(0)
        self.main_pages_layout.setObjectName(u"main_pages_layout")
        self.main_pages_layout.setContentsMargins(5, 5, 5, 5)
        self.menus = QStackedWidget(LeftColumn)
        self.menus.setObjectName(u"menus")
        self.menu_1 = QWidget()
        self.menu_1.setObjectName(u"menu_1")
        self.menu_1_layout = QVBoxLayout(self.menu_1)
        self.menu_1_layout.setSpacing(5)
        self.menu_1_layout.setObjectName(u"menu_1_layout")
        self.menu_1_layout.setContentsMargins(5, 5, 5, 5)
        self.menus.addWidget(self.menu_1)
        self.menu_2 = QWidget()
        self.menu_2.setObjectName(u"menu_2")
        self.menu_2_layout = QVBoxLayout(self.menu_2)
        self.menu_2_layout.setSpacing(5)
        self.menu_2_layout.setObjectName(u"menu_2_layout")
        self.menu_2_layout.setContentsMargins(5, 5, 5, 5)
        self.btn_4_widget = QWidget(self.menu_2)
        self.btn_4_widget.setObjectName(u"btn_4_widget")
        self.btn_4_widget.setMinimumSize(QSize(0, 40))
        self.btn_4_widget.setMaximumSize(QSize(16777215, 40))
        self.btn_4_layout = QVBoxLayout(self.btn_4_widget)
        self.btn_4_layout.setSpacing(0)
        self.btn_4_layout.setObjectName(u"btn_4_layout")
        self.btn_4_layout.setContentsMargins(0, 0, 0, 0)

        self.menu_2_layout.addWidget(self.btn_4_widget)

        self.label_2 = QLabel(self.menu_2)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"font-size: 16pt")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.menu_2_layout.addWidget(self.label_2)

        self.label_3 = QLabel(self.menu_2)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setPointSize(9)
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"font-size: 9pt")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_3.setWordWrap(True)

        self.menu_2_layout.addWidget(self.label_3)

        self.menus.addWidget(self.menu_2)

        self.main_pages_layout.addWidget(self.menus)


        self.retranslateUi(LeftColumn)

        self.menus.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(LeftColumn)
    # setupUi

    def retranslateUi(self, LeftColumn):
        LeftColumn.setWindowTitle(QCoreApplication.translate("LeftColumn", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("LeftColumn", u"Menu 2 - Left Menu", None))
        self.label_3.setText(QCoreApplication.translate("LeftColumn", u"This is just an example menu.\n"
"Add Qt Widgets or your custom widgets here.", None))
    # retranslateUi

