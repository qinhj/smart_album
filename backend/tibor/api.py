# ///////////////////////////////////////////////////////////////
#
# BY: qinhj@lsec.cc.ac.cn
#
# ///////////////////////////////////////////////////////////////

# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
from backend.backend import IBackend
from backend.worker import create_worker_face_cluster
from backend.worker import create_worker_image_search
from backend.worker import create_worker_image_similarity
from backend.tibor.tibor_face_cluster import tibor_face_cluster
from backend.tibor.tibor_image_search import tibor_image_search
from backend.tibor.tibor_image_similarity import tibor_image_similarity

# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from gui.core.qt_core import *


class TiborBackend(IBackend):

    def __init__(self, main_window: QMainWindow):
        super().__init__(main_window)
        # create handler for supported task and thread worker
        self._task_handler = {
            "face_cluster" : [create_worker_face_cluster, tibor_face_cluster],
            "image_search" : [create_worker_image_search, tibor_image_search],
            "image_similarity" : [create_worker_image_similarity, tibor_image_similarity],
        }

    def __call__(self, cmd: str, *args):
        if cmd in self._task_handler.keys():
            worker, handler = self._task_handler[cmd]
            worker(self._main_window, handler, *args)
        else:
            raise RuntimeError("Unsupported command {}".format(cmd))

