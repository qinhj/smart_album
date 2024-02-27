# ///////////////////////////////////////////////////////////////
#
# BY: qinhj@lsec.cc.ac.cn
#
# ///////////////////////////////////////////////////////////////

# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
import time
from backend.backend import IBackend
from backend.utils import get_image_paths, differ_paths
from backend.worker import Worker, TimerLabel, _TEXT_NEED_IMAGE_DIR, _TEXT_FILL_BLANK
from backend.worker import create_worker_image_search
from backend.worker import create_worker_image_similarity
from backend.picf.utils.face_functions import search_person_pics, sorter_main
from backend.picf.utils import embedder as EMBEDDER

# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from gui.core.qt_core import *


def get_duplicate_pics(image_dir):
    """ 相似性筛查 """
    from . imagededup.methods import PHash
    phasher = PHash()
    try:
        encodings = phasher.encode_images(image_dir=image_dir)
    except Exception:
        print("[ERROR] phasher.encode_images failed, input image dir: {}".format(image_dir))
        return []
    duplicates = phasher.find_duplicates(encoding_map=encodings)
    #print(duplicates)

    duplicated_pics = []
    for pic, sim_pics in duplicates.items():
        if sim_pics:
            sim_pics.append(pic)
            sim_pics = sorted(sim_pics)
            #print(sim_pics)
            has_union_pics = False
            for index, existed_sim_pics in enumerate(duplicated_pics):
                set_sim_pics = set(sim_pics)
                set_existed_sim_pics = set(existed_sim_pics)
                if len(set_sim_pics.intersection(set_existed_sim_pics)) != 0:
                    duplicated_pics[index] = list(set_existed_sim_pics.union(set_sim_pics))
                    has_union_pics = True
                    break
                    #sim_pics.extend(existed_sim_pics)
            if not has_union_pics:
                duplicated_pics.append(sim_pics)
    print("GET Duplicated Pics Done")
    for pics in duplicated_pics:
        print(pics)
    return duplicated_pics


class TimerLabelPicf(TimerLabel):
    def __init__(self, label, total: int):
        super().__init__(label=label)
        self._total = total

        def slot_update_text():
            self._count = int(time.time() - self._start)
            try:
                processed_image = EMBEDDER.global_counter.value
            except AttributeError:
                processed_image = 0
            if processed_image == 0:
                self._label.setText(u"正在加载模型, 已开始 {}s".format(self._count))
            elif processed_image == self._total:
                self._label.setText(u"识别完成，正在分类，已开始 {} 秒".format(self._total))
            else:
                self._label.setText(u"正在识别中，{}/{}，已开始 {} 秒".format(processed_image, self._total, self._count))
        self.timeout.connect(lambda: slot_update_text())

    def stop(self):
        super().stop()
        self._count = int(time.time() - self._start)
        self._label.setText(u"完成识别, 总耗时 {}s".format(self._count))


# Default worker for face cluster task
def create_worker_face_cluster_picf(main_window: QMainWindow, worker_handler, *args):
    if worker_handler is None:
        raise RuntimeError("Input worker handler for face cluster task is None!")

    if main_window.settings["image_path"] == "":
        QMessageBox.information(main_window, main_window.settings["app_name"], _TEXT_NEED_IMAGE_DIR)
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

    timer = TimerLabelPicf(copyright_label, total_image)
    timer.start(100)

    def cluster_finished(result):
        timer.stop()
        main_window.face_cluster_result = result
        QMessageBox.information(main_window, main_window.settings["app_name"], u"人脸聚类完成{}".format(_TEXT_FILL_BLANK))

    main_window.face_cluster_worker = Worker(worker_handler, main_window.settings["image_path"])
    main_window.face_cluster_worker.finished.connect(cluster_finished)
    main_window.face_cluster_worker.start()


class PicfBackend(IBackend):

    def __init__(self, main_window: QMainWindow):
        super().__init__(main_window)
        # create handler for supported task and thread worker
        self._task_handler = {
            "face_cluster" : [create_worker_face_cluster_picf, sorter_main],
            "image_search" : [create_worker_image_search, search_person_pics],
            "image_similarity" : [create_worker_image_similarity, get_duplicate_pics],
        }

    def __call__(self, cmd: str, *args):
        if cmd in self._task_handler.keys():
            worker, handler = self._task_handler[cmd]
            worker(self._main_window, handler, *args)
        else:
            raise RuntimeError("Unsupported command {}".format(cmd))

