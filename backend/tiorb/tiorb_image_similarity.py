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

def tiorb_image_similarity(image_dir, *args, **kwargs):
    result_file = os.path.normpath(os.path.join(kwargs["workspace"], "tiorb_similar.json"))
    args = ["/usr/bin/tiorb", "similar", image_dir, result_file]
    try:
        cp = run_subprocess(["mkdir -p {}".format(kwargs["workspace"])], shell=True)
        cp = run_subprocess(args, dll_path=None, shell=False)
        #print(cp)
    except Exception:
        import traceback
        traceback.print_exc()
        return []

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
    tiorb_image_similarity(os.path.realpath("data/images"), workspace="/tmp")
