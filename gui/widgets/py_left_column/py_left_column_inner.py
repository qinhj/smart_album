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

class PyLeftColumnInner(QWidget):

    def __init__(
        self,
        parent,
        app_parent,
        text_title,
        text_title_size,
        text_title_color,
        dark_one,
        bg_color,
        context_color,
        radius = 8
    ):
        super().__init__()

        # PARAMETERS
        self._parent = parent
        self._app_parent = app_parent
        self._text_title = text_title
        self._text_title_size = text_title_size
        self._text_title_color = text_title_color
        self._dark_one = dark_one
        self._bg_color = bg_color
        self._context_color = context_color
        self._radius = radius

        # SETUP UI
        self.setup_ui()

    # WIDGETS
    # ///////////////////////////////////////////////////////////////
    def setup_ui(self):
        # BASE LAYOUT
        self.base_layout = QVBoxLayout(self)
        self.base_layout.setContentsMargins(0,0,0,0)
        self.base_layout.setSpacing(0)

        # TITLE FRAME
        # ///////////////////////////////////////////////////////////////
        self.title_frame = QFrame()
        self.title_frame.setMaximumHeight(47)
        self.title_frame.setMinimumHeight(47)

        # TITLE BASE LAYOUT 
        self.title_base_layout = QVBoxLayout(self.title_frame)
        self.title_base_layout.setContentsMargins(5,3,5,3)

        # TITLE BG
        self.title_bg_frame = QFrame()
        self.title_bg_frame.setObjectName("title_bg_frame")
        self.title_bg_frame.setStyleSheet(f'''
        #title_bg_frame {{
            background-color: {self._bg_color};
            border-radius: {self._radius}px;
        }}
        ''')

        # LAYOUT TITLE BG
        self.title_bg_layout = QHBoxLayout(self.title_bg_frame)
        self.title_bg_layout.setContentsMargins(5,5,5,5)
        self.title_bg_layout.setSpacing(3)

        # LABEL
        self.title_label = QLabel(self._text_title)
        self.title_label.setObjectName("title_label")
        self.title_label.setStyleSheet(f'''
        #title_label {{
            font-size: {self._text_title_size}pt;
            color: {self._text_title_color};
            padding-bottom: 2px;
            background: none;
        }}
        ''')

        # ADD TO TITLE LAYOUT
        self.title_bg_layout.addWidget(self.title_label)

        # ADD TITLE BG TO LAYOUT
        self.title_base_layout.addWidget(self.title_bg_frame)

        # CONTENT FRAME
        # ///////////////////////////////////////////////////////////////
        self.content_frame = QFrame()
        self.content_frame.setStyleSheet("background: none")
        self.content_frame.resize(240, 600)
        self.content_frame_layout = QVBoxLayout(self.content_frame)
        self.content_frame_layout.setSpacing(0)
        self.content_frame_layout.setObjectName(u"main_pages_layout")
        self.content_frame_layout.setContentsMargins(2, 2, 2, 2)

        # SCROLL AREA
        # ///////////////////////////////////////////////////////////////
        self.scrollArea = QScrollArea(self.content_frame)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"background: transparent;")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 240, 600))
        self.scrollAreaWidgetContents.setStyleSheet(u"background: transparent;")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.scrollAreaLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.scrollAreaLayout.setSpacing(0)
        self.scrollAreaLayout.setObjectName(u"scrollAreaLayout")
        self.scrollAreaLayout.setContentsMargins(0, 0, 0, 0)
        # Add Widget As Placeholder
        self.scrollAreaLayout.addWidget(QWidget())

        # ADD TO CONTENT FRAME LAYOUT
        # ///////////////////////////////////////////////////////////////
        self.content_frame_layout.addWidget(self.scrollArea)

        # ADD TO LAYOUT
        # ///////////////////////////////////////////////////////////////
        self.base_layout.addWidget(self.title_frame)
        self.base_layout.addWidget(self.content_frame)
