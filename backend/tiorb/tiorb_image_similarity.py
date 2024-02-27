# ///////////////////////////////////////////////////////////////
#
# BY: qinhj@lsec.cc.ac.cn
#
# ///////////////////////////////////////////////////////////////

# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
import os
import json

from backend.run import run_subprocess

parent = os.path.dirname(os.path.realpath(__file__))
default_bin = os.path.normpath(os.path.join(parent, "Linux_similar"))
default_model = os.path.normpath(os.path.join(parent, "models", "similar"))
default_threads = "4"
default_workspace = os.path.normpath(os.path.join(parent, "temp", "similar"))

def tiorb_image_similarity(image_dir, model_dir = default_model, output_dir = default_workspace,
                  thread_num: str = default_threads, use_gpu: str = "0"):
    args = [default_bin, thread_num, model_dir, image_dir, output_dir, use_gpu]
    cp = run_subprocess(["mkdir -p {}".format(output_dir)], shell=True)
    cp = run_subprocess(args, dll_path=parent, shell=False)
    #print(cp)

    result_file = os.path.normpath(os.path.join(output_dir, "result.json"))
    with open(result_file, 'r', encoding='utf-8') as fin:
        result_info = json.load(fin)
    # convert {"path": "label"} => {"label": ["path", ...]}
    result_dict = {}
    for path, label in result_info.items():
        if label not in result_dict.keys():
            result_dict[label] = [path]
        else:
            result_dict[label].append(path)
    result_labels = sorted(result_dict.keys())
    result_list = [sorted(result_dict[label]) for label in result_labels]
    return result_list


if __name__ == "__main__":
    tiorb_image_similarity(os.path.realpath("data/images"))
