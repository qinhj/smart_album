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

# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
from backend.backend import backend_selector
from . functions_main_window import MainFunctions

# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from gui.core.qt_core import *

# IMPORT SETTINGS
# ///////////////////////////////////////////////////////////////
from gui.core.json_settings import Settings

# IMPORT THEME COLORS
# ///////////////////////////////////////////////////////////////
from gui.core.json_themes import Themes

# IMPORT PY ONE DARK WIDGETS
# ///////////////////////////////////////////////////////////////
from gui.widgets import *

# LOAD UI MAIN
# ///////////////////////////////////////////////////////////////
from . ui_main import * # UI_MainWindow

# MAIN FUNCTIONS 
# ///////////////////////////////////////////////////////////////
from . functions_main_window import *

# PY WINDOW
# ///////////////////////////////////////////////////////////////
class SetupMainWindow:
    def __init__(self):
        super().__init__()
        # SETUP MAIN WINDOW
        # Load widgets from "gui\uis\main_window\ui_main.py"
        # ///////////////////////////////////////////////////////////////
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)

    # ADD LEFT MENUS
    # ///////////////////////////////////////////////////////////////
    add_left_menus = [
        {
            "btn_icon" : "icon_home.svg",
            "btn_id" : "btn_home",
            "btn_text" : "首页",
            "btn_tooltip" : "首页",
            "show_top" : True,
            "is_active" : True
        },
        {
            "btn_icon": "icon_folder_open.svg",
            "btn_id": "btn_page_pics",
            "btn_text": "分类结果",
            "btn_tooltip": "分类结果",
            "show_top": True,
            "is_active": False
        },
        {
            "btn_icon": "icon_search.svg",
            "btn_id": "btn_page_search",
            "btn_text": "搜索结果",
            "btn_tooltip": "搜索结果",
            "show_top": True,
            "is_active": False
        },
        {
            "btn_icon": "icon_signal.svg",
            "btn_id": "btn_page_duplicate",
            "btn_text": "筛重结果",
            "btn_tooltip": "筛重结果",
            "show_top": True,
            "is_active": False
        }
    ]

    # ADD TITLE BAR MENUS
    # ///////////////////////////////////////////////////////////////
    add_title_bar_menus = [
        {
            "btn_icon" : "icon_search.svg",
            "btn_id" : "btn_search",
            "btn_tooltip" : "Search",
            "is_active" : False
        },
    ]

    # SETUP CUSTOM BTNs OF CUSTOM WIDGETS
    # Get sender() function when btn is clicked
    # ///////////////////////////////////////////////////////////////
    def setup_btns(self):
        if self.ui.title_bar.sender() != None:
            return self.ui.title_bar.sender()
        elif self.ui.left_menu.sender() != None:
            return self.ui.left_menu.sender()
        elif self.ui.left_column.sender() != None:
            return self.ui.left_column.sender()
        elif self.ui.left_column.menus.verticalLayout.sender() != None:
            return self.ui.left_column.menus.verticalLayout.sender()

    # SETUP MAIN WINDOW WITH CUSTOM PARAMETERS
    # ///////////////////////////////////////////////////////////////
    def setup_gui(self):
        # APP TITLE
        # ///////////////////////////////////////////////////////////////
        self.setWindowTitle(self.settings["app_name"])
        
        # REMOVE TITLE BAR
        # ///////////////////////////////////////////////////////////////
        if self.settings["custom_title_bar"]:
            self.setWindowFlag(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)

        # ADD GRIPS
        # ///////////////////////////////////////////////////////////////
        if self.settings["custom_title_bar"]:
            self.left_grip = PyGrips(self, "left", self.hide_grips)
            self.right_grip = PyGrips(self, "right", self.hide_grips)
            self.top_grip = PyGrips(self, "top", self.hide_grips)
            self.bottom_grip = PyGrips(self, "bottom", self.hide_grips)
            self.top_left_grip = PyGrips(self, "top_left", self.hide_grips)
            self.top_right_grip = PyGrips(self, "top_right", self.hide_grips)
            self.bottom_left_grip = PyGrips(self, "bottom_left", self.hide_grips)
            self.bottom_right_grip = PyGrips(self, "bottom_right", self.hide_grips)

        # LEFT MENUS / GET SIGNALS WHEN LEFT MENU BTN IS CLICKED / RELEASED
        # ///////////////////////////////////////////////////////////////
        # ADD MENUS
        self.ui.left_menu.add_menus(SetupMainWindow.add_left_menus)

        # SET SIGNALS
        self.ui.left_menu.clicked.connect(self.btn_clicked)
        self.ui.left_menu.released.connect(self.btn_released)

        # TITLE BAR / ADD EXTRA BUTTONS
        # ///////////////////////////////////////////////////////////////
        # ADD MENUS
        self.ui.title_bar.add_menus(SetupMainWindow.add_title_bar_menus)

        # SET SIGNALS
        self.ui.title_bar.clicked.connect(self.btn_clicked)
        self.ui.title_bar.released.connect(self.btn_released)

        # ADD Title
        if self.settings["custom_title_bar"]:
            self.ui.title_bar.set_title(self.settings["app_name"])
        else:
            self.ui.title_bar.set_title("Welcome to PyOneDark")

        # LEFT COLUMN SET SIGNALS
        # ///////////////////////////////////////////////////////////////
        self.ui.left_column.clicked.connect(self.btn_clicked)
        self.ui.left_column.released.connect(self.btn_released)

        # SET INITIAL PAGE / SET LEFT AND RIGHT COLUMN MENUS
        # ///////////////////////////////////////////////////////////////
        MainFunctions.set_page(self, self.ui.load_pages.page_1)
        MainFunctions.set_left_column_menu(
            self,
            menu = self.ui.left_column.menus.menu_1,
            title = "分类结果",
            icon_path = Functions.set_svg_icon("icon_folder_open.svg")
        )
        MainFunctions.set_right_column_menu(self, self.ui.right_column.menu_1)

        # ///////////////////////////////////////////////////////////////
        # EXAMPLE CUSTOM WIDGETS
        # Here are added the custom widgets to pages and columns that
        # were created using Qt Designer.
        # This is just an example and should be deleted when creating
        # your application.
        #
        # OBJECTS FOR LOAD PAGES, LEFT AND RIGHT COLUMNS
        # You can access objects inside Qt Designer projects using
        # the objects below:
        #
        # <OBJECTS>
        # LEFT COLUMN: self.ui.left_column.menus
        # RIGHT COLUMN: self.ui.right_column
        # LOAD PAGES: self.ui.load_pages
        # </OBJECTS>
        # ///////////////////////////////////////////////////////////////

        # LOAD SETTINGS
        # ///////////////////////////////////////////////////////////////
        settings = Settings()
        self.settings = settings.items

        # LOAD THEME COLOR
        # ///////////////////////////////////////////////////////////////
        themes = Themes()
        self.themes = themes.items

        # GET AND INIT AI BACKEND
        # ///////////////////////////////////////////////////////////////
        self.backend = backend_selector(self, self.settings["backend"])

        # DEFINE BTN FLAGS USED IN MainFunctions
        # ///////////////////////////////////////////////////////////////
        self.selected_image = None
        self.search_changed = False
        self.has_searched = False
        self.found_duplicate_image = False

        # ///////////////////////////////////////////////////////////////
        # ADD Buttons To Page1 For "人脸分类"
        # ///////////////////////////////////////////////////////////////
        self.func_btn_11 = PyPushButton(
            text = u"选择文件夹",
            radius = 8,
            color = self.themes["app_color"]["white"],
            bg_color = self.themes["app_color"]["dark_one"],
            bg_color_hover = self.themes["app_color"]["orange"],
            bg_color_pressed = self.themes["app_color"]["orange"]
        )
        self.func_btn_11.setMaximumWidth(200)
        self.func_btn_11.setMinimumWidth(200)
        self.func_btn_11.setMinimumHeight(40)
        self.func_btn_11.clicked.connect(lambda: MainFunctions.select_image_directory(self))
        self.ui.load_pages.func_1_frame_1_layout = QHBoxLayout(self.ui.load_pages.func_1_frame_1)
        self.ui.load_pages.func_1_frame_1_layout.addWidget(self.func_btn_11, alignment=Qt.AlignCenter)

        self.func_btn_12 = PyPushButton(
            text = u"开始分类",
            radius = 8,
            color = self.themes["app_color"]["white"],
            bg_color = self.themes["app_color"]["dark_one"],
            bg_color_hover = self.themes["app_color"]["orange"],
            bg_color_pressed = self.themes["app_color"]["orange"]
        )
        self.func_btn_12.setMaximumWidth(200)
        self.func_btn_12.setMinimumWidth(200)
        self.func_btn_12.setMinimumHeight(40)
        self.func_btn_12.clicked.connect(lambda: self.backend("Detect"))
        self.ui.load_pages.func_1_frame_2_layout = QHBoxLayout(self.ui.load_pages.func_1_frame_2)
        self.ui.load_pages.func_1_frame_2_layout.addWidget(self.func_btn_12, alignment=Qt.AlignCenter)

        # ///////////////////////////////////////////////////////////////
        # ADD Button To Page1 For "人脸搜索"
        # ///////////////////////////////////////////////////////////////
        self.func_btn_21 = PyPushButton(
            text = u"选择图片",
            radius = 8,
            color = self.themes["app_color"]["white"],
            bg_color = self.themes["app_color"]["dark_one"],
            bg_color_hover = self.themes["app_color"]["orange"],
            bg_color_pressed = self.themes["app_color"]["orange"]
        )
        self.func_btn_21.setMaximumWidth(200)
        self.func_btn_21.setMinimumWidth(200)
        self.func_btn_21.setMinimumHeight(40)
        self.func_btn_21.clicked.connect(lambda: MainFunctions.select_single_image(self))
        self.ui.load_pages.func_2_frame_1_layout = QHBoxLayout(self.ui.load_pages.func_2_frame_1)
        self.ui.load_pages.func_2_frame_1_layout.addWidget(self.func_btn_21, alignment=Qt.AlignCenter)

        self.func_btn_22 = PyPushButton(
            text = u"开始查找",
            radius = 8,
            color = self.themes["app_color"]["white"],
            bg_color = self.themes["app_color"]["dark_one"],
            bg_color_hover = self.themes["app_color"]["orange"],
            bg_color_pressed = self.themes["app_color"]["orange"]
        )
        self.func_btn_22.setMaximumWidth(200)
        self.func_btn_22.setMinimumWidth(200)
        self.func_btn_22.setMinimumHeight(40)
        self.func_btn_22.clicked.connect(lambda: self.backend("Search"))
        self.ui.load_pages.func_2_frame_2_layout = QHBoxLayout(self.ui.load_pages.func_2_frame_2)
        self.ui.load_pages.func_2_frame_2_layout.addWidget(self.func_btn_22, alignment=Qt.AlignCenter)

        # ///////////////////////////////////////////////////////////////
        # ADD Button To Page1 For "智能筛选"
        # ///////////////////////////////////////////////////////////////
        self.func_btn_31 = PyPushButton(
            text = u"开始筛重",
            radius = 8,
            color = self.themes["app_color"]["white"],
            bg_color = self.themes["app_color"]["dark_one"],
            bg_color_hover = self.themes["app_color"]["orange"],
            bg_color_pressed = self.themes["app_color"]["orange"]
        )
        self.func_btn_31.setMaximumWidth(200)
        self.func_btn_31.setMinimumWidth(200)
        self.func_btn_31.setMinimumHeight(40)
        self.func_btn_31.clicked.connect(lambda: self.backend("Duplicate"))
        self.ui.load_pages.func_3_frame_1_layout = QHBoxLayout(self.ui.load_pages.func_3_frame_1)
        self.ui.load_pages.func_3_frame_1_layout.addWidget(self.func_btn_31, alignment=Qt.AlignCenter)

        self.func_btn_32 = QFrame()
        self.func_btn_32.setStyleSheet(u"background: transparent;")
        self.func_btn_32.setMaximumWidth(200)
        self.func_btn_32.setMinimumWidth(200)
        self.func_btn_32.setMinimumHeight(40)
        self.ui.load_pages.func_3_frame_2_layout = QHBoxLayout(self.ui.load_pages.func_3_frame_2)
        self.ui.load_pages.func_3_frame_2_layout.addWidget(self.func_btn_32, alignment=Qt.AlignCenter)

        # ADD CONNECT
        self.ui.credits.person_name.returnPressed.connect(lambda: MainFunctions.exec_edit_single_group_name(self, self.ui.credits.person_name))
        #MainFunctions.load_persons(self)

        # LEFT COLUMN
        # ///////////////////////////////////////////////////////////////

        # ADD Widgets
        # ///////////////////////////////////////////////////////////////

        # RIGHT COLUMN
        # ///////////////////////////////////////////////////////////////

        # ///////////////////////////////////////////////////////////////
        # END - EXAMPLE CUSTOM WIDGETS
        # ///////////////////////////////////////////////////////////////

    # RESIZE GRIPS AND CHANGE POSITION
    # Resize or change position when window is resized
    # ///////////////////////////////////////////////////////////////
    def resize_grips(self):
        if self.settings["custom_title_bar"]:
            self.left_grip.setGeometry(5, 10, 10, self.height())
            self.right_grip.setGeometry(self.width() - 15, 10, 10, self.height())
            self.top_grip.setGeometry(5, 5, self.width() - 10, 10)
            self.bottom_grip.setGeometry(5, self.height() - 15, self.width() - 10, 10)
            self.top_right_grip.setGeometry(self.width() - 20, 5, 15, 15)
            self.bottom_left_grip.setGeometry(5, self.height() - 20, 15, 15)
            self.bottom_right_grip.setGeometry(self.width() - 20, self.height() - 20, 15, 15)
