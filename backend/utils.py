# ///////////////////////////////////////////////////////////////
#
# BY: qinhj@lsec.cc.ac.cn
#
# ///////////////////////////////////////////////////////////////

# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
import os
import sys
import json

# FUNCTIONS

def get_duplicate_pics(image_dir):
    """ 相似性筛查 """
    from imagededup.methods import PHash
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


def get_image_paths(root_dir):
    """
    Brief:  Generates a list of paths for the images in a root directory and ignores rest of the files
    Args:
        root_dir : string containing the relative path to root directory
    Returns:
        image_list : list containing paths of the images in the directory
    """
    if not os.path.exists(root_dir):
        print("Directory not found, please enter valid directory..")
        sys.exit(1)
    image_list = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp')):
                image_list.append(os.path.normpath(os.path.join(dirpath, filename)))
    return image_list


def differ_paths(image_list: list, json_file: str, root_dir: str = None):
    # 从 image_list 中剔除已存在于 json_file 中的图片并返回
    with open(json_file, 'r', encoding='utf-8') as f:
        image_info = json.load(f)   # list of dict: [{"person":name,"pic_name":path}]
        image_exist = [info["pic_name"] for info in image_info]
        if root_dir:
            image_exist = [os.path.normpath(os.path.join(root_dir, image)) for image in image_exist]
        image_diff = set(image_list).difference(set(image_exist))
        return list(image_diff)
