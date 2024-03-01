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

def tiorb_smart_album(image_dir, *args, **kwargs):
    result_file = os.path.normpath(os.path.join(kwargs["workspace"], "tiorb_album.json"))
    args = ["/usr/bin/tiorb", "album", image_dir, result_file]
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
    return result_info # List(dict)


if __name__ == "__main__":
    tiorb_smart_album(os.path.realpath("data/images"), workspace="/tmp")
