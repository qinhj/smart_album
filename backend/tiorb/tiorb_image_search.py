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
default_bin = os.path.normpath(os.path.join(parent, "Linux_search"))
default_model = os.path.normpath(os.path.join(parent, "models", "nli"))
default_threshold = "0.0"
default_threads = "16"
default_workspace = os.path.normpath(os.path.join(parent, "temp", "nli"))

def tiorb_image_search(image_args, model_dir = default_model, output_dir = default_workspace,
                 thread_num: str = default_threads, threshold: str = default_threshold):
    image_dir, image_or_text = image_args[:2]
    args = [default_bin, thread_num, model_dir, image_or_text, threshold, image_dir, output_dir]
    cp = run_subprocess(["mkdir -p {}".format(output_dir)], shell=True)
    cp = run_subprocess(args, dll_path=parent, shell=False)
    #print(cp)

    result_file = os.path.normpath(os.path.join(output_dir, "result.json"))
    with open(result_file, 'r', encoding='utf-8') as fin:
        result_info = json.load(fin)
    return result_info


if __name__ == "__main__":
    for text in ["美女", "小草", "天空"]:
        tiorb_image_search([os.path.realpath("data/images"), text])
