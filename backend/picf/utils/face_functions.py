from . sort_images import sort_images
from backend.display_by_person import  get_persons, get_persons_more,  print_by_person
import time
from . embedder import embedder
import json
import os
import shutil
import sys
from backend.display_by_person import *
from . facenet import compute_embedding
from . CW import draw_graph, chinese_whispers
from . sort_images import image_sorter
from tensorflow.keras.models import load_model

default_model = None
default_model_detector = None

def sorter_main(image_paths):
    t0 = time.time()
    if embedder(image_paths):
        sort_images()
        print(time.time()-t0)
        #persons = get_persons('output.json')
        #persons = get_persons_more(persons)
        #print_by_person(persons)
    return {}

def copy_images():
    root = './Sorted-pictures'
    persons = get_persons('output.json')
    persons = get_persons_more(persons)
    for name, paths in persons.items():
        destination = os.path.join(root,name)
        if not os.path.exists(destination ):
            os.mkdir(destination )
        for path in paths:
            try: 
                shutil.copy(path,destination)
            except FileNotFoundError:
                pass

def get_image_folder():
    with open('resources\settings.json', 'r+',encoding='utf-8') as f:
        settings = json.load(f)
    return settings['image_path']

######################################################################
# 人脸搜索接口
def search_person_pics(path, model = None, model_detector = None):
    global default_model
    global default_model_detector
    try:
        if model is None:
            if default_model is None:
                default_model = load_model("Models/facenet.h5")
            model = default_model
        if model_detector is None:
            if default_model_detector is None:
                default_model_detector = load_model("Models/RFB.h5",compile=False)
            model_detector = default_model_detector
    except Exception:
        print("[ERROR] Load tensorflow model failed!")
        return {}

    args = {'threshold': 0.67, 'iterations': 30}

    data = load_pickle('embeddings.pickle')
    user_embedding = compute_embedding(path, model, model_detector)

    if user_embedding is None:
        # cv2.imread() returns a NoneType object instead of throwing an error for invalid image paths
        print("Image not found, please enter valid image path")
        sys.exit(1)

    elif user_embedding.shape[0] > 1:
        print("Found more than one face in picture. Please give a picture with only one face..")
        sys.exit(1)

    elif user_embedding.shape[0] == 0:
        print("Found no faces. Please give a picture with a face..")
        sys.exit(1)

    data.append({"path":path,"embedding":user_embedding[0]})

    graph = draw_graph(data,args["threshold"])
    graph = chinese_whispers(graph,args["iterations"])

    images = image_sorter(graph)

    for image in images:
        if image['pic_name'] == os.path.basename(path):
            images.remove(image)
            name = image['person']
    
    #print(name)
    persons = sort_by_person(images)
    temp_persons = {name:persons[name]}
    print(path)
    print_by_person(temp_persons)
    return temp_persons


if __name__ == '__main__':
    #sorter_main('./image')
    path = 'test_image\Biden_01.jpeg'
    search_person_pics(path)
    #print(select_image_folder())
    #print(get_image_folder())
    '''
    #persons = edit_single_group_name("妹妹","./additional\\122.jpg",persons)
    print(time.time()-t0)
    print_by_person(persons)
    print(time.time()-t0)
    print(time.time()-t0)
    #cos = get_similarity(embeddings[0],embeddings[1])
    #print(cos)
    img = './test_image/TEST_02.jpg'
    load_and_align(img)
    
    #删除某张图片
    persons = get_persons("output.json")
    print(time.time()-t0)
    persons = delete_single_pic('./image_backup\\003.jpg',persons)
    write_json(persons)
    print_by_person(persons)
    #将图片复制到目标
    root = "Sorted-pictures"
    if not os.path.exists(root):
        os.mkdir(root)
    
    persons = get_persons('output.json')
    persons = get_persons_more(persons)
    for name, paths in persons.items():
        destination = os.path.join(root,name)
        if not os.path.exists(destination ):
            os.mkdir(destination )
        for path in paths:
            try: 
                shutil.copy(path,destination)
            except FileNotFoundError:
                pass
    '''
