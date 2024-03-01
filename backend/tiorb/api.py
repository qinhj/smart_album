# ///////////////////////////////////////////////////////////////
#
# BY: qinhj@lsec.cc.ac.cn
#
# ///////////////////////////////////////////////////////////////

# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
from backend.backend import IBackend
from backend.worker import create_worker_smart_album
from backend.worker import create_worker_face_cluster
from backend.worker import create_worker_image_search
from backend.worker import create_worker_image_similarity
from backend.tiorb.tiorb_smart_album import tiorb_smart_album
from backend.tiorb.tiorb_face_cluster import tiorb_face_cluster
from backend.tiorb.tiorb_image_search import tiorb_image_search
from backend.tiorb.tiorb_image_similarity import tiorb_image_similarity

# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from gui.core.qt_core import *


class TiorbBackend(IBackend):

    def __init__(self, main_window: QMainWindow):
        super().__init__(main_window)
        # create handler for supported task and thread worker
        self._task_handler = {
            "smart_album"  : [create_worker_smart_album,  tiorb_smart_album],
            "face_cluster" : [create_worker_face_cluster, tiorb_face_cluster],
            "image_search" : [create_worker_image_search, tiorb_image_search],
            "image_similarity" : [create_worker_image_similarity, tiorb_image_similarity],
        }
        self._workspace = main_window.workspace
        if self._workspace is None:
            self._workspace = "/tmp"

    def __call__(self, cmd: str, *args, **kwargs):
        if cmd in self._task_handler.keys():
            # add workspace to input kwargs
            kwargs["workspace"] = self._workspace
            worker, handler = self._task_handler[cmd]
            worker(self._main_window, handler, *args, **kwargs)
        else:
            raise RuntimeError("Unsupported command {}".format(cmd))

