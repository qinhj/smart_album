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
import json
import os, sys

# IMPORT SETTINGS
# ///////////////////////////////////////////////////////////////
from gui.core.json_settings import Settings

# APP THEMES
# ///////////////////////////////////////////////////////////////
class Themes(object):

    # INIT SETTINGS
    # ///////////////////////////////////////////////////////////////
    def __init__(self, settings_path: str = None):
        super(Themes, self).__init__()

        # LOAD SETTINGS
        # ///////////////////////////////////////////////////////////////
        setup_settings = Settings(settings_path)
        self._settings = setup_settings.items

        # APP PATH
        # ///////////////////////////////////////////////////////////////
        json_file = f"gui/themes/{self._settings['theme_name']}.json"
        app_path = os.path.dirname(os.path.realpath(sys.argv[0]))
        self.settings_path = os.path.normpath(os.path.join(app_path, json_file))
        if not os.path.isfile(self.settings_path):
            print("WARNING: \"gui/themes/{}.json\" not found! check in the folder {}".format(
                self._settings['theme_name'], self.settings_path
            ))

        # DICTIONARY WITH SETTINGS
        self.items = {}

        # DESERIALIZE
        self.deserialize()

    # SERIALIZE JSON
    # ///////////////////////////////////////////////////////////////
    def serialize(self):
        # WRITE JSON FILE
        with open(self.settings_path, "w", encoding='utf-8') as write:
            json.dump(self.items, write, indent=4)

    # DESERIALIZE JSON
    # ///////////////////////////////////////////////////////////////
    def deserialize(self):
        # READ JSON FILE
        with open(self.settings_path, "r", encoding='utf-8') as reader:
            settings = json.loads(reader.read())
            self.items = settings