import json
import os


def load_json(jsonfile):
    # format: [{"person": xxx, "pic_name": yyy}, {...}]
    with open(jsonfile, 'r', encoding='utf-8') as f:
        images = json.load(f)
    return images


def write_json(person_dict, filepath = "output.json"):
    """
        Input  format: {"name1": [path11, path12, ...], "name2": [path21, path22, ...], ...}
        Output format: [{"person": xxx, "pic_name": yyy}, {...}]
    """
    images = []
    for name, paths in person_dict.items():
        images.extend([{
            "pic_name": path, # os.path.basename(path)
            "person": name,
            } for path in paths
        ])
    images.sort(key=lambda x: x['person'])
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(json.dumps(images, indent=4, ensure_ascii=False, sort_keys=True))


def load_person_dict(jsonfile):
    """
        Input  : json [{"person": xxx, "pic_name": yyy}, {...}]
        Return : dict {name: [img1, img2, ...]}
    """
    image_info = load_json(jsonfile)
    person_dict = {}
    for info in image_info:
        k, v = info["person"], info["pic_name"]
        if k not in person_dict.keys():
            person_dict[k] = [v]
        else:
            person_dict[k].append(v)
    return person_dict


def update_group_name(name_new, name_old, person_dict):
    if name_new not in person_dict:
        person_dict[name_new] = person_dict.pop(name_old)
    else:
        person_dict[name_new].extend(person_dict.pop(name_old))
    return person_dict


def edit_single_image_label(
        new_group_name, path, filepath: str = "output.json", person_dict: dict = None):
    if person_dict is None:
        person_dict = load_person_dict(filepath)
    name_to_delete = []
    for name, paths in person_dict.items():
        if path in paths:
            if name == new_group_name:
                print("[WARN] ignore update image label since no change")
                return person_dict
            person_dict[name].remove(path)
            if len(paths) == 0:
                name_to_delete.append(name)
            break
    for _key in name_to_delete:
        _ = person_dict.pop(_key)
    if new_group_name in person_dict:
        person_dict[new_group_name].append(path)
    else:
        person_dict[new_group_name] = [path]
    write_json(person_dict, filepath)
    return person_dict


def delete_images(target_paths, filepath = "output.json"):
    person_dict = load_person_dict(filepath)
    empty_names = []
    # update output json
    for name, paths in person_dict.items():
        for path in target_paths[::-1]:
            if path in paths:
                paths.remove(path)
        person_dict[name] = paths
        if len(paths) == 0:
            empty_names.append(name)
    for name in empty_names:
        person_dict.pop(name)
    write_json(person_dict, filepath)
    # remove selected images
    for path in target_paths:
        try:
            os.remove(path)
            print("[INFO] Image {} has been removed".format(path))
        except FileNotFoundError:
            print("[ERROR] Image {} not found!".format(path))
            pass
    return person_dict
