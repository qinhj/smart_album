# ///////////////////////////////////////////////////////////////
#
# BY: qinhj@lsec.cc.ac.cn
#
# ///////////////////////////////////////////////////////////////

# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
import time

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


class TimerLabel(QTimer):
    def __init__(self, label):
        super().__init__()
        self._label = label
        self._count = 0
        self._start = time.time()
        #self._label.setText(u"正在分析中，请稍等")

        def slot_update_text():
            self._count = int(time.time() - self._start)
            self._label.setText(u"智能分析中, 已开始 {}s".format(self._count))
        self.timeout.connect(lambda: slot_update_text())

    def stop(self):
        super().stop()
        self._count = int(time.time() - self._start)
        self._label.setText(u"智能分析完成, 总耗时 {}s".format(self._count))


_TEXT_NEED_IMAGE_DIR = u"还未选择图片文件夹，请先选择文件夹"
_TEXT_FILL_BLANK = "                                    "

# Default worker for face cluster task
def create_worker_face_cluster(main_window: QMainWindow, worker_handler, *args):
    if worker_handler is None:
        raise RuntimeError("Input worker handler for face cluster task is None!")

    if main_window.settings["image_path"] == "":
        QMessageBox.information(main_window, main_window.settings["app_name"], _TEXT_NEED_IMAGE_DIR)
        return None

    timer = TimerLabel(main_window.ui.credits.copyright_label)
    timer.start(100)

    def cluster_finished(result):
        timer.stop()
        main_window.face_cluster_result = result
        QMessageBox.information(main_window, main_window.settings["app_name"], u"人脸聚类完成{}".format(_TEXT_FILL_BLANK))

    main_window.face_cluster_worker = Worker(worker_handler, main_window.settings["image_path"])
    main_window.face_cluster_worker.finished.connect(cluster_finished)
    main_window.face_cluster_worker.start()


# Default worker for image search task
def create_worker_image_search(main_window: QMainWindow, worker_handler, *args):
    if worker_handler is None:
        raise RuntimeError("Input worker handler for image search task is None!")

    if main_window.settings["image_path"] == "":
        QMessageBox.information(main_window, main_window.settings["app_name"], _TEXT_NEED_IMAGE_DIR)
        return None

    timer = TimerLabel(main_window.ui.credits.copyright_label)
    timer.start(100)

    def search_finished(result):
        timer.stop()
        main_window.image_search_result = result
        QMessageBox.information(main_window, main_window.settings["app_name"], u"智能搜图完成{}".format(_TEXT_FILL_BLANK))

    if main_window.selected_image is None or main_window.selected_image == '':
        QMessageBox.information(
            main_window, main_window.settings["app_name"],
            u"还未选择图片或输入文本，请先选择图片或输入文本后再执行")
    else:
        # TODO: decouple with input main_window?
        main_window.image_search_changed = True
        main_window.image_search_worker = Worker(worker_handler, [main_window.settings["image_path"], main_window.selected_image])
        main_window.image_search_worker.finished.connect(search_finished)
        main_window.image_search_worker.start()
        main_window.image_search_done = True


# Default worker for image similarity task
def create_worker_image_similarity(main_window: QMainWindow, worker_handler, *args):
    if worker_handler is None:
        raise RuntimeError("Input worker handler for image similarity task is None!")

    if main_window.settings["image_path"] == "":
        QMessageBox.information(main_window, main_window.settings["app_name"], _TEXT_NEED_IMAGE_DIR)
        return None

    timer = TimerLabel(main_window.ui.credits.copyright_label)
    timer.start(100)

    def similarity_finished(path):
        timer.stop()
        main_window.image_similarity_result = path
        main_window.image_pages = []
        QMessageBox.information(main_window, main_window.settings["app_name"], u"智能筛重完成{}".format(_TEXT_FILL_BLANK))

    main_window.image_similarity_worker = Worker(worker_handler, main_window.settings['image_path'])
    main_window.image_similarity_worker.finished.connect(similarity_finished)
    main_window.image_similarity_worker.start()
    main_window.image_similarity_done = True
