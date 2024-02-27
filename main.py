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
from gui.uis.windows.main_window.functions_main_window import *
import sys
import os
import time

# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from gui.core.qt_core import *

# IMPORT SETTINGS
# ///////////////////////////////////////////////////////////////
from gui.core.json_settings import Settings

# IMPORT PY ONE DARK WINDOWS
# ///////////////////////////////////////////////////////////////
# MAIN WINDOW
from gui.uis.windows.main_window import *

# IMPORT PY ONE DARK WIDGETS
# ///////////////////////////////////////////////////////////////
from gui.widgets import *

# ADJUST QT FONT DPI FOR HIGHT SCALE AN 4K MONITOR
# ///////////////////////////////////////////////////////////////
os.environ["QT_FONT_DPI"] = "96"
# IF IS 4K MONITOR ENABLE 'os.environ["QT_SCALE_FACTOR"] = "2"'

# MAIN WINDOW
# ///////////////////////////////////////////////////////////////
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # SETUP MAIN WINDOw
        # Load widgets from "gui\uis\main_window\ui_main.py"
        # ///////////////////////////////////////////////////////////////
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)

        # LOAD SETTINGS
        # ///////////////////////////////////////////////////////////////
        settings = Settings()
        self.settings = settings.items

        # SETUP MAIN WINDOW
        # ///////////////////////////////////////////////////////////////
        self.hide_grips = True # Show/Hide resize grips
        SetupMainWindow.setup_gui(self)

        # SHOW MAIN WINDOW
        # ///////////////////////////////////////////////////////////////
        self.show()

    # LEFT MENU BTN IS CLICKED
    # Run function when btn is clicked
    # Check funtion by object name / btn_id
    # ///////////////////////////////////////////////////////////////
    def btn_clicked(self):
        # GET BT CLICKED
        btn = SetupMainWindow.setup_btns(self)

        # LEFT MENU
        # ///////////////////////////////////////////////////////////////
        
        # HOME BTN
        if btn.objectName() == "btn_home":
            # Select Menu
            self.ui.left_menu.select_only_one(btn.objectName())
            # Close Left Column
            if MainFunctions.left_column_is_visible(self):
                MainFunctions.toggle_left_column(self)
            MainFunctions.update_ui_credit_bar(self)
            # Load Page 1
            MainFunctions.set_page(self, self.ui.load_pages.page_1)

        # OPEN PAGE 2(smart album)
        if btn.objectName() == 'btn_page_smart_album':
            # Select Menu
            self.ui.left_menu.select_only_one(btn.objectName())
            # Always Show Left Column
            if not MainFunctions.left_column_is_visible(self):
                MainFunctions.toggle_left_column(self)
            # Load Page 2
            MainFunctions.set_page(self, self.ui.load_pages.page_2)
            if self.ui.load_pages.scrollArea_4_layout.count():
                MainFunctions.delete_widget(self, self.ui.load_pages.scrollArea_4_layout, 0, 1)
            # Load && Update Menu 2
            MainFunctions.update_left_column_menu2(self)
            MainFunctions.set_left_column_menu(
                self,
                menu = self.ui.left_column.menus.menu_2,
                title = btn.text(),
                icon_path = btn._icon_path
            )

        # OPEN PAGE 3(pics)
        if btn.objectName() == 'btn_page_face_cluster':
            # Select Menu
            self.ui.left_menu.select_only_one(btn.objectName())
            # Always Show Left Column
            if not MainFunctions.left_column_is_visible(self):
                MainFunctions.toggle_left_column(self)
            # Load Page 3
            MainFunctions.set_page(self, self.ui.load_pages.page_3)
            if self.ui.load_pages.gridLayout_2.count():
                MainFunctions.delete_widget(self, self.ui.load_pages.gridLayout_2, 0, 1)
            # Load && Update Menu 1
            MainFunctions.update_left_column_menu1(self)
            MainFunctions.set_left_column_menu(
                self,
                menu = self.ui.left_column.menus.menu_1,
                title = btn.text(),
                icon_path = btn._icon_path
            )

        # OPEN PAGE 4
        if btn.objectName() == 'btn_page_image_search':
            # Select Menu
            self.ui.left_menu.select_only_one(btn.objectName())
            # Close Left Column
            if MainFunctions.left_column_is_visible(self):
                MainFunctions.toggle_left_column(self)
            # Load Page 4
            MainFunctions.set_page(self, self.ui.load_pages.page_4)
            MainFunctions.load_image_search_result(self)

        # OPEN PAGE 5
        if btn.objectName() == 'btn_page_image_similarity':
            # Select Menu
            self.ui.left_menu.select_only_one(btn.objectName())
            # Close Left Column
            if MainFunctions.left_column_is_visible(self):
                MainFunctions.toggle_left_column(self)
            # Load Page 5
            MainFunctions.set_page(self, self.ui.load_pages.page_5)
            MainFunctions.load_image_similarity_result(self)

        # SETTINGS LEFT
        if btn.objectName() == "btn_settings" or btn.objectName() == "btn_close_left_column":
            # CHECK IF LEFT COLUMN IS VISIBLE
            if not MainFunctions.left_column_is_visible(self):
                # Show / Hide
                MainFunctions.toggle_left_column(self)
                self.ui.left_menu.select_only_one_tab(btn.objectName())
            else:
                if btn.objectName() == "btn_close_left_column":
                    self.ui.left_menu.deselect_all_tab()
                    # Show / Hide
                    MainFunctions.toggle_left_column(self)
                self.ui.left_menu.select_only_one_tab(btn.objectName())

            # Change Left Column Menu
            if btn.objectName() != "btn_close_left_column":
                MainFunctions.set_left_column_menu(
                    self, 
                    menu = self.ui.left_column.menus.menu_1,
                    title = "Settings Left Column",
                    icon_path = Functions.set_svg_icon("icon_settings.svg")
                )
        
        # TITLE BAR MENU
        # ///////////////////////////////////////////////////////////////
        
        # SETTINGS TITLE BAR
        if btn.objectName() == "btn_top_settings":
            # Toogle Active
            if not MainFunctions.right_column_is_visible(self):
                btn.set_active(True)

                # Show / Hide
                MainFunctions.toggle_right_column(self)
            else:
                btn.set_active(False)

                # Show / Hide
                MainFunctions.toggle_right_column(self)

            # Get Left Menu Btn            
            top_settings = MainFunctions.get_left_menu_btn(self, "btn_settings")
            top_settings.set_active_tab(False)

        # BUTTON SEARCH
        if btn.objectName() == "btn_search":
            self.backend("image_search")

        # DEBUG
        print(f"Button {btn.objectName()}, clicked!")

    # LEFT MENU BTN IS RELEASED
    # Run function when btn is released
    # Check funtion by object name / btn_id
    # ///////////////////////////////////////////////////////////////
    def btn_released(self):
        # GET BT CLICKED
        btn = SetupMainWindow.setup_btns(self)

        # DEBUG
        print(f"Button {btn.objectName()}, released!")

    # RESIZE EVENT
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        SetupMainWindow.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def closeEvent(self, event):
        self.close()
        print("[INFO] Quit {}. See you later.".format(self.settings["app_name"]))


# SETTINGS WHEN TO START
# Set the initial class and also additional parameters of the "QApplication" class
# ///////////////////////////////////////////////////////////////
if __name__ == "__main__":
    # APPLICATION
    # ///////////////////////////////////////////////////////////////
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()

    # EXEC APP
    # ///////////////////////////////////////////////////////////////
    sys.exit(app.exec_())
