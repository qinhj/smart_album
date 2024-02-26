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
            "btn_id": "btn_page_face_cluster",
            "btn_text": "人物列表",
            "btn_tooltip": "人物列表",
            "show_top": True,
            "is_active": False
        },
        {
            "btn_icon": "icon_search.svg",
            "btn_id": "btn_page_image_search",
            "btn_text": "搜图结果",
            "btn_tooltip": "搜图结果",
            "show_top": True,
            "is_active": False
        },
        {
            "btn_icon": "icon_signal.svg",
            "btn_id": "btn_page_image_similarity",
            "btn_text": "相似图片",
            "btn_tooltip": "相似图片",
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
        elif self.ui.left_column.menus.menu_1_layout.sender() != None:
            return self.ui.left_column.menus.menu_1_layout.sender()

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
        # ADD LINE EDIT TO MENU FOR CUSTOM SEARCH
        self.search_text = PyLineEdit(place_holder_text = u"文搜图")
        self.search_text.setAlignment(Qt.AlignLeft)
        self.search_text.setReadOnly(False)
        self.ui.title_bar.custom_buttons_layout.addWidget(self.search_text)
        def search_text_slot(text):
            print("Input test: {}".format(self.search_text.text()))
            self.selected_image = text
            self.backend("image_search")
        self.search_text.returnPressed.connect(lambda: search_text_slot(self.search_text.text()))
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
            title = "人物列表",
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
        # Face Cluster
        self.person_list_btn_group = None
        self.image_page_dict_person = {}
        # Image Search
        self.selected_image = None
        self.image_search_changed = False
        self.image_search_done = False
        self.image_search_result = {}
        # Image Similarity
        self.image_similarity_done = False
        self.image_similarity_result = []
        self.image_similarity_pages = []

        # LEFT COLUMN
        # ///////////////////////////////////////////////////////////////

        # ADD WIDGETS: Person List Placeholder
        self.ui.left_column.menus.menu_1_layout.addWidget(QWidget())

        # PAGES
        # ///////////////////////////////////////////////////////////////

        # ///////////////////////////////////////////////////////////////
        # PAGE 1 - ADD BUTTON FOR "人脸分类"
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
        self.func_btn_12.clicked.connect(lambda: self.backend("face_cluster"))
        self.ui.load_pages.func_1_frame_2_layout = QHBoxLayout(self.ui.load_pages.func_1_frame_2)
        self.ui.load_pages.func_1_frame_2_layout.addWidget(self.func_btn_12, alignment=Qt.AlignCenter)

        self.func_btn_13 = QFrame()
        self.func_btn_13.setStyleSheet(u"background: transparent;")
        self.func_btn_13.setMaximumWidth(200)
        self.func_btn_13.setMinimumWidth(200)
        self.func_btn_13.setMinimumHeight(40)
        self.ui.load_pages.func_1_frame_3_layout = QHBoxLayout(self.ui.load_pages.func_1_frame_3)
        self.ui.load_pages.func_1_frame_3_layout.addWidget(self.func_btn_13, alignment=Qt.AlignCenter)

        # ///////////////////////////////////////////////////////////////
        # PAGE 1 - ADD BUTTON FOR "以图搜图"
        # ///////////////////////////////////////////////////////////////
        self.func_btn_21 = PyPushButton(
            text = u"选择文件夹",
            radius = 8,
            color = self.themes["app_color"]["white"],
            bg_color = self.themes["app_color"]["dark_one"],
            bg_color_hover = self.themes["app_color"]["orange"],
            bg_color_pressed = self.themes["app_color"]["orange"]
        )
        self.func_btn_21.setMaximumWidth(200)
        self.func_btn_21.setMinimumWidth(200)
        self.func_btn_21.setMinimumHeight(40)
        self.func_btn_21.clicked.connect(lambda: MainFunctions.select_image_directory(self))
        self.ui.load_pages.func_2_frame_1_layout = QHBoxLayout(self.ui.load_pages.func_2_frame_1)
        self.ui.load_pages.func_2_frame_1_layout.addWidget(self.func_btn_21, alignment=Qt.AlignCenter)

        self.func_btn_22 = PyPushButton(
            text = u"选择图片",
            radius = 8,
            color = self.themes["app_color"]["white"],
            bg_color = self.themes["app_color"]["dark_one"],
            bg_color_hover = self.themes["app_color"]["orange"],
            bg_color_pressed = self.themes["app_color"]["orange"]
        )
        self.func_btn_22.setMaximumWidth(200)
        self.func_btn_22.setMinimumWidth(200)
        self.func_btn_22.setMinimumHeight(40)
        self.func_btn_22.clicked.connect(lambda: MainFunctions.select_single_image(self))
        self.ui.load_pages.func_2_frame_2_layout = QHBoxLayout(self.ui.load_pages.func_2_frame_2)
        self.ui.load_pages.func_2_frame_2_layout.addWidget(self.func_btn_22, alignment=Qt.AlignCenter)

        self.func_btn_23 = PyPushButton(
            text = u"开始查找",
            radius = 8,
            color = self.themes["app_color"]["white"],
            bg_color = self.themes["app_color"]["dark_one"],
            bg_color_hover = self.themes["app_color"]["orange"],
            bg_color_pressed = self.themes["app_color"]["orange"]
        )
        self.func_btn_23.setMaximumWidth(200)
        self.func_btn_23.setMinimumWidth(200)
        self.func_btn_23.setMinimumHeight(40)
        self.func_btn_23.clicked.connect(lambda: self.backend("image_search"))
        self.ui.load_pages.func_2_frame_3_layout = QHBoxLayout(self.ui.load_pages.func_2_frame_3)
        self.ui.load_pages.func_2_frame_3_layout.addWidget(self.func_btn_23, alignment=Qt.AlignCenter)

        # ///////////////////////////////////////////////////////////////
        # PAGE 1 - ADD BUTTON FOR "智能分析"
        # ///////////////////////////////////////////////////////////////
        self.func_btn_31 = PyPushButton(
            text = u"选择文件夹",
            radius = 8,
            color = self.themes["app_color"]["white"],
            bg_color = self.themes["app_color"]["dark_one"],
            bg_color_hover = self.themes["app_color"]["orange"],
            bg_color_pressed = self.themes["app_color"]["orange"]
        )
        self.func_btn_31.setMaximumWidth(200)
        self.func_btn_31.setMinimumWidth(200)
        self.func_btn_31.setMinimumHeight(40)
        self.func_btn_31.clicked.connect(lambda: MainFunctions.select_image_directory(self))
        self.ui.load_pages.func_3_frame_1_layout = QHBoxLayout(self.ui.load_pages.func_3_frame_1)
        self.ui.load_pages.func_3_frame_1_layout.addWidget(self.func_btn_31, alignment=Qt.AlignCenter)

        self.func_btn_32 = PyPushButton(
            text = u"智能筛重",
            radius = 8,
            color = self.themes["app_color"]["white"],
            bg_color = self.themes["app_color"]["dark_one"],
            bg_color_hover = self.themes["app_color"]["orange"],
            bg_color_pressed = self.themes["app_color"]["orange"]
        )
        self.func_btn_32.setMaximumWidth(200)
        self.func_btn_32.setMinimumWidth(200)
        self.func_btn_32.setMinimumHeight(40)
        self.func_btn_32.clicked.connect(lambda: self.backend("image_similarity"))
        self.ui.load_pages.func_3_frame_2_layout = QHBoxLayout(self.ui.load_pages.func_3_frame_2)
        self.ui.load_pages.func_3_frame_2_layout.addWidget(self.func_btn_32, alignment=Qt.AlignCenter)

        self.func_btn_33 = PyPushButton(
            text = u"智能影集",
            radius = 8,
            color = self.themes["app_color"]["white"],
            bg_color = self.themes["app_color"]["dark_one"],
            bg_color_hover = self.themes["app_color"]["orange"],
            bg_color_pressed = self.themes["app_color"]["orange"]
        )
        self.func_btn_33.setMaximumWidth(200)
        self.func_btn_33.setMinimumWidth(200)
        self.func_btn_33.setMinimumHeight(40)
        self.func_btn_33.clicked.connect(lambda: self.backend("image_similarity"))
        self.ui.load_pages.func_3_frame_3_layout = QHBoxLayout(self.ui.load_pages.func_3_frame_3)
        self.ui.load_pages.func_3_frame_3_layout.addWidget(self.func_btn_33, alignment=Qt.AlignCenter)

        # SET SCROLLBAR STYLE
        # ///////////////////////////////////////////////////////////////
        custom_scrollbar_style = style_scrollbar.format(
            _radius = 8,
            _bg_color = self.themes["app_color"]["bg_two"],
            _bg_color_hover = self.themes['app_color']['dark_one'],
            _bg_color_pressed = self.themes["app_color"]["orange"]
        )
        self.ui.load_pages.scrollArea_1.verticalScrollBar().setStyleSheet(custom_scrollbar_style)
        self.ui.load_pages.scrollArea_2.verticalScrollBar().setStyleSheet(custom_scrollbar_style)
        self.ui.load_pages.scrollArea_3.verticalScrollBar().setStyleSheet(custom_scrollbar_style)

        # ADD CONNECT TO CUSTOM WIDGET CREDITS
        self.ui.credits.person_name.returnPressed.connect(
            lambda: MainFunctions.update_image_object_label(self, self.ui.credits.person_name))

        # ADD Widgets
        # ///////////////////////////////////////////////////////////////

        # SET GRID LAYOUT FOR PAGE3 ("人物列表")
        # ///////////////////////////////////////////////////////////////
        self.ui.load_pages.gridLayout_2 = QGridLayout(self.ui.load_pages.scrollAreaWidgetContents)
        self.ui.load_pages.gridLayout_2.setSpacing(0)
        self.ui.load_pages.gridLayout_2.setObjectName(u"gridLayout_2")
        self.ui.load_pages.gridLayout_2.setContentsMargins(0, 0, 0, 0)

        # SET VERTICAL LAYOUT FOR PAGE5 ("智能搜图")
        # ///////////////////////////////////////////////////////////////
        self.ui.load_pages.scrollArea_2_layout = QVBoxLayout(self.ui.load_pages.scrollAreaWidgetContents_2)
        self.ui.load_pages.scrollArea_2_layout.setSpacing(0)
        self.ui.load_pages.scrollArea_2_layout.setObjectName(u"scrollArea_2_layout")
        self.ui.load_pages.scrollArea_2_layout.setContentsMargins(0, 0, 0, 0)

        # SET VERTICAL LAYOUT FOR PAGE5 ("智能筛重")
        # ///////////////////////////////////////////////////////////////
        self.ui.load_pages.scrollArea_3_layout = QVBoxLayout(self.ui.load_pages.scrollAreaWidgetContents_3)
        self.ui.load_pages.scrollArea_3_layout.setSpacing(0)
        self.ui.load_pages.scrollArea_3_layout.setObjectName(u"scrollArea_3_layout")
        self.ui.load_pages.scrollArea_3_layout.setContentsMargins(0, 0, 0, 0)
        self.ui.load_pages.scrollArea_3_layout.setSpacing(20)

        # ADD CONFIRM BUTTON FOR PAGE5
        self.commit_delete_button = PyPushButton(
            text = u'确定',
            radius = 8,
            color = self.themes['app_color']['white'],
            bg_color = self.themes['app_color']['dark_one'],
            bg_color_hover = self.themes['app_color']['orange'],
            bg_color_pressed = self.themes['app_color']['orange']
        )
        self.commit_delete_button.setMinimumHeight(40)
        self.ui.load_pages.page_5_layout.addWidget(self.commit_delete_button)
        self.commit_delete_button.hide()
        self.commit_delete_button.clicked.connect(lambda: MainFunctions.update_page5_with_similar_images(self))

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

style_scrollbar = '''
QScrollBar {{
	border: solid;
	border-radius: {_radius};	
	background: {_bg_color};
}}
QScrollBar:handle {{
    border-radius: {_radius};
	background: {_bg_color_hover};
}}
QScrollBar:handle:pressed {{
	background: {_bg_color_pressed};
}}
QScrollBar:add-page,
QScrollBar:sub-page{{
    background: transparent;
}}
QScrollBar:add-line,
QScrollBar:sub-line{{
    background: transparent;
}}
'''