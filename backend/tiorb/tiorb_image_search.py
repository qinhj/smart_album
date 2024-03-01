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

def tiorb_image_search(image_args, *args, **kwargs):
    result_file = os.path.normpath(os.path.join(kwargs["workspace"], "tiorb_search.json"))
    image_dir, image_or_text = image_args[:2]
    args = ["/usr/bin/tiorb", "search", image_dir, result_file, image_or_text]
    try:
        cp = run_subprocess(["mkdir -p {}".format(kwargs["workspace"])], shell=True)
        cp = run_subprocess(args, dll_path=None, shell=False)
        #print(cp)
    except Exception:
        import traceback
        traceback.print_exc()
        return {}

    with open(result_file, 'r', encoding='utf-8') as fin:
        result_info = json.load(fin)
    return result_info


if __name__ == "__main__":
    for text in ["美女", "小草", "天空"]:
        tiorb_image_search([os.path.realpath("data/images"), text], workspace="/tmp")
