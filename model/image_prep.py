import glob 

main_path = "flickr8k_dataset..."

img = glob.glob(main_path + '*.jpg')
train_path = main_path + '/'
train_img = open(train_path, 'r', encoding='utf-8').read().split('\n')
train_img = []

for i in img:
    if (i[len(main_path):] in train_img):
        train_img.append(i)