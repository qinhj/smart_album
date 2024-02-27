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
default_bin = os.path.normpath(os.path.join(parent, "Linux_cluster"))
default_model = os.path.normpath(os.path.join(parent, "models", "face"))
default_threads = "16"
default_workspace = os.path.normpath(os.path.join(parent, "temp", "face"))

def tiorb_face_cluster(image_dir, model_dir = default_model,
                       output_dir = default_workspace, thread_num: str = default_threads):
    args = [default_bin, thread_num, model_dir, image_dir, output_dir]
    cp = run_subprocess(["mkdir -p {}".format(output_dir)], shell=True)
    cp = run_subprocess(args, dll_path=parent, shell=False)
    #print(cp)

    result_file = os.path.normpath(os.path.join(output_dir, "result.json"))
    override_file = os.path.normpath(os.path.join(parent, "..", "..", "output.json"))
    cp = run_subprocess(["cp -f {} {}".format(result_file, override_file)], shell=True)
    with open(result_file, 'r', encoding='utf-8') as fin:
        result_info = json.load(fin)
    return result_info # List(dict)


if __name__ == "__main__":
    tiorb_face_cluster(os.path.realpath("data/images"))
