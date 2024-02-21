# ///////////////////////////////////////////////////////////////
#
# BY: qinhj@lsec.cc.ac.cn
#
# ///////////////////////////////////////////////////////////////

# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
import time
from backend.utils import get_image_paths, differ_paths

# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from gui.core.qt_core import *


class Worker(QThread):
    finished = Signal(object) # Signal(dict)
    def __init__(self, handler, args):
        super().__init__()
        self._args = args
        self._handler = handler

    def run(self):
        result = self._handler(self._args)
        #print(result)
        self.finished.emit(result)


# Default worker for detection task
def create_detect_worker(main_window: QMainWindow, worker_handler, *args):
    if worker_handler is None:
        raise RuntimeError("Input worker handler for face detection task is None!")

    if main_window.settings["image_path"] == "":
        QMessageBox.information(main_window, main_window.settings["app_name"], "还未选择图片文件夹，请先选择文件夹后再开始识别")
        return None

    copyright_label = main_window.ui.credits.copyright_label

    image_paths = get_image_paths(main_window.settings["image_path"])
    image_paths = differ_paths(image_paths, main_window.settings["output_path"])
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
        timer_count = int(time.time() - timer_start)
        copyright_label.setText("正在识别中，已开始 {} 秒".format(timer_count))
        #print("正在识别中，{}/{}，已识别 {} 秒".format(processed_image, total_image, timer_count))

    timer.timeout.connect(lambda: detect_print_time())
    timer.start(100)

    def detect_finished(result):
        timer.stop()
        main_window.classification_result = result
        copyright_label.setText("完成识别，耗时 {} 秒".format(timer_count))
        QMessageBox.information(main_window, main_window.settings["app_name"], "完成识别")

    main_window.worker_detect = Worker(worker_handler, image_paths)
    main_window.worker_detect.finished.connect(detect_finished)
    main_window.worker_detect.start()


# Default worker for face search task
def create_search_worker(main_window: QMainWindow, worker_handler, *args):
    if worker_handler is None:
        raise RuntimeError("Input worker handler for face search task is None!")

    if main_window.settings["image_path"] == "":
        QMessageBox.information(main_window, main_window.settings["app_name"], "还未选择图片文件夹，请先选择文件夹后再开始识别")
        return None

    copyright_label = main_window.ui.credits.copyright_label
    #copyright_label.setText("正在进行人脸搜索，请稍等")

    timer_count = 0
    timer_start = time.time()
    timer = QTimer()

    def search_print_time():
        timer_count = int(time.time() - timer_start)
        copyright_label.setText("正在搜索中，已开始 {} 秒".format(timer_count))

    timer.timeout.connect(lambda: search_print_time())
    timer.start(100)

    def search_finished(result):
        timer.stop()
        main_window.person_search_result = result
        copyright_label.setText("搜索完成，耗时 {} 秒".format(timer_count))
        QMessageBox.information(main_window, main_window.settings["app_name"], "搜索完成")

    if main_window.selected_image is None or main_window.selected_image == '':
        QMessageBox.information(main_window, main_window.settings["app_name"], "还未选择照片，请先选择照片后再开始搜索")
    else:
        # TODO: decouple with input QWidget
        main_window.search_changed = True
        main_window.has_searched = True
        main_window.worker_search = Worker(worker_handler, main_window.selected_image)
        main_window.worker_search.finished.connect(search_finished)
        main_window.worker_search.start()


# Default worker for image duplicate task
def create_duplicate_worker(main_window: QMainWindow, worker_handler, *args):
    if worker_handler is None:
        raise RuntimeError("Input worker handler for duplicate task is None!")

    if main_window.settings["image_path"] == "":
        QMessageBox.information(main_window, main_window.settings["app_name"], "还未选择图片文件夹，请先选择文件夹后再开始识别")
        return None

    copyright_label = main_window.ui.credits.copyright_label
    #copyright_label.setText("正在进行相似图片筛查，请稍等")

    timer_start = time.time()
    timer_count = 0
    timer = QTimer()

    def dedup_print_time():
        timer_count = int(time.time() - timer_start)
        copyright_label.setText("正在筛查中，已开始 {} 秒".format(timer_count))

    timer.timeout.connect(lambda: dedup_print_time())
    timer.start(100)

    def dedup_finished(path):
        timer.stop()
        copyright_label.setText("筛查完成，耗时 {} 秒".format(timer_count))
        main_window.person_duplicate_result = path
        main_window.image_pages = []
        QMessageBox.information(main_window, main_window.settings["app_name"], "完成筛查")

    main_window.found_duplicate_image = True
    main_window.worker_duplicate = Worker(worker_handler, main_window.settings['image_path'])
    main_window.worker_duplicate.finished.connect(dedup_finished)
    main_window.worker_duplicate.start()
