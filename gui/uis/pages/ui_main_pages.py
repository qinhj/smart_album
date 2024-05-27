# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_pages.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from gui.core.qt_core import *

class Ui_MainPages(object):
    def setupUi(self, MainPages):
        if not MainPages.objectName():
            MainPages.setObjectName(u"MainPages")
        MainPages.resize(860, 600)
        self.main_pages_layout = QVBoxLayout(MainPages)
        self.main_pages_layout.setSpacing(0)
        self.main_pages_layout.setObjectName(u"main_pages_layout")
        self.main_pages_layout.setContentsMargins(5, 5, 5, 5)
        self.pages = QStackedWidget(MainPages)
        self.pages.setObjectName(u"pages")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.page_1.setStyleSheet(u"font-size: 16pt")
        self.page_1_layout = QVBoxLayout(self.page_1)
        self.page_1_layout.setSpacing(5)
        self.page_1_layout.setObjectName(u"page_1_layout")
        self.page_1_layout.setContentsMargins(5, 5, 5, 5)
        self.welcome_base = QFrame(self.page_1)
        self.welcome_base.setObjectName(u"welcome_base")
        self.welcome_base.setMinimumSize(QSize(300, 150))
        self.welcome_base.setMaximumSize(QSize(400, 200))
        self.welcome_base.setFrameShape(QFrame.NoFrame)
        self.welcome_base.setFrameShadow(QFrame.Raised)
        self.center_page_layout = QVBoxLayout(self.welcome_base)
        self.center_page_layout.setSpacing(10)
        self.center_page_layout.setObjectName(u"center_page_layout")
        self.center_page_layout.setContentsMargins(0, 0, 0, 0)
        self.logo = QFrame(self.welcome_base)
        self.logo.setObjectName(u"logo")
        self.logo.setMinimumSize(QSize(300, 120))
        self.logo.setMaximumSize(QSize(400, 160))
        self.logo.setFrameShape(QFrame.NoFrame)
        self.logo.setFrameShadow(QFrame.Raised)
        self.logo_layout = QVBoxLayout(self.logo)
        self.logo_layout.setSpacing(0)
        self.logo_layout.setObjectName(u"logo_layout")
        self.logo_layout.setContentsMargins(0, 0, 0, 0)

        self.center_page_layout.addWidget(self.logo)

        self.label = QLabel(self.welcome_base)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.center_page_layout.addWidget(self.label)


        self.page_1_layout.addWidget(self.welcome_base, 0, Qt.AlignHCenter)

        self.pages.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setStyleSheet(u"QFrame {\n"
"	font-size: 16pt;\n"
"}")
        self.page_2_layout = QVBoxLayout(self.page_2)
        self.page_2_layout.setSpacing(5)
        self.page_2_layout.setObjectName(u"page_2_layout")
        self.page_2_layout.setContentsMargins(5, 5, 5, 5)
        self.page_2_top_widget = QWidget(self.page_2)
        self.page_2_top_widget.setObjectName(u"page_2_top_widget")

        self.page_2_layout.addWidget(self.page_2_top_widget)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.page_2_left_column_frame = QFrame(self.page_2)
        self.page_2_left_column_frame.setObjectName(u"page_2_left_column_frame")
        self.page_2_left_column_frame.setFrameShape(QFrame.StyledPanel)
        self.page_2_left_column_frame.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.page_2_left_column_frame)

        self.page_2_right_scrollArea = QScrollArea(self.page_2)
        self.page_2_right_scrollArea.setObjectName(u"page_2_right_scrollArea")
        self.page_2_right_scrollArea.setStyleSheet(u"background: transparent;")
        self.page_2_right_scrollArea.setFrameShape(QFrame.NoFrame)
        self.page_2_right_scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.page_2_right_scrollArea.setWidgetResizable(True)
        self.page_2_right_scrollAreaWidgetContents = QWidget()
        self.page_2_right_scrollAreaWidgetContents.setObjectName(u"page_2_right_scrollAreaWidgetContents")
        self.page_2_right_scrollAreaWidgetContents.setGeometry(QRect(0, 0, 832, 563))
        self.page_2_right_scrollAreaWidgetContents.setStyleSheet(u"background: transparent;")
        self.page_2_right_scrollArea.setWidget(self.page_2_right_scrollAreaWidgetContents)

        self.horizontalLayout_2.addWidget(self.page_2_right_scrollArea)


        self.page_2_layout.addLayout(self.horizontalLayout_2)

        self.pages.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setStyleSheet(u"QFrame {\n"
"	font-size: 16pt;\n"
"}")
        self.page_3_layout = QVBoxLayout(self.page_3)
        self.page_3_layout.setSpacing(5)
        self.page_3_layout.setObjectName(u"page_3_layout")
        self.page_3_layout.setContentsMargins(5, 5, 5, 5)
        self.page_3_top_widget = QWidget(self.page_3)
        self.page_3_top_widget.setObjectName(u"page_3_top_widget")

        self.page_3_layout.addWidget(self.page_3_top_widget)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.page_3_left_column_frame = QFrame(self.page_3)
        self.page_3_left_column_frame.setObjectName(u"page_3_left_column_frame")
        self.page_3_left_column_frame.setFrameShape(QFrame.StyledPanel)
        self.page_3_left_column_frame.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_3.addWidget(self.page_3_left_column_frame)

        self.page_3_right_scrollArea = QScrollArea(self.page_3)
        self.page_3_right_scrollArea.setObjectName(u"page_3_right_scrollArea")
        self.page_3_right_scrollArea.setStyleSheet(u"background: transparent;")
        self.page_3_right_scrollArea.setFrameShape(QFrame.NoFrame)
        self.page_3_right_scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.page_3_right_scrollArea.setWidgetResizable(True)
        self.page_3_right_scrollAreaWidgetContents = QWidget()
        self.page_3_right_scrollAreaWidgetContents.setObjectName(u"page_3_right_scrollAreaWidgetContents")
        self.page_3_right_scrollAreaWidgetContents.setGeometry(QRect(0, 0, 832, 563))
        self.page_3_right_scrollAreaWidgetContents.setStyleSheet(u"background: transparent;")
        self.page_3_right_scrollArea.setWidget(self.page_3_right_scrollAreaWidgetContents)

        self.horizontalLayout_3.addWidget(self.page_3_right_scrollArea)


        self.page_3_layout.addLayout(self.horizontalLayout_3)

        self.pages.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.page_4.setStyleSheet(u"QFrame {\n"
"	font-size: 16pt;\n"
"}")
        self.page_4_layout = QVBoxLayout(self.page_4)
        self.page_4_layout.setSpacing(5)
        self.page_4_layout.setObjectName(u"page_4_layout")
        self.page_4_layout.setContentsMargins(5, 5, 5, 5)
        self.page_4_top_widget = QWidget(self.page_4)
        self.page_4_top_widget.setObjectName(u"page_4_top_widget")

        self.page_4_layout.addWidget(self.page_4_top_widget)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.page_4_search_info = QFrame(self.page_4)
        self.page_4_search_info.setObjectName(u"page_4_search_info")
        self.page_4_search_info.setFrameShape(QFrame.NoFrame)
        self.page_4_search_info.setFrameShadow(QFrame.Raised)

        self.verticalLayout_4.addWidget(self.page_4_search_info)

        self.page_4_scrollArea = QScrollArea(self.page_4)
        self.page_4_scrollArea.setObjectName(u"page_4_scrollArea")
        self.page_4_scrollArea.setStyleSheet(u"background: transparent;")
        self.page_4_scrollArea.setFrameShape(QFrame.NoFrame)
        self.page_4_scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.page_4_scrollArea.setWidgetResizable(True)
        self.page_4_scrollAreaWidgetContents = QWidget()
        self.page_4_scrollAreaWidgetContents.setObjectName(u"page_4_scrollAreaWidgetContents")
        self.page_4_scrollAreaWidgetContents.setGeometry(QRect(0, 0, 838, 557))
        self.page_4_scrollAreaWidgetContents.setStyleSheet(u"background: transparent;")
        self.page_4_scrollArea.setWidget(self.page_4_scrollAreaWidgetContents)

        self.verticalLayout_4.addWidget(self.page_4_scrollArea)


        self.page_4_layout.addLayout(self.verticalLayout_4)

        self.pages.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.page_5.setStyleSheet(u"QFrame {\n"
"	font-size: 16pt;\n"
"}")
        self.page_5_layout = QVBoxLayout(self.page_5)
        self.page_5_layout.setSpacing(5)
        self.page_5_layout.setObjectName(u"page_5_layout")
        self.page_5_layout.setContentsMargins(5, 5, 5, 5)
        self.page_5_top_widget = QWidget(self.page_5)
        self.page_5_top_widget.setObjectName(u"page_5_top_widget")

        self.page_5_layout.addWidget(self.page_5_top_widget)

        self.page_5_scrollArea = QScrollArea(self.page_5)
        self.page_5_scrollArea.setObjectName(u"page_5_scrollArea")
        self.page_5_scrollArea.setStyleSheet(u"background: transparent;")
        self.page_5_scrollArea.setFrameShape(QFrame.NoFrame)
        self.page_5_scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.page_5_scrollArea.setWidgetResizable(True)
        self.page_5_scrollAreaWidgetContents = QWidget()
        self.page_5_scrollAreaWidgetContents.setObjectName(u"page_5_scrollAreaWidgetContents")
        self.page_5_scrollAreaWidgetContents.setGeometry(QRect(0, 0, 840, 565))
        self.page_5_scrollAreaWidgetContents.setStyleSheet(u"background: transparent;")
        self.page_5_scrollArea.setWidget(self.page_5_scrollAreaWidgetContents)

        self.page_5_layout.addWidget(self.page_5_scrollArea)

        self.pages.addWidget(self.page_5)

        self.main_pages_layout.addWidget(self.pages)


        self.retranslateUi(MainPages)

        self.pages.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainPages)
    # setupUi

    def retranslateUi(self, MainPages):
        MainPages.setWindowTitle(QCoreApplication.translate("MainPages", u"Form", None))
        self.label.setText(QCoreApplication.translate("MainPages", u"Welcome To Bianbu Smart Album GUI", None))
    # retranslateUi

