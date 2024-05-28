# ///////////////////////////////////////////////////////////////
#
# BY: qinhj@lsec.cc.ac.cn
#
# ///////////////////////////////////////////////////////////////

# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
import time
from backend.callback import TaskState, ICallback

# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from gui.core.qt_core import *

from gui.uis.windows.main_window.functions_main_window import MainFunctions

class Worker(QThread):
    finished = Signal(object) # Signal(dict)
    def __init__(self, handler, arg, *args, **kwargs):
        super().__init__()
        self._arg = arg
        self._args = args
        self._kwargs = kwargs
        self._handler = handler

    def run(self):
        result = self._handler(self._arg, *self._args, **self._kwargs)
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
_TEXT_NEED_IMAGE_PATH = u"还未选择图片或输入文本，请先选择图片或输入文本后再执行"

# Default worker for smart album task
def create_worker_smart_album(main_window: QMainWindow, worker_handler, worker_callback: ICallback, *args, **kwargs):
    worker_callback("smart_album", TaskState.PREPARE, *args, **kwargs)

    if worker_handler is None:
        worker_callback("smart_album", TaskState.ERROR, "worker_handler is None!")
        raise RuntimeError("Input worker handler for smart album task is None!")

    if main_window.settings["image_path"] == "":
        QMessageBox.information(main_window, main_window.settings["app_name"], _TEXT_NEED_IMAGE_DIR)
        return None

    timer = TimerLabel(main_window.ui.credits.copyright_label)
    timer.start(100)

    def generate_finished(result):
        timer.stop()
        main_window.smart_album_result = result
        QMessageBox.information(main_window, main_window.settings["app_name"], u"智能影集生成完毕{}".format(_TEXT_FILL_BLANK))
        worker_callback("smart_album", TaskState.FINISHED, *args, **kwargs)

    worker_callback("smart_album", TaskState.RUNNING, *args, **kwargs)
    main_window.smart_album_worker = Worker(worker_handler, main_window.settings["image_path"], *args, **kwargs)
    main_window.smart_album_worker.finished.connect(generate_finished)
    main_window.smart_album_worker.start()


# Default worker for face cluster task
def create_worker_face_cluster(main_window: QMainWindow, worker_handler, worker_callback: ICallback, *args, **kwargs):
    worker_callback("face_cluster", TaskState.PREPARE, *args, **kwargs)

    if worker_handler is None:
        worker_callback("face_cluster", TaskState.ERROR, "worker_handler is None!")
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
        worker_callback("face_cluster", TaskState.FINISHED, *args, **kwargs)

    worker_callback("face_cluster", TaskState.RUNNING, *args, **kwargs)
    main_window.face_cluster_worker = Worker(worker_handler, main_window.settings["image_path"], *args, **kwargs)
    main_window.face_cluster_worker.finished.connect(cluster_finished)
    main_window.face_cluster_worker.start()


# Default worker for image search task
def create_worker_image_search(main_window: QMainWindow, worker_handler, worker_callback: ICallback, *args, **kwargs):
    worker_callback("image_search", TaskState.PREPARE, *args, **kwargs)

    if worker_handler is None:
        worker_callback("image_search", TaskState.ERROR, "worker_handler is None!")
        raise RuntimeError("Input worker handler for image search task is None!")

    if main_window.settings["image_path"] == "":
        QMessageBox.information(main_window, main_window.settings["app_name"], _TEXT_NEED_IMAGE_DIR)
        return None

    if main_window.selected_image is None or main_window.selected_image == '':
        QMessageBox.information(
            main_window, main_window.settings["app_name"], _TEXT_NEED_IMAGE_PATH)
        return None

    timer = TimerLabel(main_window.ui.credits.copyright_label)
    timer.start(100)

    def search_finished(result):
        timer.stop()
        main_window.image_search_result = result
        QMessageBox.information(main_window, main_window.settings["app_name"], u"智能搜图完成{}".format(_TEXT_FILL_BLANK))
        worker_callback("image_search", TaskState.FINISHED, *args, **kwargs)

    worker_callback("image_search", TaskState.RUNNING, *args, **kwargs)
    main_window.image_search_worker = Worker(worker_handler, [main_window.settings["image_path"], main_window.selected_image], *args, **kwargs)
    main_window.image_search_worker.finished.connect(search_finished)
    main_window.image_search_worker.start()


# Default worker for image similarity task
def create_worker_image_similarity(main_window: QMainWindow, worker_handler, worker_callback: ICallback, *args, **kwargs):
    worker_callback("image_similarity", TaskState.PREPARE, *args, **kwargs)

    if worker_handler is None:
        worker_callback("image_similarity", TaskState.ERROR, "worker_handler is None!")
        raise RuntimeError("Input worker handler for image similarity task is None!")

    if main_window.settings["image_path"] == "":
        QMessageBox.information(main_window, main_window.settings["app_name"], _TEXT_NEED_IMAGE_DIR)
        return None

    timer = TimerLabel(main_window.ui.credits.copyright_label)
    timer.start(100)

    def similarity_finished(path):
        timer.stop()
        main_window.image_similarity_result = path
        main_window.image_similarity_pages = [] # reset PyImagePage list
        QMessageBox.information(main_window, main_window.settings["app_name"], u"智能筛重完成{}".format(_TEXT_FILL_BLANK))
        worker_callback("image_similarity", TaskState.FINISHED, *args, **kwargs)

    worker_callback("image_similarity", TaskState.RUNNING, *args, **kwargs)
    main_window.image_similarity_worker = Worker(worker_handler, main_window.settings['image_path'], *args, **kwargs)
    main_window.image_similarity_worker.finished.connect(similarity_finished)
    main_window.image_similarity_worker.start()
    main_window.image_similarity_done = True
