import json
import pickle
import os
import re

def load_json(jsonfile):
    # format: [{"person": xxx, "pic_name": yyy}, {...}]
    with open(jsonfile, 'r', encoding='utf-8') as f:
        images = json.load(f)
    return images

def sort_by_person(images):
    #输入[{"person":name,"pic_name":path}]形式的列表，返回{name:[paths]}形式的字典
    persons = {}
    for image in images:
        path = image['pic_name']
        name = image['person']
        if name not in persons:
            persons[name] = []
        persons[name].append(path)
    return persons

def get_persons(jsonfile):
    #输入json文件名，返回{name:[paths]}形式的字典
    images = load_json(jsonfile)
    persons = sort_by_person(images)
    return persons

def get_persons_more(persons):
    #输入{name:[paths]}形式的字典，去除paths个数小于等于3的节点，返回{name:[paths]}形式的字典
    person_to_delete = []
    for name, paths in list(persons.items()):
        if name == "未命名":
            continue
        if len(paths) <= 3 or name == "错误分类":
            person_to_delete.append(name)
    for person in person_to_delete:
        persons.pop(person)
    return persons
    
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


def print_by_person(persons):
    #将{name:[paths]}形式的字典按"人名:图片组"的形式格式化输出
    for name, paths in persons.items():
        print("------------------------------")
        print()
        print("Name:{}".format(name))
        for count,path in enumerate(paths):
            index = path.rfind('\\', 0, len(path))
            print("{}:{}".format(count, path[index+1:]))
        print()
    print("------------------------------")

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


def load_pickle(picklefile):
    #输入embeddings.pickle的路径，返回[{"path":path,"embedding":np_array}]类型的列表
    datas = pickle.load(open(picklefile,"rb"))
    return datas

def write_pickle(datas):
    #输入[{"path":path,"embedding":np_array}]类型的列表，写入embeddings.pickle
    with open("embeddings.pickle", "wb") as f: 
        pickle.dump(datas, f)


def delete_single_pic(target_path, persons):
    # 输入图片路径target_path和{name:[paths]}形式的字典
    # 将target_path对应的图片从embeddings.pickle中删除，
    # 将target_path对应的图片从{name:[paths]}形式的字典中删除，返回修改过的{name:[paths]}形式的字典

    #从persons里删除单张照片
    empty_names =[]
    for name, paths in persons.items():
        if target_path in paths:
            paths.remove(target_path)
            persons[name] = paths
            try:
                os.remove(target_path)
            except FileNotFoundError:
                pass
        if len(paths) == 0:
            empty_names.append(name)
    for name in empty_names:
        persons.pop(name)

    #从embeddings.pickle里删除单张照片
    pickle_datas = load_pickle("embeddings.pickle")
    pickle_to_delete = []
    for index, pickle_data in enumerate(pickle_datas):
        if target_path == pickle_data["path"]:
            pickle_to_delete.append(index)
    for index in pickle_to_delete:
        pickle_datas.pop(index)
    write_pickle(pickle_datas)

    return persons

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
