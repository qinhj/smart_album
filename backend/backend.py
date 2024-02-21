# ///////////////////////////////////////////////////////////////
#
# BY: qinhj@lsec.cc.ac.cn
#
# ///////////////////////////////////////////////////////////////

# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
import os, sys
from abc import ABC, abstractmethod
from backend.worker import create_detect_worker, create_search_worker, create_duplicate_worker

# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from gui.core.qt_core import *

# pylint: disable=unused-argument

def _not_implemented(*args):
    raise NotImplementedError("Sorry, not implement yet.")


class IBackend(ABC):

    def __init__(self, main_window: QMainWindow):
        self._main_window = main_window

    def __call__(self, cmd: str, *args):
        return _not_implemented(*args)


class FakeBackend(IBackend):

    def __init__(self, main_window: QMainWindow):
        super().__init__(main_window)
        self._image_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "assets", "obama")

        def fake_detect(image_paths):
            from backend.display_by_person import load_json, write_json
            results = load_json(main_window.settings["output_path"])
            persons = {}
            for item in results:
                k, v = item["person"], item["pic_name"]
                if k in persons.keys():
                    persons[k].append(item["pic_name"])
                else:
                    persons[k] = [item["pic_name"]]
            if u"未命名" not in persons.keys():
                persons[u"未命名"] = image_paths
            else:
                persons[u"未命名"].extend(image_paths)
            write_json(persons)
            return {u"未命名": image_paths} # just do nothing

        def fake_search(image_path):
            print("[WARN] fake search will ignore input images!")
            # always reset settings['image_path'] as test data dir
            main_window.settings['image_path'] = self._image_dir
            from backend.utils import get_image_paths
            return {"obama": get_image_paths(self._image_dir)}

        def fake_duplicate(image_dir):
            print("[WARN] fake duplicate will ignore input image directory!")
            fake_result = [
                os.path.normpath(os.path.join(self._image_dir, "Obama_00.jpg")),
                os.path.normpath(os.path.join(self._image_dir, "Obama_00.copy.jpg"))
            ]
            return [fake_result]

        # create handler for supported task and thread worker
        self._task_handler = {
            "Detect" : [create_detect_worker, fake_detect],
            "Search" : [create_search_worker, fake_search],
            "Duplicate" : [create_duplicate_worker, fake_duplicate],
        }

    def __call__(self, cmd: str, *args):
        if cmd in self._task_handler.keys():
            worker, handler = self._task_handler[cmd]
            worker(self._main_window, handler, *args)
        else:
            raise RuntimeError("Unsupported command {}".format(cmd))


def backend_selector(qw: QWidget, name: str):
    if name.lower() == "fake":
        return FakeBackend(qw)
    raise RuntimeError("Unsupported backend: {}".format(name))