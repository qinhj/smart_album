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
from backend.callback import ICallback, TaskState
from . functions_main_window import MainFunctions, Functions

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
            "btn_text": "人脸聚类",
            "btn_tooltip": "人脸聚类",
            "show_top": True,
            "is_active": False
        },
        {
            "btn_icon": "icon_search.svg",
            "btn_id": "btn_page_image_search",
            "btn_text": "智能搜图",
            "btn_tooltip": "智能搜图",
            "show_top": True,
            "is_active": False
        },
        {
            "btn_icon": "icon_signal.svg",
            "btn_id": "btn_page_image_similarity",
            "btn_text": "智能筛重",
            "btn_tooltip": "智能筛重",
            "show_top": True,
            "is_active": False
        },
        {
            "btn_icon": "icon_heart.svg",
            "btn_id": "btn_page_smart_album",
            "btn_text": "智能影集",
            "btn_tooltip": "智能影集",
            "show_top": True,
            "is_active": False
        },
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
        #self.ui.title_bar.add_menus(SetupMainWindow.add_title_bar_menus)

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
        settings = Settings(self.settings_path)
        self.settings = settings.items

        # LOAD THEME COLOR
        # ///////////////////////////////////////////////////////////////
        themes = Themes(self.settings_path)
        self.themes = themes.items

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
        self.image_search_pages = None
        # Image Similarity
        self.image_similarity_done = False
        self.image_similarity_result = []
        self.image_similarity_pages = []
        # Smart Album
        self.smart_album_result = None # dict: {"name":"", "images":[]}, None for init
        self.smart_album_btn_group = None
        self.smart_album_image_page = {}
        # Task Pending
        self.task_pending = { task : False for task in [
            "smart_album",
            "face_cluster",
            "image_search",
            "image_similarity",
        ]}

        # GET AND INIT AI BACKEND
        # ///////////////////////////////////////////////////////////////
        class BackendCallback(ICallback):
            def __init__(self, main_window: QMainWindow):
                super().__init__()
                self._main_window = main_window

            def __call__(self, cmd: str, state: TaskState, *args, **kwargs):
                print(f"{cmd} {state}")
                if state == TaskState.PREPARE:
                    if cmd in ["smart_album", "face_cluster"]:
                        MainFunctions.update_ui_credit_bar(self._main_window)
                elif state == TaskState.FINISHED:
                    self._main_window.task_pending[cmd] = False
                    if cmd == "smart_album":
                        MainFunctions.update_album_list(self._main_window)
                    elif cmd == "face_cluster":
                        MainFunctions.update_human_list(self._main_window)
                    elif cmd == "image_search":
                        MainFunctions.load_image_search_result(self._main_window)
                    elif cmd == "image_similarity":
                        MainFunctions.load_image_similarity_result(self._main_window)
                    else:
                        print(f"[WARN] unknown cmd: {cmd}")
                elif state == TaskState.RUNNING:
                    self._main_window.task_pending[cmd] = True
                    if cmd == "smart_album":
                        self._main_window.smart_album_result = None
                        self._main_window.smart_album_image_page = {}
                    elif cmd == "face_cluster":
                        pass
                    elif cmd == "image_search":
                        self._main_window.image_search_changed = True
                        self._main_window.image_search_done = True
                    elif cmd == "image_similarity":
                        pass
                    else:
                        print(f"[WARN] unknonw cmd: {cmd}")
                else:
                    pass

        self.callback = BackendCallback(self)
        self.backend = backend_selector(self, self.settings["backend"], self.callback)

        # LEFT COLUMN
        # ///////////////////////////////////////////////////////////////

        # PAGES
        # ///////////////////////////////////////////////////////////////

        def add_label(layout: QBoxLayout, text: str, name: str, parent = None):
            label = QLabel(text, parent=parent)
            label.setObjectName(name)
            layout.addWidget(label, alignment=Qt.AlignCenter)
            return label
        
        def add_btn(layout: QBoxLayout, text: str, slot, parent = None):
            btn = PyPushButton(
                text = text,
                radius = 8,
                color = self.themes["app_color"]["white"],
                bg_color = self.themes["app_color"]["dark_one"],
                bg_color_hover = self.themes["app_color"]["orange"],
                bg_color_pressed = self.themes["app_color"]["orange"],
                parent = parent,
            )
            btn.setMaximumWidth(200)
            btn.setMinimumWidth(200)
            btn.setMinimumHeight(40)
            btn.clicked.connect(slot)
            layout.addWidget(btn, alignment=Qt.AlignCenter)
            return btn

        # ADD CUSTOM LEFT COLUMN WIDGET
        def add_left_column(layout: QBoxLayout, title: str):
            frame = layout.parentWidget()
            left_column = PyLeftColumnInner(
                parent = frame,
                app_parent = self.ui.central_widget,
                text_title = title,
                text_title_size = self.settings["font"]["title_size"],
                text_title_color = self.themes['app_color']['text_foreground'],
                dark_one = self.themes['app_color']['dark_one'],
                bg_color = self.themes['app_color']['bg_three'],
                context_color = self.themes['app_color']['context_color'],
            )
            layout.addWidget(left_column)
            return left_column

        def run_backend(task: str, list_layout: QBoxLayout = None, image_layout: QBoxLayout = None, index = 0, count = 1):
            if self.task_pending[task]:
                print("[INFO] Ignore run {} since update is pending ...".format(task))
                return
            # Clear previous list widget and image widgets.
            if list_layout and list_layout.count():
                MainFunctions.delete_widget(self, list_layout, index, count)
            if image_layout and image_layout.count():
                if count != -1:
                    MainFunctions.delete_widget(self, image_layout, index, count)
                else:
                    for index in range(image_layout.count()-1, -1, -1):
                        MainFunctions.delete_widget(
                            self, image_layout, index, index+1)
            self.backend(task)

        # ///////////////////////////////////////////////////////////////
        # PAGE 1 - ADD LOGO TO MAIN PAGE
        # ///////////////////////////////////////////////////////////////
        self.logo_svg = QSvgWidget(Functions.set_svg_image("bianbu-logo-dark.svg"))
        self.ui.load_pages.logo_layout.addWidget(self.logo_svg, Qt.AlignCenter, Qt.AlignCenter)

        # ///////////////////////////////////////////////////////////////
        # PAGE 2 - SET LAYOUT FOR PAGE2 ("智能影集")
        # ///////////////////////////////////////////////////////////////
        self.ui.load_pages.scrollArea_layout_album = QGridLayout(self.ui.load_pages.page_2_right_scrollAreaWidgetContents)
        self.ui.load_pages.scrollArea_layout_album.setSpacing(0)
        self.ui.load_pages.scrollArea_layout_album.setObjectName(u"scrollArea_layout_album")
        self.ui.load_pages.scrollArea_layout_album.setContentsMargins(0, 0, 0, 0)

        # PAGE 2 - ADD LEFT COLUMN
        self.ui.load_pages.page_2_left_column_frame.setMaximumWidth(self.settings["left_column_size"]["maximum"])
        self.ui.load_pages.page_2_left_column_frame.setMinimumWidth(self.settings["left_column_size"]["minimum"])
        self.ui.load_pages.page_2_left_column_frame.setStyleSheet(f"background: {self.themes['app_color']['bg_two']}")
        self.ui.load_pages.album_list_layout = QVBoxLayout(self.ui.load_pages.page_2_left_column_frame)
        self.ui.load_pages.album_list_layout.setContentsMargins(0,0,0,0)
        self.ui.load_pages.page_2_left_column = add_left_column(self.ui.load_pages.album_list_layout, u"影集列表")

        # PAGE 2 - ADD COMMAND BUTTON
        self.ui.load_pages.page_2_top_widget_layout = QHBoxLayout(self.ui.load_pages.page_2_top_widget)
        _ = add_label(self.ui.load_pages.page_2_top_widget_layout, u"智能影集",
                      "page_2_func_label", self.ui.load_pages.page_2)
        _ = add_btn(self.ui.load_pages.page_2_top_widget_layout, u"选择文件夹",
                    lambda: MainFunctions.select_image_directory(self), self.ui.load_pages.page_2)
        _ = add_btn(self.ui.load_pages.page_2_top_widget_layout, u"开始分析",
                    lambda: run_backend(
                        "smart_album",
                        self.ui.load_pages.page_2_left_column.scrollAreaLayout,
                        self.ui.load_pages.scrollArea_layout_album,
                    ), self.ui.load_pages.page_2)

        # ///////////////////////////////////////////////////////////////
        # PAGE 3 - SET LAYOUT FOR PAGE3 ("人脸聚类")
        # ///////////////////////////////////////////////////////////////
        self.ui.load_pages.scrollArea_layout_human = QGridLayout(self.ui.load_pages.page_3_right_scrollAreaWidgetContents)
        self.ui.load_pages.scrollArea_layout_human.setSpacing(0)
        self.ui.load_pages.scrollArea_layout_human.setObjectName(u"scrollArea_layout_human")
        self.ui.load_pages.scrollArea_layout_human.setContentsMargins(0, 0, 0, 0)

        # PAGE 3 - ADD LEFT COLUMN
        self.ui.load_pages.page_3_left_column_frame.setMaximumWidth(self.settings["left_column_size"]["maximum"])
        self.ui.load_pages.page_3_left_column_frame.setMinimumWidth(self.settings["left_column_size"]["minimum"])
        self.ui.load_pages.page_3_left_column_frame.setStyleSheet(f"background: {self.themes['app_color']['bg_two']}")
        self.ui.load_pages.human_list_layout = QVBoxLayout(self.ui.load_pages.page_3_left_column_frame)
        self.ui.load_pages.human_list_layout.setContentsMargins(0,0,0,0)
        self.ui.load_pages.page_3_left_column = add_left_column(self.ui.load_pages.human_list_layout, u"人物列表")

        # PAGE 3 - ADD COMMAND BUTTON
        self.ui.load_pages.page_3_top_widget_layout = QHBoxLayout(self.ui.load_pages.page_3_top_widget)
        _ = add_label(self.ui.load_pages.page_3_top_widget_layout, u"人脸聚类",
                      "page_3_func_label", self.ui.load_pages.page_3)
        _ = add_btn(self.ui.load_pages.page_3_top_widget_layout, u"选择文件夹",
                    lambda: MainFunctions.select_image_directory(self), self.ui.load_pages.page_3)
        _ = add_btn(self.ui.load_pages.page_3_top_widget_layout, u"开始聚类",
                    lambda: run_backend(
                        "face_cluster",
                        self.ui.load_pages.scrollArea_layout_human,
                        self.ui.load_pages.page_3_left_column.scrollAreaLayout
                    ), self.ui.load_pages.page_3)

        # ///////////////////////////////////////////////////////////////
        # PAGE 4 - SET LAYOUT FOR PAGE4 ("智能搜图")
        # ///////////////////////////////////////////////////////////////
        self.ui.load_pages.search_info_layout = QHBoxLayout(self.ui.load_pages.page_4_search_info)
        self.ui.load_pages.search_info_layout.setSpacing(0)
        self.ui.load_pages.search_info_layout.setObjectName(u"search_info_layout")
        self.ui.load_pages.search_info_layout.setContentsMargins(0, 0, 0, 0)
        self.ui.load_pages.search_info_layout.setAlignment(Qt.AlignCenter)
        self.ui.load_pages.scrollArea_layout_search = QGridLayout(self.ui.load_pages.page_4_scrollAreaWidgetContents)
        self.ui.load_pages.scrollArea_layout_search.setSpacing(0)
        self.ui.load_pages.scrollArea_layout_search.setObjectName(u"scrollArea_layout_search")
        self.ui.load_pages.scrollArea_layout_search.setContentsMargins(0, 0, 0, 0)

        # PAGE 4 - ADD COMMAND BUTTON
        self.ui.load_pages.page_4_top_widget_layout = QHBoxLayout(self.ui.load_pages.page_4_top_widget)
        _ = add_label(self.ui.load_pages.page_4_top_widget_layout, u"智能搜图",
                      "page_4_func_label", self.ui.load_pages.page_4)
        _ = add_btn(self.ui.load_pages.page_4_top_widget_layout, u"选择文件夹",
                    lambda: MainFunctions.select_image_directory(self), self.ui.load_pages.page_4)
        _ = add_btn(self.ui.load_pages.page_4_top_widget_layout, u"选择图片",
                    lambda: MainFunctions.select_single_image(self), self.ui.load_pages.page_4)
        _ = add_btn(self.ui.load_pages.page_4_top_widget_layout, u"开始查找",
                    lambda: run_backend(
                        "image_search",
                        self.ui.load_pages.search_info_layout,
                        self.ui.load_pages.scrollArea_layout_search
                    ), self.ui.load_pages.page_4)

        # ADD LINE EDIT TO TITLE BAR FOR CUSTOM SEARCH WITH TEXT
        self.search_text = PyLineEdit(place_holder_text = u"文搜图")
        self.search_text.setAlignment(Qt.AlignLeft)
        self.search_text.setReadOnly(False)
        self.ui.title_bar.custom_buttons_layout.addWidget(self.search_text)
        self.search_text_div_3 = py_title_bar.py_div.PyDiv(self.themes["app_color"]["bg_three"])
        self.ui.title_bar.custom_buttons_layout.addWidget(self.search_text_div_3)
        def search_text_slot(text):
            print("[INFO] Input text: {}".format(text))
            self.selected_image = text
            MainFunctions.update_ui_credit_bar(self, u"输入：", text)
            run_backend("image_search",
                        self.ui.load_pages.search_info_layout,
                        self.ui.load_pages.scrollArea_layout_search)
            self.search_text.setText(u"")
        self.search_text.returnPressed.connect(lambda: search_text_slot(self.search_text.text()))
        # Hide Custom Title Bar
        self.ui.title_bar.set_custom_title_bar(False)

        # ///////////////////////////////////////////////////////////////
        # PAGE 5 - SET LAYOUT FOR PAGE5 ("智能筛重")
        # ///////////////////////////////////////////////////////////////
        self.ui.load_pages.scrollArea_layout_similarity = QVBoxLayout(self.ui.load_pages.page_5_scrollAreaWidgetContents)
        self.ui.load_pages.scrollArea_layout_similarity.setSpacing(0)
        self.ui.load_pages.scrollArea_layout_similarity.setObjectName(u"scrollArea_layout_similarity")
        self.ui.load_pages.scrollArea_layout_similarity.setContentsMargins(0, 0, 0, 0)
        self.ui.load_pages.scrollArea_layout_similarity.setSpacing(20)

        # PAGE 5 - ADD COMMAND BUTTON
        self.ui.load_pages.page_5_top_widget_layout = QHBoxLayout(self.ui.load_pages.page_5_top_widget)
        _ = add_label(self.ui.load_pages.page_5_top_widget_layout, u"智能筛重",
                      "page_5_func_label", self.ui.load_pages.page_5)
        _ = add_btn(self.ui.load_pages.page_5_top_widget_layout, u"选择文件夹",
                    lambda: MainFunctions.select_image_directory(self), self.ui.load_pages.page_5)
        _ = add_btn(self.ui.load_pages.page_5_top_widget_layout, u"开始分析",
                    lambda: run_backend(
                        "image_similarity", None,
                        self.ui.load_pages.scrollArea_layout_similarity, count = -1 # as all
                    ), self.ui.load_pages.page_5)

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
        self.commit_delete_button.clicked.connect(lambda: MainFunctions.update_similar_images(self))

        # SET SCROLLBAR STYLE
        # ///////////////////////////////////////////////////////////////
        custom_scrollbar_style = style_scrollbar.format(
            _radius = 8,
            _bg_color = self.themes["app_color"]["bg_two"],
            _bg_color_hover = self.themes['app_color']['dark_one'],
            _bg_color_pressed = self.themes["app_color"]["orange"]
        )
        self.ui.load_pages.page_2_right_scrollArea.verticalScrollBar().setStyleSheet(custom_scrollbar_style)
        self.ui.load_pages.page_2_left_column.scrollArea.verticalScrollBar().setStyleSheet(custom_scrollbar_style)
        self.ui.load_pages.page_3_right_scrollArea.verticalScrollBar().setStyleSheet(custom_scrollbar_style)
        self.ui.load_pages.page_3_left_column.scrollArea.verticalScrollBar().setStyleSheet(custom_scrollbar_style)
        self.ui.load_pages.page_4_scrollArea.verticalScrollBar().setStyleSheet(custom_scrollbar_style)
        self.ui.load_pages.page_5_scrollArea.verticalScrollBar().setStyleSheet(custom_scrollbar_style)

        # ADD CONNECT TO CUSTOM WIDGET CREDITS
        self.ui.credits.person_name.returnPressed.connect(
            lambda: MainFunctions.update_image_object_label(self, self.ui.credits.person_name))

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