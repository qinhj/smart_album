# ///////////////////////////////////////////////////////////////
#
# BY: qinhj@lsec.cc.ac.cn
#
# ///////////////////////////////////////////////////////////////

# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
import time
from backend.backend import IBackend
from backend.utils import get_duplicate_pics, get_image_paths, differ_paths
from backend.worker import Worker, create_search_worker, create_duplicate_worker
from backend.picf.utils.face_functions import search_person_pics, sorter_main
from backend.picf.utils import embedder as EMBEDDER

# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from gui.core.qt_core import *


def create_detect_worker_picf(main_window: QMainWindow, worker_handler, *args):
    if worker_handler is None:
        raise RuntimeError("Input worker handler for duplicate task is None!")

    if main_window.settings["image_path"] == "":
        QMessageBox.information(main_window, main_window.settings["app_name"], "还未选择图片文件夹，请先选择文件夹后再开始识别")
        return None

    copyright_label = main_window.ui.credits.copyright_label

    image_paths = get_image_paths(main_window.settings["image_path"])
    image_paths = differ_paths(image_paths, main_window.settings["output_path"], main_window.settings["image_path"])
    total_image = len(image_paths)
    if total_image == 0:
        copyright_label.setText("共有 0 张新增图片，识别取消")
        return None
    # DEBUG
    print("[DEBUG] Found {} images, start detection and recognition ...".format(total_image))

    timer_count = 0
    timer_start = time.time()
    timer = QTimer()
    
    def detect_print_time():
        try:
            processed_image = EMBEDDER.global_counter.value
        except AttributeError:
            processed_image = 0
        timer_count = int(time.time() - timer_start)
        if processed_image == 0:
            copyright_label.setText("正在加载模型，已开始 {} 秒".format(timer_count))
            #print("正在加载模型，已开始 {} 秒".format(timer_count))
        elif processed_image == total_image:
            copyright_label.setText("识别完成，正在分类，已开始 {} 秒".format(timer_count))
        else:
            copyright_label.setText("正在识别中，{}/{}，已开始 {} 秒".format(processed_image, total_image, timer_count))
            #print("正在识别中，{}/{}，已识别 {} 秒".format(processed_image, total_image, timer_count))

    timer.timeout.connect(lambda: detect_print_time())
    timer.start(100)

    def detect_finished():
        timer.stop()
        copyright_label.setText("完成识别，耗时 {} 秒".format(timer_count))
        QMessageBox.information(main_window, main_window.settings["app_name"], "完成识别")

    main_window.worker_detect = Worker(worker_handler, image_paths)
    main_window.worker_detect.finished.connect(detect_finished)
    main_window.worker_detect.start()


class PicfBackend(IBackend):

    def __init__(self, main_window: QMainWindow):
        super().__init__(main_window)
        # create handler for supported task and thread worker
        self._task_handler = {
            "Detect" : [create_detect_worker_picf, sorter_main],
            "Search" : [create_search_worker, search_person_pics],
            "Duplicate" : [create_duplicate_worker, get_duplicate_pics],
        }

    def __call__(self, cmd: str, *args):
        if cmd in self._task_handler.keys():
            worker, handler = self._task_handler[cmd]
            worker(self._main_window, handler, *args)
        else:
            raise RuntimeError("Unsupported command {}".format(cmd))

