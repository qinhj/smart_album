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
import os
import json
from backend.display_by_person import *

# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from gui.core.qt_core import *

# LOAD UI MAIN
# ///////////////////////////////////////////////////////////////
from . ui_main import *

# FUNCTIONS
class MainFunctions():
    def __init__(self):
        super().__init__()
        # SETUP MAIN WINDOW
        # Load widgets from "gui\uis\main_window\ui_main.py"
        # ///////////////////////////////////////////////////////////////
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)

    # SET MAIN WINDOW PAGES
    # ///////////////////////////////////////////////////////////////
    def set_page(self, page):
        self.ui.load_pages.pages.setCurrentWidget(page)

    # SET LEFT COLUMN PAGES
    # ///////////////////////////////////////////////////////////////
    def set_left_column_menu(
        self,
        menu,
        title,
        icon_path
    ):
        self.ui.left_column.menus.menus.setCurrentWidget(menu)
        self.ui.left_column.title_label.setText(title)
        self.ui.left_column.title_label.setAlignment(Qt.AlignCenter)
        self.ui.left_column.icon.set_icon(icon_path)

    # RETURN IF LEFT COLUMN IS VISIBLE
    # ///////////////////////////////////////////////////////////////
    def left_column_is_visible(self):
        width = self.ui.left_column_frame.width()
        if width == 0:
            return False
        else:
            return True

    # RETURN IF RIGHT COLUMN IS VISIBLE
    # ///////////////////////////////////////////////////////////////
    def right_column_is_visible(self):
        width = self.ui.right_column_frame.width()
        if width == 0:
            return False
        else:
            return True

    # SET RIGHT COLUMN PAGES
    # ///////////////////////////////////////////////////////////////
    def set_right_column_menu(self, menu):
        self.ui.right_column.menus.setCurrentWidget(menu)

    # GET TITLE BUTTON BY OBJECT NAME
    # ///////////////////////////////////////////////////////////////
    def get_title_bar_btn(self, object_name):
        return self.ui.title_bar_frame.findChild(QPushButton, object_name)

    # GET TITLE BUTTON BY OBJECT NAME
    # ///////////////////////////////////////////////////////////////
    def get_left_menu_btn(self, object_name):
        return self.ui.left_menu.findChild(QPushButton, object_name)
    
    # LEDT AND RIGHT COLUMNS / SHOW / HIDE
    # ///////////////////////////////////////////////////////////////
    def toggle_left_column(self):
        # GET ACTUAL CLUMNS SIZE
        width = self.ui.left_column_frame.width()
        right_column_width = self.ui.right_column_frame.width()

        MainFunctions.start_box_animation(self, width, right_column_width, "left")

    def toggle_right_column(self):
        # GET ACTUAL CLUMNS SIZE
        left_column_width = self.ui.left_column_frame.width()
        width = self.ui.right_column_frame.width()

        MainFunctions.start_box_animation(self, left_column_width, width, "right")

    def start_box_animation(self, left_box_width, right_box_width, direction):
        right_width = 0
        left_width = 0
        time_animation = self.ui.settings["time_animation"]
        minimum_left = self.ui.settings["left_column_size"]["minimum"]
        maximum_left = self.ui.settings["left_column_size"]["maximum"]
        minimum_right = self.ui.settings["right_column_size"]["minimum"]
        maximum_right = self.ui.settings["right_column_size"]["maximum"]

        # Check Left Values        
        if left_box_width == minimum_left and direction == "left":
            left_width = maximum_left
        else:
            left_width = minimum_left

        # Check Right values        
        if right_box_width == minimum_right and direction == "right":
            right_width = maximum_right
        else:
            right_width = minimum_right       

        # ANIMATION LEFT BOX        
        self.left_box = QPropertyAnimation(self.ui.left_column_frame, b"minimumWidth")
        self.left_box.setDuration(time_animation)
        self.left_box.setStartValue(left_box_width)
        self.left_box.setEndValue(left_width)
        self.left_box.setEasingCurve(QEasingCurve.InOutQuart)

        # ANIMATION RIGHT BOX        
        self.right_box = QPropertyAnimation(self.ui.right_column_frame, b"minimumWidth")
        self.right_box.setDuration(time_animation)
        self.right_box.setStartValue(right_box_width)
        self.right_box.setEndValue(right_width)
        self.right_box.setEasingCurve(QEasingCurve.InOutQuart)

        # GROUP ANIMATION
        self.group = QParallelAnimationGroup()
        self.group.stop()
        self.group.addAnimation(self.left_box)
        self.group.addAnimation(self.right_box)
        self.group.start()

    # CUSTOM FUNCTIONS
    # ///////////////////////////////////////////////////////////////
    def update_left_column_menu1(self):
        """ Reload person/face cluster info. """
        self.person_dict = load_person_dict('output.json')

        # Move label "unknown" to the bottom of the item keys.
        if u'未命名' in self.person_dict:
            unnamed = self.person_dict.pop(u'未命名')
            self.person_dict['未命名'] = unnamed
        
        # Create a new widget to hold all buttons for quick replace/refresh
        # with latest person image cluster result.
        self.person_list_widget = QWidget()
        self.person_list_layout = QVBoxLayout(self.person_list_widget)
        # Create a new ButtonGroup to get selected button via checkedButton.
        self.person_list_btn_group = QButtonGroup()
        # Create PushButton for each person image cluster.
        for name, _ in self.person_dict.items():
            btn = PyPushButton(
                text = name,
                radius = 5,
                color = self.themes["app_color"]["white"],
                bg_color = self.themes["app_color"]["dark_one"],
                bg_color_hover = self.themes['app_color']['orange'],
                bg_color_pressed = self.themes['app_color']['orange']
            )
            btn.setMinimumHeight(25)
            btn.setMaximumHeight(25)
            btn.setObjectName("Person")
            btn.setCheckable(True)
            btn.setAutoExclusive(True)
            btn.clicked.connect(lambda: MainFunctions.load_images_of_checked_button(
                self, self.person_dict, self.person_list_btn_group))
            btn.DoubleClickSig.connect(lambda: MainFunctions.update_image_group_name(
                self, self.person_dict, self.person_list_btn_group))
            self.person_list_layout.addWidget(btn)
            self.person_list_btn_group.addButton(btn)
        self.person_list_layout.addStretch()
        self.person_list_layout.setSpacing(10)
        try:
            # Clear previous person image list widget.
            _prev_widget = self.ui.left_column.menus.menu_1_layout.itemAt(0).widget()
            _prev_widget.setParent(None)
            self.ui.left_column.menus.menu_1_layout.removeWidget(_prev_widget)
            self.ui.left_column.menus.menu_1_layout.update()
        except AttributeError:
            pass

        self.ui.left_column.menus.menu_1_layout.addWidget(self.person_list_widget)
        assert(self.ui.left_column.menus.menu_1_layout.count() == 1)

    def load_images_of_checked_button(self, person_dict, btn_group):
        self.ui.credits.copyright_label.setText("正在加载图片，请稍后")
        self.ui.credits.person.setText("")
        self.ui.credits.person_name.setText("")
        self.ui.credits.person_name.setFocusPolicy(Qt.WheelFocus)
        self.ui.credits.person_name.setReadOnly(False)
        self.ui.credits.image.setText("")
        self.ui.credits.image_title.setText("")
        self.ui.credits.update()
        QApplication.processEvents()
        _btn = btn_group.checkedButton()
        if _btn is None or _btn.text() not in person_dict.keys():
            # Maybe trigged by Double Click Event
            return
        MainFunctions.update_page3_with_person_images(self, person_dict, _btn.text())
        self.ui.credits.person_name.setText(_btn.text())
        QApplication.processEvents()

    def update_page3_with_person_images(self, person_dict, name):
        images = person_dict[name]
        try:
            _prev_widget = self.ui.load_pages.gridLayout_2.itemAt(0).widget()
            _prev_widget.setParent(None)
            self.ui.load_pages.gridLayout_2.removeWidget(_prev_widget)
        except AttributeError:
            pass
        # Create new image page if not exist
        _image_page = self.image_page_dict_person.setdefault(name, PyImagePage())
        # Check image count
        _image_count = _image_page.flow_layout.count()
        assert(_image_count == 0 or _image_count == len(images)), "{}: {} vs {}".format(name, _image_count, len(images))
        if _image_count == 0:
            for image in images:
                image_box = PyImage(image)
                image_box.checkbox.stateChanged.connect(lambda: MainFunctions.get_checked_button(self, _image_page))
                _image_page.flow_layout.addWidget(image_box)
                _image_page.btn_group.addButton(image_box.checkbox)
                _image_page.flow_layout.update()
                self.ui.load_pages.gridLayout_2.update()
                QApplication.processEvents()
        # Note: Add widget at the end of this function, otherwise the window will refresh `_image_count` times.
        self.ui.load_pages.gridLayout_2.addWidget(_image_page)
        # update checked btn state
        for btn in self.person_list_btn_group.buttons():
            if btn.text() == name:
                btn.setChecked(True)
        # update path for checked image
        _btn = _image_page.btn_group.checkedButton()
        MainFunctions.update_ui_credit_bar(
            self, u"人物名：", name, u"图片名：", _btn.objectName() if _btn else "", u"总数量：{}".format(len(images)))

    def update_ui_credit_bar(
            self, line_text = "", line_edit = "",
            image_label = "", image_title = "",
            copyright = "", # self.settings["copyright"]
        ):
        self.ui.credits.person.setText(line_text)
        self.ui.credits.person_name.setText(line_edit)
        self.ui.credits.person_name.setFocusPolicy(Qt.NoFocus)
        self.ui.credits.person_name.setReadOnly(True)
        self.ui.credits.image.setText(image_label)
        self.ui.credits.image_title.setText(image_title)
        self.ui.credits.copyright_label.setText(copyright)
        self.ui.credits.update()

    def get_checked_button(self, image_page, read_only = False):
        btn = image_page.btn_group.checkedButton()
        print("{} Checked".format(btn.objectName())) 
        self.ui.credits.image_title.setText(btn.objectName())
        self.ui.credits.person_name.setFocusPolicy(Qt.NoFocus if read_only else Qt.WheelFocus)
        self.ui.credits.person_name.setReadOnly(read_only)

    def get_flow_layout(self):
        return self.flow_layout

    def select_single_image(self):
        """ 以图搜图: 选择图片 """
        m = QFileDialog.getOpenFileName(None, "选择图片", ".", "图片 (*.png *.jpg *.JPG *.jpeg *.JPEG *.tiff *.bmp);;")
        self.selected_image = m[0]
        self.ui.credits.copyright_label.setText("选择图片：{}".format(self.selected_image))
        return m[0]

    def select_image_directory(self):
        """ 选择文件夹 """
        directory = QFileDialog.getExistingDirectory(None)
        with open('resources/settings.json', 'r+', encoding='utf-8') as f:
            if directory == '':
                print("No folder selected")
                return None
            self.settings = json.load(f)
            self.settings['image_path'] = directory
            f.seek(0)
            f.truncate()
            f.write(json.dumps(self.settings, indent=4, ensure_ascii=False))
        self.ui.credits.copyright_label.setText("选择文件夹：{}".format(directory))
        return directory
    
    def load_image_search_result(self):
        if not self.image_search_done:
            MainFunctions.update_ui_credit_bar(self, copyright=u"还未选择图片")
            self.ui.load_pages.scrollAreaWidgetContents_2.hide()
            return None
        
        if len(self.image_search_result) == 0:
            MainFunctions.update_ui_credit_bar(self, copyright=u"未能找到相关图片")
            self.ui.load_pages.scrollAreaWidgetContents_2.hide()
            return None
        #print(self.image_search_result)

        self.ui.load_pages.scrollAreaWidgetContents_2.show()

        name, paths = tuple(self.image_search_result.items())[0]
        MainFunctions.update_ui_credit_bar(
            self, u"输入：", name, "", "", u"总数量：{}".format(len(paths)))
        
        if not self.image_search_changed:
            return None

        self.image_search_changed = False
        if os.path.exists(self.selected_image):
            self.ui.load_pages.search_target_lable.setText(u"所选照片")
            self.ui.load_pages.input_image.show()
            self.ui.load_pages.search_target_text.hide()
            # update widget for input image
            if self.ui.load_pages.input_image_layout.count():
                assert(self.ui.load_pages.input_image_layout.count() == 1)
                _prev_widget = self.ui.load_pages.input_image_layout.itemAt(0).widget()
                _prev_widget.setParent(None)
                self.ui.load_pages.input_image_layout.removeWidget(_prev_widget)
            _image_widget = PyImage(self.selected_image)
            _image_widget.checkbox.setCheckable(False)
            self.ui.load_pages.input_image_layout.addWidget(_image_widget)
            self.ui.load_pages.input_image_layout.update()
        else:
            self.ui.load_pages.search_target_lable.setText(u"输入文本")
            self.ui.load_pages.input_image.hide()
            self.ui.load_pages.search_target_text.show()
            self.ui.load_pages.search_target_text.setText(self.selected_image)
        self.ui.load_pages.scrollArea_2_layout.update()

        MainFunctions.update_ui_credit_bar(self, copyright=u"正在加载图片")
        QApplication.processEvents()

        # update widget for output images
        if self.image_search_pages:
            self.image_search_pages.setParent(None)
            self.ui.load_pages.scrollArea_2_layout.removeWidget(self.image_search_pages)

        self.image_search_pages = PyImagePage()
        for path in paths:
            image_box = PyImage(path)
            image_box.checkbox.stateChanged.connect(
                lambda: MainFunctions.get_checked_button(self, self.image_search_pages, True))
            self.image_search_pages.flow_layout.addWidget(image_box)
            self.image_search_pages.flow_layout.update()
            self.image_search_pages.btn_group.addButton(image_box.checkbox)
            QApplication.processEvents()
        MainFunctions.update_ui_credit_bar(
            self, u"输入：", name, "", "", u"总数量：{}".format(len(paths)))
        self.ui.load_pages.scrollArea_2_layout.addWidget(self.image_search_pages)
        self.ui.load_pages.scrollArea_2_layout.addStretch()
        self.ui.load_pages.scrollArea_2_layout.setSpacing(20)
        self.ui.load_pages.scrollArea_2_layout.update()

    def load_image_similarity_result(self):
        if not self.image_similarity_done:
            MainFunctions.update_ui_credit_bar(self, copyright=u"还未进行智能筛重")
            return None
        else:            
            MainFunctions.update_ui_credit_bar(self, copyright=u"正在加载图片")
            QApplication.processEvents()

        if len(self.image_similarity_pages) != 0:
            self.commit_delete_button.show()
            self.ui.credits.copyright_label.setText(u"选择要删除的图片并点击确定")
            return None

        if len(self.image_similarity_result) == 0:
            self.commit_delete_button.hide()
            self.ui.credits.copyright_label.setText(u"未发现相似图片")
            return None

        # ADD IMAGES
        for paths in self.image_similarity_result:
            image_page = PyImagePage()
            image_page.btn_group.setExclusive(False)
            self.ui.load_pages.scrollArea_3_layout.addWidget(image_page)
            for path in paths:
                image_box = PyImage(path)
                image_page.flow_layout.addWidget(image_box)
                image_page.flow_layout.update()
                image_page.btn_group.addButton(image_box.checkbox)
                self.ui.load_pages.scrollArea_3_layout.update()
            self.image_similarity_pages.append(image_page)
        QApplication.processEvents()
        self.commit_delete_button.show()
        self.ui.credits.copyright_label.setText(u"选择要删除的图片并点击确定")

    def update_page5_with_similar_images(self):
        image_path_to_delete = []
        image_page_to_delete = []
        for image_page in self.image_similarity_pages:
            checked_buttons, checked_widgets = [], []
            for index, button in enumerate(image_page.btn_group.buttons()):
                if button.isChecked():
                    #print(index)
                    image_path_to_delete.append(button.objectName())
                    checked_buttons.append(button)
                    checked_widgets.append(image_page.flow_layout.itemAt(index).widget())
            # remove checked widgets from image page
            for checked_widget in checked_widgets:
                checked_widget.setParent(None)
                image_page.flow_layout.removeWidget(checked_widget)
                image_page.flow_layout.update()
                QApplication.processEvents()
            # remove checked buttons from button group
            for checked_button in checked_buttons:
                image_page.btn_group.removeButton(checked_button)
            # add empty or single image page to delete list
            if image_page.flow_layout.count() < 2:
                image_page.setParent(None)
                self.ui.load_pages.scrollArea_3_layout.removeWidget(image_page)
                image_page_to_delete.append(image_page)
                QApplication.processEvents()
        # remove empty image page from page5
        for image_page in image_page_to_delete:
            self.image_similarity_pages.remove(image_page)
        print(image_path_to_delete)
        _ = delete_images(image_path_to_delete, "output.json")
        MainFunctions.update_left_column_menu1(self)
        self.image_page_dict_person = {}

    def update_image_object_label(self, person_name_editer: PyLineEdit):
        assert(self.person_list_btn_group is not None)

        new_name = person_name_editer.text()
        # get old name
        old_name = self.person_list_btn_group.checkedButton().text()
        if new_name == old_name:
            print("[INFO] Ignore image label change since they're same!")
            return

        assert(old_name in self.image_page_dict_person.keys())
        _image_page = self.image_page_dict_person.pop(old_name)

        # get image path
        checked_image = _image_page.btn_group.checkedButton()
        image_path = checked_image.objectName()

        # remove previous widget
        index = _image_page.btn_group.buttons().index(checked_image)
        _prev_widget = _image_page.flow_layout.itemAt(index).widget()
        _prev_widget.setParent(None)
        _image_page.flow_layout.removeWidget(_prev_widget)
        _image_page.flow_layout.update()
        checked_image.setParent(None)
        _image_page.btn_group.removeButton(checked_image)

        # update person image page dict
        if new_name in self.image_page_dict_person.keys():
            _ = self.image_page_dict_person.pop(new_name)

        _ = edit_single_image_label(new_name, image_path, self.person_dict)

        # update person image menu(list button)
        MainFunctions.update_left_column_menu1(self)
        # reload person image page of new name
        MainFunctions.update_page3_with_person_images(self, self.person_dict, new_name)
        QApplication.processEvents()

    def update_image_group_name(self, person_dict, btn_group):
        _btn = btn_group.checkedButton()
        name_old = _btn.text()
        input_dialog = QInputDialog(self)
        name_new, ok = input_dialog.getText(self, u"更改名称", "New Name: ")
        if ok:
            if name_new == name_old:
                print("[INFO] Ignore rename since they're same!")
                return
            if name_new not in person_dict.keys():
                person_dict[name_new] = person_dict.pop(name_old)
                if name_old in self.image_page_dict_person.keys():
                    self.image_page_dict_person[name_new] = self.image_page_dict_person.pop(name_old)
            else:
                person_dict[name_new].extend(person_dict.pop(name_old))
                # pop image pages which need reload
                if name_old in self.image_page_dict_person.keys():
                    _ = self.image_page_dict_person.pop(name_old)
                if name_new in self.image_page_dict_person.keys():
                    _ = self.image_page_dict_person.pop(name_new)
            write_json(person_dict)
            # reload person since person groups have changed
            MainFunctions.update_left_column_menu1(self)
            # reload person image page of new name
            MainFunctions.update_page3_with_person_images(self, person_dict, name_new)
            QApplication.processEvents()
