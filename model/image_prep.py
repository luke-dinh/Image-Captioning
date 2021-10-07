import glob
from load_des import prep_cap

main_path = "flickr8k_dataset"
cap_path = "captions.txt"

img = glob.glob(main_path + '/images' + '*.jpg')
train_path = main_path + '/'
train_img = open(train_path, 'r', encoding='utf-8').read().split('\n')
train_img = []

for i in img:
    if (i[len(main_path):] in train_img):
        train_img.append(i)

def load_clean_cap(des, dataset):

    dataset_des = dict()

    for key, des_list in dataset_des.items():
        if key + '.jpg' in dataset:
            if key not in dataset_des:
                dataset_des[key] = list()
            for line in des_list:
                desc = 'startseq' + line + 'endseq'
                dataset_des[key].append(desc)
                
    return dataset_des

doc = prep_cap.load_doc(cap_path)
descriptions = prep_cap.load_cap(doc)
