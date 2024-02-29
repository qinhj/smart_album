# ///////////////////////////////////////////////////////////////
#
# BY: qinhj@lsec.cc.ac.cn
#
# ///////////////////////////////////////////////////////////////

# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
import os
from abc import ABC, abstractmethod
from backend.worker import create_worker_smart_album
from backend.worker import create_worker_face_cluster
from backend.worker import create_worker_image_search
from backend.worker import create_worker_image_similarity

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
        if main_window.workspace:
            # use customer assets
            self._image_dir = os.path.join(main_window.workspace, "assets", "obama")
        else:
            # use default assets of package
            self._image_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "assets", "obama")
        self._image_dir = os.path.normpath(self._image_dir)

        def fake_smart_album(image_dir):
            print("[WARN] fake smart album will ignore input image directory!")
            fake_result = [
                {
                    "name" : "Obama_00",
                    "images": [
                        os.path.normpath(os.path.join(self._image_dir, "Obama_00.jpg")),
                        os.path.normpath(os.path.join(self._image_dir, "Obama_00.copy.jpg")),
                    ]
                },
                {
                    "name" : "Obama_01",
                    "images": [
                        os.path.normpath(os.path.join(self._image_dir, "Obama_01.jpg")),
                        os.path.normpath(os.path.join(self._image_dir, "copy_01.jpg")),
                        os.path.normpath(os.path.join(self._image_dir, "copy_02.jpg")),
                    ]
                },
            ]
            return fake_result

        def fake_face_cluster(image_dir):
            persons = {}
            copyright_label = self._main_window.ui.credits.copyright_label

            from backend.utils import get_image_paths, differ_paths
            image_paths = get_image_paths(self._main_window.settings["image_path"])
            image_paths = differ_paths(image_paths, self._main_window.settings["output_path"])
            total_image = len(image_paths)
            if total_image == 0:
                copyright_label.setText("共有 0 张新增图片，识别取消")
                return persons
            # DEBUG
            print("[DEBUG] Found {} images, start face cluster ...".format(total_image))

            from backend.display_by_person import load_json, write_json
            results = load_json(main_window.settings["output_path"])
            for item in results:
                k, v = item["person"], item["pic_name"]
                if k in persons.keys():
                    persons[k].append(v)
                else:
                    persons[k] = [v]
            if u"未命名" not in persons.keys():
                persons[u"未命名"] = image_paths
            else:
                persons[u"未命名"].extend(image_paths)
            write_json(persons, main_window.settings["output_path"])
            return {u"未命名": image_paths} # just do nothing

        def fake_image_search(image_args):
            print("[WARN] fake image search will ignore input images!")
            # always reset settings['image_path'] as test data dir
            main_window.settings['image_path'] = self._image_dir
            from backend.utils import get_image_paths
            return {"obama": get_image_paths(self._image_dir)}

        def fake_image_similarity(image_dir):
            print("[WARN] fake image similarity will ignore input image directory!")
            fake_result = [
                [
                    os.path.normpath(os.path.join(self._image_dir, "Obama_00.jpg")),
                    os.path.normpath(os.path.join(self._image_dir, "Obama_00.copy.jpg")),
                ],
                [
                    os.path.normpath(os.path.join(self._image_dir, "Obama_01.jpg")),
                    os.path.normpath(os.path.join(self._image_dir, "copy_01.jpg")),
                    os.path.normpath(os.path.join(self._image_dir, "copy_02.jpg")),
                ],
            ]
            return fake_result

        # create handler for supported task and thread worker
        self._task_handler = {
            "smart_album"  : [create_worker_smart_album,  fake_smart_album],
            "face_cluster" : [create_worker_face_cluster, fake_face_cluster],
            "image_search" : [create_worker_image_search, fake_image_search],
            "image_similarity" : [create_worker_image_similarity, fake_image_similarity],
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
    if name.lower() == "tiorb":
        from backend.tiorb.api import TiorbBackend
        return TiorbBackend(qw)
    raise RuntimeError("Unsupported backend: {}".format(name))
